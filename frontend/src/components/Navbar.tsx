import React, { useContext } from 'react';
import { AppBar, Toolbar, Typography, IconButton, Avatar } from '@mui/material';
import LogoutIcon from '@mui/icons-material/Logout';
import { AuthContext } from '../context/AuthContext';
import './Navbar.css';

const Navbar: React.FC = () => {
  const { user, logout } = useContext(AuthContext);

  return (
    <AppBar position="static" className="navbar">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Programming Practices Platform
        </Typography>
        {user && (
          <>
            <IconButton color="inherit" onClick={logout} aria-label="logout" data-testid="logout-button">
              <LogoutIcon />
            </IconButton>
            <Avatar alt={user.email} src={user.avatarUrl} className="navbar-avatar" />
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
