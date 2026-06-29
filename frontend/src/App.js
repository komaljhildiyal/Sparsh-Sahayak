import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import TopicSelect from './pages/TopicSelect';
import VideoPlayer from './pages/VideoPlayer';
import './styles/senior.css';

function App() {
  return (
    <Router>
      <div style={{ minHeight: '100vh', padding: '20px' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/select" element={<TopicSelect />} />
          <Route path="/video/:id" element={<VideoPlayer />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;