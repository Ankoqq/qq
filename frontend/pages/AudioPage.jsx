import React from 'react';

export default function AudioPage() {
  return (
    <div>
      <h1 className="text-xl font-bold mb-4">Audio Anchors</h1>
      <audio controls src="/sample.mp3" className="w-full">
        Your browser does not support the audio element.
      </audio>
    </div>
  );
}
