import React from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';

const Sidebar: React.FC = () => {
  const links = [
    { to: '/', label: 'Dashboard' },
    { to: '/problems', label: 'Problems' },
    { to: '/editor', label: 'Editor' },
    { to: '/profile', label: 'Profile' },
  ];

  return (
    <aside className="sidebar">
      <nav>
        <ul>
          {links.map((link) => (
            <li key={link.to}>
              <NavLink to={link.to} className={({ isActive }) => isActive ? 'active' : ''}>
                {link.label}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
