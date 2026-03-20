import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    console.log('Fetching workouts from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched workouts:', results);
        setWorkouts(results);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 display-6 fw-semibold">Workouts</h2>
      <div className="card shadow">
        <div className="card-body">
          <table className="table table-striped table-bordered align-middle">
            <thead className="table-dark">
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">Description</th>
                <th scope="col">Duration</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((w) => (
                <tr key={w.id}>
                  <td>{w.id}</td>
                  <td>{w.name}</td>
                  <td>{w.description}</td>
                  <td>{w.duration}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Workouts;
