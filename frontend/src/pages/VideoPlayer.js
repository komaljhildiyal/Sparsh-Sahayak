import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import StepProgress from '../components/StepProgress';
import BigButton from '../components/BigButton';

function VideoPlayer() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [status, setStatus] = useState('pending');
  const [videoUrl, setVideoUrl] = useState('');

  useEffect(() => {
    const pollInterval = setInterval(async () => {
      try {
        const response = await axios.get(`http://localhost:8001/api/tutorials/${id}`);
        const tutorialData = response.data;
        
        setStatus(tutorialData.status);

        if (tutorialData.status === 'completed') {
          setVideoUrl(`http://localhost:8001/api/tutorials/${id}/video`);
          clearInterval(pollInterval);
        } else if (tutorialData.status === 'failed') {
          clearInterval(pollInterval);
        }
      } catch (error) {
        console.error("Polling error:", error);
      }
    }, 4000);

    return () => clearInterval(pollInterval);
  }, [id]);

  return (
    <div className="card">
      <h1 className="text-large">🎬 वीडियो ट्यूटोरियल</h1>
      
      <StepProgress currentStatus={status} />

      {status === 'completed' && (
        <div className="mt-4" style={{ width: '100%' }}>
          <video 
            controls 
            autoPlay 
            style={{ width: '100%', borderRadius: '15px', boxShadow: '0 10px 30px rgba(0,0,0,0.5)' }}
            src={videoUrl}
          >
            आपका ब्राउज़र वीडियो सपोर्ट नहीं करता।
          </video>
        </div>
      )}

      {status === 'failed' && (
        <div className="mt-4">
          <p style={{ color: '#dc3545', fontSize: '28px' }}>❌ वीडियो बनाने में समस्या हुई।</p>
          <p>(Error generating video. Check backend terminal logs).</p>
        </div>
      )}

      <div className="mt-4">
        <BigButton onClick={() => navigate('/select')} color="primary">🔙 वापस जाएं (Go Back)</BigButton>
      </div>
    </div>
  );
}

export default VideoPlayer;