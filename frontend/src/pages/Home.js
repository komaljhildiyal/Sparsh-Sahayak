import React from 'react';
import { useNavigate } from 'react-router-dom';
import BigButton from '../components/BigButton';
import VoiceGuide from '../components/VoiceGuide';

function Home() {
  const navigate = useNavigate();
  const welcomeMessage = "स्वागत है! स्पर्श लाइफ सर्टिफिकेट ट्यूटोरियल सिस्टम में। आगे बढ़ने के लिए बटन दबाएं।";

  return (
    <div className="card">
      <h1 className="text-xlarge">🇮🇳 SPARSH Tutorial</h1>
      <p className="text-large mt-2">Life Certificate Made Easy</p>
      <p className="mt-2" style={{ fontSize: '28px' }}>(स्पर्श पोर्टल गाइड)</p>

      <div className="mt-4">
        <VoiceGuide text={welcomeMessage} />
        <p style={{ marginTop: '10px', fontSize: '20px' }}>सुनने के लिए दबाएं 🔊</p>
      </div>

      <div className="mt-4">
        <BigButton onClick={() => navigate('/select')} color="primary">शुरू करें (Start)</BigButton>
      </div>
    </div>
  );
}

export default Home;