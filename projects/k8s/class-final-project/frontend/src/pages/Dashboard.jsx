import { useEffect, useState } from 'react'
import { getScans, runScan } from '../services/api.js'

const defaultForm = {
  target: 'https://internal.cluster',
  automationMode: 'automated',
}

function Dashboard() {
  const [form, setForm] = useState(defaultForm)
  const [scans, setScans] = useState([])
  const [busy, setBusy] = useState(false)
  const [error, setError] = useState('')

  const loadScans = async () => {
    try {
      setError('')
      const items = await getScans()
      setScans(items)
    } catch (err) {
      setError(err.message)
    }
  }

  useEffect(() => {
    loadScans()
  }, [])

  const onSubmit = async (evt) => {
    evt.preventDefault()
    setBusy(true)
    try {
      await runScan(form)
      setForm((current) => ({ ...current, target: '' }))
      await loadScans()
    } catch (err) {
      setError(err.message)
    } finally {
      setBusy(false)
    }
  }

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <h1>Automation sandbox</h1>
          <p>Kick off a mock scan that the Flask backend tracks inside SQLite.</p>
        </div>
      </div>

      <form className="scan-form" onSubmit={onSubmit}>
        <label>
          Target to scan
          <input
            type="text"
            required
            placeholder="cluster, domain, or repo"
            value={form.target}
            onChange={(evt) => setForm({ ...form, target: evt.target.value })}
          />
        </label>
        <label>
          Automation mode
          <select
            value={form.automationMode}
            onChange={(evt) => setForm({ ...form, automationMode: evt.target.value })}
          >
            <option value="automated">Automated</option>
            <option value="augmented">Augmented</option>
            <option value="manual">Manual</option>
          </select>
        </label>
        <button type="submit" disabled={busy}>
          {busy ? 'Scheduling…' : 'Run lightning scan'}
        </button>
      </form>

      {error && <p className="error">{error}</p>}

      <div className="scan-table">
        {scans.length === 0 ? (
          <p>No scans yet. Launch one to populate the log.</p>
        ) : (
          <table>
            <thead>
              <tr>
                <th>Time (UTC)</th>
                <th>Target</th>
                <th>Mode</th>
                <th>Status</th>
                <th>Summary</th>
              </tr>
            </thead>
            <tbody>
              {scans.map((scan) => (
                <tr key={scan.id}>
                  <td>{new Date(scan.created_at).toLocaleString()}</td>
                  <td>{scan.target}</td>
                  <td>{scan.automation_mode}</td>
                  <td className={`status ${scan.status}`}>{scan.status}</td>
                  <td>{scan.summary}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </section>
  )
}

export default Dashboard

