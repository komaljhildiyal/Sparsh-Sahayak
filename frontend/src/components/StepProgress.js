import React from 'react';

function StepProgress({ currentStatus }) {
  const steps = [
    { key: 'pending', label: '1. Received' },
    { key: 'processing', label: '2. Creating Video' },
    { key: 'completed', label: '3. Ready to Watch!' },
    { key: 'failed', label: '❌ Failed' }
  ];

  const getStepColor = (stepKey) => {
    if (currentStatus === 'failed' && stepKey === 'failed') return '#dc3545';
    if (stepKey === currentStatus) return '#ffd700';
    if (steps.findIndex(s => s.key === currentStatus) > steps.findIndex(s => s.key === stepKey)) return '#28a745';
    return '#555555';
  };

  return (
    <div style={{ margin: '40px 0' }}>
      <div style={{ display: 'flex', justifyContent: 'space-around', flexWrap: 'wrap', gap: '20px' }}>
        {steps.filter(s => s.key !== 'failed').map((step) => (
          <div 
            key={step.key} 
            style={{
              padding: '20px',
              borderRadius: '10px',
              background: '#1a3a5c',
              border: `4px solid ${getStepColor(step.key)}`,
              flex: '1',
              minWidth: '200px'
            }}
          >
            <div style={{ fontSize: '28px', fontWeight: 'bold', color: getStepColor(step.key) }}>
              {step.label}
            </div>
          </div>
        ))}
      </div>
      {currentStatus === 'processing' && (
        <p className="text-accent mt-4 text-large">⏳ Please wait, AI is generating the video...</p>
      )}
    </div>
  );
}

export default StepProgress;