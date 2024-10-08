import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const ScorecardPage = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleButtonClick = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.get('http://127.0.0.1:5000/run-scorecard');
      const data = response.data;
      console.log(data);
      navigate('/result', { state: { scorecard: data } });
    } catch (err) {
      setError('An error occurred while fetching the scorecard.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <button onClick={handleButtonClick} disabled={loading}>
        {loading ? 'Loading...' : 'Run Scorecard Analysis'}
      </button>
      {error && <p>{error}</p>}
    </div>
  );
};

export default ScorecardPage;
