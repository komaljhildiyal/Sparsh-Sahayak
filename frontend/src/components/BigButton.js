import React from 'react';

function BigButton({ onClick, children, color = 'primary', disabled = false }) {
  const styles = {
    padding: '30px 60px',
    fontSize: '36px',
    fontWeight: 'bold',
    border: 'none',
    borderRadius: '15px',
    cursor: disabled ? 'not-allowed' : 'pointer',
    width: '100%',
    maxWidth: '600px',
    transition: 'all 0.2s ease',
    opacity: disabled ? 0.6 : 1,
    backgroundColor: color === 'primary' ? '#ff6b00' : color === 'success' ? '#28a745' : '#1a3a5c',
    color: 'white',
    boxShadow: '0 6px 12px rgba(0,0,0,0.4)',
  };

  return (
    <button 
      style={styles} 
      onClick={onClick} 
      disabled={disabled}
      onMouseOver={(e) => !disabled && (e.target.style.transform = 'scale(1.05)')}
      onMouseOut={(e) => (e.target.style.transform = 'scale(1)')}
    >
      {children}
    </button>
  );
}

export default BigButton;