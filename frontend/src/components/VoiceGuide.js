import React from 'react';

function VoiceGuide({ text }) {
  const speakAloud = () => {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'hi-IN';
      utterance.rate = 0.9;
      window.speechSynthesis.speak(utterance);
    } else {
      alert('आपका ब्राउज़र वॉइस सपोर्ट नहीं करता है।');
    }
  };

  return (
    <button 
      onClick={speakAloud}
      style={{
        background: 'none',
        border: '4px solid #ffd700',
        borderRadius: '50%',
        width: '80px',
        height: '80px',
        fontSize: '40px',
        cursor: 'pointer',
        color: '#ffd700',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        margin: '0 auto',
        boxShadow: '0 4px 8px rgba(0,0,0,0.3)'
      }}
      title="सुनें (Listen)"
    >
      🔊
    </button>
  );
}

export default VoiceGuide;