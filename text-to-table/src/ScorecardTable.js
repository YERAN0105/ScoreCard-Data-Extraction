import React from 'react';
import { useLocation } from 'react-router-dom';

const ScorecardTable = () => {
  const location = useLocation();
  const { scorecard } = location.state;

  return (
    <div>
      <h1>Scorecard Data</h1>
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
          {scorecard.map((player, index) => (
            <tr key={index}>
              <td>{player.name}</td>
              <td>{player.fours}</td>
              <td>{player.sixes}</td>
              <td>{player.balls_faced}</td>
              <td>{player.total_runs}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ScorecardTable;
