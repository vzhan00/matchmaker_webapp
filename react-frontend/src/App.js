import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [ranking, setRanking] = useState(0);

  // [] parameter only cause useEffect when ranking changes
  useEffect(() => {
    fetch('/rankings').then(res => res.json()).then(data => setRanking(data));
    console.log(ranking);
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {Object.keys(ranking).map(key => <p>{key}: { ranking[key] }</p>)}
        </div>
      </header>
    </div>
  );
}

export default App;
