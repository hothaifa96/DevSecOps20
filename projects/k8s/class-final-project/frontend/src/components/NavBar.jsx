import { NavLink } from 'react-router-dom'

const routes = [
  { to: '/', label: 'Automation Lab' },
  { to: '/env', label: 'Backend Env' },
]

function NavBar() {
  return (
    <header className="navbar">
      <div className="brand">
        <span>AutoScan</span>
        <small>tiny automation lab</small>
      </div>
      <nav>
        {routes.map(({ to, label }) => (
          <NavLink key={to} to={to} className={({ isActive }) => (isActive ? 'active' : '')}>
            {label}
          </NavLink>
        ))}
      </nav>
    </header>
  )
}

export default NavBar

