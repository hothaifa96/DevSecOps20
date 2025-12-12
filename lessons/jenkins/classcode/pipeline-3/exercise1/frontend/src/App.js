import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [health, setHealth] = useState(null);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

  useEffect(() => {
    fetchHealth();
    fetchData();
  }, []);

  const fetchHealth = async () => {
    try {
      const response = await fetch(`${API_URL}/api/health`);
      const result = await response.json();
      setHealth(result);
    } catch (err) {
      setError("Failed to connect to backend");
    }
  };

  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_URL}/api/data`);
      const result = await response.json();
      setData(result.items);
    } catch (err) {
      setError("Failed to fetch data");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className='App'>
      <div className='container'>
        <h1>🚀 Simple Web App</h1>

        {health && (
          <div className='health-card'>
            <h2>Backend Status</h2>
            <p className='status'>{health.status}</p>
            <p>{health.message}</p>
            <p className='environment'>Environment: {health.environment}</p>
          </div>
        )}

        {error && <div className='error'>{error}</div>}

        <div className='data-section'>
          <h2>Data from Backend</h2>
          {loading ? (
            <p>Loading...</p>
          ) : (
            <div className='items-grid'>
              {data.map((item) => (
                <div key={item.id} className='item-card'>
                  <h3>{item.name}</h3>
                  <p>{item.description}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
