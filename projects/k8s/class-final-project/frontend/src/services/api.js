const API_BASE_URL = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:5000'

async function request(endpoint, options = {}) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  })

  if (!response.ok) {
    const message = await response.text()
    throw new Error(message || `Request failed with ${response.status}`)
  }

  return response.json()
}

export async function getScans() {
  const payload = await request('/api/scans')
  return payload.items ?? []
}

export async function runScan(data) {
  return request('/api/scans', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function getEnvironmentSnapshot() {
  return request('/api/env')
}

