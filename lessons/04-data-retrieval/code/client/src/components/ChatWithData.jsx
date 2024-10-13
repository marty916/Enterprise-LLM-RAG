// client/src/components/ChatWithData.jsx
import React, { useState } from 'react';
import { sendChatWithDataMessage } from '../services/api';
import { Scatter } from 'react-chartjs-2';
import {
  Chart,
  ScatterController,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from 'chart.js';
import './ChatWithData.css'

// Register necessary Chart.js components
Chart.register(ScatterController, LinearScale, PointElement, Tooltip, Legend);

const ChatWithData = () => {
  const [embeddings, setEmbeddings] = useState([]);
  const [metadata, setMetadata] = useState([]);
  const [error, setError] = useState(null);

  const handleIngestAndVisualize = async () => {
    try {
      const response = await sendChatWithDataMessage();
      setEmbeddings(response.embeddings);
      setMetadata(response.metadata);
    } catch (err) {
      setError('Failed to load embeddings');
      console.error(err);
    }
  };

  const chartData = {
    datasets: [
      {
        label: 'Embeddings',
        data: embeddings.map((coord, idx) => ({
          x: coord[0],
          y: coord[1],
          label: metadata[idx]?.title || `Doc ${idx + 1}`,
        })),
        backgroundColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  const options = {
    plugins: {
      tooltip: {
        callbacks: {
          label: function (context) {
            const label = context.raw.label || '';
            return ` ${label}`;
          },
        },
      },
      legend: {
        display: false,
      },
    },
    scales: {
      x: {
        type: 'linear',
        position: 'bottom',
        title: {
          display: true,
          text: 'Component 1',
        },
      },
      y: {
        title: {
          display: true,
          text: 'Component 2',
        },
      },
    },
  };

  return (
    <div className="chat-with-data">
      <button onClick={handleIngestAndVisualize}>Ingest and Visualize Data</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {embeddings.length > 0 && (
        <div className="chart-container" style={{ width: '600px', height: '400px' }}>
          <Scatter data={chartData} options={options} />
        </div>
      )}
    </div>
  );
};

export default ChatWithData;
