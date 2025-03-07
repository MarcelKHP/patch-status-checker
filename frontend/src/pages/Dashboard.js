import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { CSVLink } from 'react-csv';

const Dashboard = () => {
  const [patchStatus, setPatchStatus] = useState([]);

  useEffect(() => {
    axios.get('/patch-status')
      .then(response => {
        setPatchStatus(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the patch status!', error);
      });
  }, []);

  return (
    <div>
      <h1>Patch Status Dashboard</h1>
      <CSVLink data={patchStatus} filename={"patch-status.csv"}>Export to CSV</CSVLink>
      <table>
        <thead>
          <tr>
            <th>Endpoint</th>
            <th>OS Type</th>
            <th>Last Checked</th>
            <th>Missing Updates</th>
          </tr>
        </thead>
        <tbody>
          {patchStatus.map(status => (
            <tr key={status.id}>
              <td>{status.endpoint}</td>
              <td>{status.os_type}</td>
              <td>{status.last_checked}</td>
              <td>{status.missing_updates}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;