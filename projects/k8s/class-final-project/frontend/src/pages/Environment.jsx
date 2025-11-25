import { useEffect, useState } from 'react'
import { getEnvironmentSnapshot } from '../services/api.js'

function Environment() {
  const [snapshot, setSnapshot] = useState(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const run = async () => {
      setLoading(true)
      try {
        const data = await getEnvironmentSnapshot()
        setSnapshot(data)
        setError('')
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }
    run()
  }, [])

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <h1>Backend environment</h1>
          <p>Lightweight view of what the Flask automation worker exposes.</p>
        </div>
      </div>

      {loading && <p>Loading environment snapshot…</p>}
      {error && <p className="error">{error}</p>}

      {snapshot && (
        <div className="env-grid">
          <article>
            <h2>Runtime</h2>
            <dl>
              <dt>Python version</dt>
              <dd>{snapshot.python_version}</dd>
              <dt>Working dir</dt>
              <dd>{snapshot.working_directory}</dd>
              <dt>SQLite DB</dt>
              <dd>{snapshot.database_path}</dd>
            </dl>
          </article>
          <article>
            <h2>Exposed ENV keys</h2>
            {Object.keys(snapshot.exposed_env || {}).length === 0 ? (
              <p>No custom vars provided. Set AUTOSCAN_* vars to see them here.</p>
            ) : (
              <dl>
                {Object.entries(snapshot.exposed_env).map(([key, value]) => (
                  <div key={key}>
                    <dt>{key}</dt>
                    <dd>{value}</dd>
                  </div>
                ))}
              </dl>
            )}
          </article>
        </div>
      )}
    </section>
  )
}

export default Environment

