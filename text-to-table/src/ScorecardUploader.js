import React, { useState } from 'react';
import axios from 'axios';

function ScorecardUploader() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please upload a file");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setLoading(true);
      const response = await axios.post('http://127.0.0.1:5000/run-scorecard', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setData(response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Upload Scorecard Image</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Analyze</button>

      {loading && <p>Processing...</p>}

      {data.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>4s</th>
              <th>6s</th>
              <th>Balls Faced</th>
              <th>Total Runs</th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                <td>{row.name}</td>
                <td>{row.fours}</td>
                <td>{row.sixes}</td>
                <td>{row.balls_faced}</td>
                <td>{row.total_runs}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ScorecardUploader;
