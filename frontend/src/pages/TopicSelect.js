import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import BigButton from '../components/BigButton';
import VoiceGuide from '../components/VoiceGuide';

function TopicSelect() {
  const [topic, setTopic] = useState('SPARSH Life Certificate');
  const [text, setText] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async () => {

    if (!text.trim() && !selectedFile) {

        alert(
        'Enter text or upload PDF'
        );

        return;
    }

    setLoading(true);

    try {

        const formData=new FormData();

        formData.append(
            "topic",
            topic
        );

        formData.append(
            "text",
            text
        );

        if(selectedFile){

            formData.append(
                "file",
                selectedFile
            );

        }

        const response=
        await axios.post(
        "http://localhost:8001/api/tutorials",
        formData,
        {
            headers:{
                "Content-Type":
                "multipart/form-data"
            }
        }
        );

        navigate(
        `/video/${response.data.tutorial_id}`
        );

    }

    catch(error){

        console.log(error);

        alert(
        "Error generating tutorial"
        );

        setLoading(false);

    }

}

  return (
    <div className="card">
      <h1 className="text-large">📝 प्रक्रिया डालें (Enter Procedure)</h1>
      
      <div className="mt-2">
        <VoiceGuide text="नीचे दिए गए बॉक्स में स्पर्श प्रक्रिया का टेक्स्ट पेस्ट करें और वीडियो बनाएं बटन दबाएं।" />
      </div>

      <div className="mt-4" style={{ textAlign: 'left' }}>
        <label style={{ fontSize: '24px', marginBottom: '10px', display: 'block' }}>Topic / विषय:</label>
        <input 
          type="text" 
          value={topic} 
          onChange={(e) => setTopic(e.target.value)}
          style={{ width: '100%', padding: '15px', fontSize: '24px', borderRadius: '10px', border: 'none' }}
        />

        <label style={{ fontSize: '24px', marginTop: '20px', display: 'block' }}>Procedure Text / प्रक्रिया टेक्स्ट:</label>
        <textarea 
          value={text} 
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste SPARSH text here..."
          rows={6}
          style={{ width: '100%', padding: '15px', fontSize: '22px', borderRadius: '10px', border: 'none', marginTop: '10px' }}
        />
          <label
  style={{
  fontSize:'24px',
  marginTop:'20px',
  display:'block'
  }}
  >

  Upload PDF:

  </label>

  <input
  type="file"
  accept=".pdf"
  onChange={(e)=>
  setSelectedFile(
  e.target.files[0]
  )
  }
  style={{
  marginTop:'10px',
  fontSize:'20px'
  }}
  />
      </div>

      <div className="mt-4">
        <BigButton onClick={handleSubmit} disabled={loading} color="success">
          {loading ? '⏳ भेज रहा है... (Sending)' : '🎬 वीडियो बनाएं (Create Video)'}
        </BigButton>
      </div>
    </div>
  );
}

export default TopicSelect;