import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from '../pages/HomePage';
import RegisterPage from '../pages/RegisterPage';
import LoginPage from '../pages/LoginPage';
import DashboardPage from '../pages/DashboardPage';
import TestPage from '../pages/TestPage';
import ChatPage from '../pages/ChatPage';
import AudioPage from '../pages/AudioPage';
import ForumPage from '../pages/ForumPage';
import ProfilePage from '../pages/ProfilePage';
import '../index.css';

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/register" element={<RegisterPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route path="/test" element={<TestPage />} />
      <Route path="/chat" element={<ChatPage />} />
      <Route path="/audio" element={<AudioPage />} />
      <Route path="/forum" element={<ForumPage />} />
      <Route path="/profile" element={<ProfilePage />} />
    </Routes>
  </Router>
);

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
