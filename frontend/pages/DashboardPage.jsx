import React, { useContext } from 'react';
import { AuthContext } from '../src/AuthContext';

export default function DashboardPage() {
  const { userId } = useContext(AuthContext);
  return (
    <div>
      <h1 className="text-xl font-bold mb-4">Dashboard</h1>
      {userId ? <p>Welcome user #{userId}</p> : <p>Please log in.</p>}
    </div>
  );
}
