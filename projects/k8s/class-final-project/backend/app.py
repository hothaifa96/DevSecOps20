from __future__ import annotations

import os
import random
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request
from flask_cors import CORS

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "autoscan.db"


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config["JSON_SORT_KEYS"] = False

    init_db()

    @app.route("/api/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok", "service": "autoscan-backend"})

    @app.route("/api/scans", methods=["GET"])
    def list_scans():
        rows = fetch_scans()
        return jsonify({"items": rows})

    @app.route("/api/scans", methods=["POST"])
    def create_scan():
        data = request.get_json(force=True, silent=True) or {}
        target = (data.get("target") or "").strip() or "internal"
        automation_mode = (data.get("automationMode") or "automated").lower()

        findings = simulate_scan(target, automation_mode)
        scan_id = insert_scan(
            target=target,
            automation_mode=automation_mode,
            status=findings["status"],
            summary=findings["summary"],
        )

        return jsonify({"id": scan_id, "result": findings}), 201

    @app.route("/api/env", methods=["GET"])
    def env_snapshot():
        allowed_keys = {
            "ENV",
            "PYTHONPATH",
            "FLASK_ENV",
            "AUTOSCAN_PROFILE",
            "AUTOSCAN_REGION",
        }
        env_values = {
            key: os.environ.get(key, "")
            for key in sorted(allowed_keys)
            if os.environ.get(key)
        }
        return jsonify(
            {
                "python_version": sys.version,
                "working_directory": str(os.getcwd()),
                "database_path": str(DB_PATH),
                "exposed_env": env_values,
            }
        )

    return app


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS scan_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                automation_mode TEXT NOT NULL,
                status TEXT NOT NULL,
                summary TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def fetch_scans() -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, target, automation_mode, status, summary, created_at "
            "FROM scan_runs ORDER BY created_at DESC LIMIT 20"
        ).fetchall()
        return [dict(row) for row in rows]


def insert_scan(
    *, target: str, automation_mode: str, status: str, summary: str
) -> int:
    created_at = datetime.utcnow().isoformat() + "Z"
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            """
            INSERT INTO scan_runs (target, automation_mode, status, summary, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (target, automation_mode, status, summary, created_at),
        )
        conn.commit()
        return cursor.lastrowid


def simulate_scan(target: str, automation_mode: str) -> dict:
    """Return mock findings to mimic an automation-assisted scan."""
    statuses = ["passed", "warning", "failed"]
    status = random.choices(statuses, weights=[0.6, 0.3, 0.1], k=1)[0]
    snippets = {
        "passed": f"{target} cleared {automation_mode} checks.",
        "warning": f"{target} has drift indicators; schedule manual follow-up.",
        "failed": f"{target} triggered critical policy violations.",
    }
    return {"status": status, "summary": snippets[status]}


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

