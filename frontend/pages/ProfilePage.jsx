import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../src/AuthContext';

export default function ProfilePage() {
  const { userId } = useContext(AuthContext);
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    if (!userId) return;
    fetch(`/api/profile/${userId}`)
      .then((res) => res.json())
      .then((data) => setProfile(data));
  }, [userId]);

  if (!userId) {
    return <p>Please log in to view your profile.</p>;
  }

  return (
    <div>
      <h1 className="text-xl font-bold mb-4">Your Profile</h1>
      {profile ? (
        <ul className="list-disc ml-4">
          <li>IQ: {profile.iq}</li>
          <li>EQ: {profile.eq}</li>
          <li>AQ: {profile.aq}</li>
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
