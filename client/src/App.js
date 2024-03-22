import React, { useState, useEffect } from 'react';
import './App.css';
import { Bar } from 'react-chartjs-2';

function App() {
  const [boroughData, setBoroughData] = useState([]);
  const [postcodeData, setPostcodeData] = useState([]);

  useEffect(() => {
    fetchBoroughData();
    fetchPostcodeData();
  }, []);

  const fetchBoroughData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/borough');
      if (!response.ok) {
        throw new Error('Failed to fetch borough data');
      }
      const data = await response.json();
      setBoroughData(data);
    } catch (error) {
      console.error('Error fetching borough data:', error);
    }
  };

  const fetchPostcodeData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5555/postcode');
      if (!response.ok) {
        throw new Error('Failed to fetch postcode data');
      }
      const data = await response.json();
      setPostcodeData(data);
    } catch (error) {
      console.error('Error fetching postcode data:', error);
    }
  };

  const colors = ['#55DA97', '#F5A623', '#4A90E2', '#DB4DF7', '#FF1418'];
  const legendLabelColor = '#a9a9a9';

  return (
    <div className="App">
      <header className="App-header">
        <div style={{ height: '400px', width: '600px', marginBottom: '20px' }}>
          <Bar
            data={{
              labels: boroughData.map(entry => entry.borough),
              datasets: [{
                label: 'Total Units',
                data: boroughData.map(entry => entry.total_units),
                backgroundColor: colors, 
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
              }]
            }}
            options={{
              scales: {
                y: {
                  beginAtZero: true
                }
              },
              plugins: {
                legend: {
                  labels: {
                    color: legendLabelColor,
                    generateLabels: function(chart) {
                      return [{
                        text: 'Total Units By Borough',
                        fillStyle: legendLabelColor,
                        strokeStyle: 'transparent',
                        lineWidth: 0
                      }];
                    }
                  },
                  display: true
                }
              }
            }}
          />
        </div>
        <div style={{ height: '400px', width: '1200px' }}>
          <Bar
            data={{
              labels: postcodeData.map(entry => entry.postcode),
              datasets: [{
                label: 'Total Units',
                data: postcodeData.map(entry => entry.total_units),
                backgroundColor: colors, 
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
              }]
            }}
            options={{
              scales: {
                y: {
                  beginAtZero: true
                }
              },
              plugins: {
                legend: {
                  labels: {
                    color: legendLabelColor,
                    generateLabels: function(chart) {
                      return [{
                        text: 'Total Units By Postcode',
                        fillStyle: legendLabelColor,
                        strokeStyle: 'transparent',
                        lineWidth: 0
                      }];
                    }
                  },
                  display: true
                }
              }
            }}
          />
        </div>
      </header>
    </div>
  );
}

export default App;