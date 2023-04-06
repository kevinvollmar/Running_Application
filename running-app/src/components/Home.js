import React, { useEffect } from 'react';
import axios from 'axios';

console.log("Making API request")
function Home() {
  useEffect(() => {
    axios.get('http://localhost:5000/api/data')
      .then(response => console.log(response.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Home Component</h1>
    </div>
  );
}

export default Home;
