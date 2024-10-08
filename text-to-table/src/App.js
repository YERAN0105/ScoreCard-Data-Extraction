// import React, { useState } from 'react';
// import axios from 'axios';

// function App() {
//   const [batsmanFile, setBatsmanFile] = useState(null);
//   const [bowlerFile, setBowlerFile] = useState(null);
//   const [tableData, setTableData] = useState([]);  // Initialize as an empty array
//   const [isLoading, setIsLoading] = useState(false);  // New state for loading status

//   const handleBatsmanFileChange = (event) => {
//     setBatsmanFile(event.target.files[0]);
//   };

//   const handleBowlerFileChange = (event) => {
//     setBowlerFile(event.target.files[0]);
//   };

//   const handleSubmit = async (event) => {
//     event.preventDefault();
//     const formData = new FormData();
//     formData.append('batsman_file', batsmanFile);
//     formData.append('bowler_file', bowlerFile);

//     if(!batsmanFile || !bowlerFile){
//       alert("Please Upload both Images")
//       return
//     }

//     setIsLoading(true);  // Start loading

//     try {
//       const response = await axios.post('http://127.0.0.1:5000/run-scorecard', formData, {
//         headers: {
//           'Content-Type': 'multipart/form-data',
//         },
//       });
      
//       // Ensure that the response is an array
//       if (Array.isArray(response.data)) {
//         setTableData(response.data);
//       } else {
//         console.error('Expected an array in response but got:', response.data);
//         setTableData([]);  // Set an empty array if the response is not an array
//       }

//     } catch (error) {
//       console.error('Error uploading files:', error);
//       setTableData([]);  // Reset table data in case of error
//     } finally {
//       setIsLoading(false);  // Stop loading
//     }
//   };

//   return (
//     <div>
//       <h1>Scorecard Uploader</h1>
//       <form onSubmit={handleSubmit}>
//         <div>
//           <label>Batsman Image: </label>
//           <input type="file" onChange={handleBatsmanFileChange} />
//         </div>
//         <div>
//           <label>Bowler Image: </label>
//           <input type="file" onChange={handleBowlerFileChange} />
//         </div>
//         <button type="submit">Upload and Process</button>
//       </form>

//       {isLoading ? (
//         <p>Loading...</p> 
//       ) : (
//         <>
//           {tableData.length > 0 ? (
//             <table>
//               <thead>
//                 <tr>
//                   <th>Name</th>
//                   <th>Fours</th>
//                   <th>Sixes</th>
//                   <th>Balls Faced</th>
//                   <th>Total Runs</th>
//                   <th>Overs</th>
//                   <th>Runs</th>
//                   <th>Wickets</th>
//                 </tr>
//               </thead>
//               <tbody>
//                 {tableData.map((row, index) => (
//                   <tr key={index}>
//                     <td>{row.name}</td>
//                     <td>{row.fours}</td>
//                     <td>{row.sixes}</td>
//                     <td>{row.balls_faced}</td>
//                     <td>{row.total_runs}</td>
//                     <td>{row.overs}</td>
//                     <td>{row.runs}</td>
//                     <td>{row.wickets}</td>
//                   </tr>
//                 ))}
//               </tbody>
//             </table>
//           ) : (
//             <p>No data available</p>
//           )}
//         </>
//       )}
//     </div>
//   );
// }

// export default App;


import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [batsmanFile, setBatsmanFile] = useState(null);
  const [bowlerFile, setBowlerFile] = useState(null);
  const [tableData, setTableData] = useState([]);  // Initialize as an empty array
  const [isLoading, setIsLoading] = useState(false);  // New state for loading status

  const handleBatsmanFileChange = (event) => {
    setBatsmanFile(event.target.files[0]);
  };

  const handleBowlerFileChange = (event) => {
    setBowlerFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('batsman_file', batsmanFile);
    formData.append('bowler_file', bowlerFile);

    if(!batsmanFile || !bowlerFile){
      alert("Upload both ScoreCard Images")
      return
    }

    setIsLoading(true);  // Start loading

    try {
      const response = await axios.post('http://127.0.0.1:5000/run-scorecard', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      // Ensure that the response is an array
      if (Array.isArray(response.data)) {
        setTableData(response.data);
      } else {
        console.error('Expected an array in response but got:', response.data);
        setTableData([]);  // Set an empty array if the response is not an array
      }

    } catch (error) {
      console.error('Error uploading files:', error);
      setTableData([]);  // Reset table data in case of error
    } finally {
      setIsLoading(false);  // Stop loading
    }
  };

  // Handle change in input fields for editable table cells
  const handleInputChange = (event, rowIndex, field) => {
    const updatedTableData = [...tableData];
    updatedTableData[rowIndex][field] = event.target.value;
    setTableData(updatedTableData);
  };

  return (
    <div>
      <h1>Scorecard Uploader</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Batsman Image: </label>
          <input type="file" onChange={handleBatsmanFileChange} />
        </div>
        <div>
          <label>Bowler Image: </label>
          <input type="file" onChange={handleBowlerFileChange} />
        </div>
        <button type="submit">Upload and Process</button>
      </form>

      {isLoading ? (
        <p>Loading...</p> 
      ) : (
        <>
          {tableData.length > 0 ? (
            <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Fours</th>
                  <th>Sixes</th>
                  <th>Balls Faced</th>
                  <th>Total Runs</th>
                  <th>Overs</th>
                  <th>Runs</th>
                  <th>Wickets</th>
                </tr>
              </thead>
              <tbody>
                {tableData.map((row, index) => (
                  <tr key={index}>
                    <td>
                      <input
                        type="text"
                        value={row.name}
                        onChange={(event) => handleInputChange(event, index, 'name')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.fours}
                        onChange={(event) => handleInputChange(event, index, 'fours')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.sixes}
                        onChange={(event) => handleInputChange(event, index, 'sixes')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.balls_faced}
                        onChange={(event) => handleInputChange(event, index, 'balls_faced')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.total_runs}
                        onChange={(event) => handleInputChange(event, index, 'total_runs')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.overs}
                        onChange={(event) => handleInputChange(event, index, 'overs')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.runs}
                        onChange={(event) => handleInputChange(event, index, 'runs')}
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        value={row.wickets}
                        onChange={(event) => handleInputChange(event, index, 'wickets')}
                      />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No data available</p>
          )}
        </>
      )}
    </div>
  );
}

export default App;
