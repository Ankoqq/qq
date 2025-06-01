import React from 'react';
import { Link } from 'react-router-dom';

export default function Layout({ children }) {
  return (
    <div>
      <nav className="p-4 bg-gray-200 flex space-x-4">
        <Link to="/">Home</Link>
        <Link to="/register">Register</Link>
        <Link to="/login">Login</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/test">Test</Link>
        <Link to="/chat">Chat</Link>
        <Link to="/audio">Audio</Link>
        <Link to="/forum">Forum</Link>
        <Link to="/profile">Profile</Link>
      </nav>
      <main className="p-4">{children}</main>
    </div>
  );
}
