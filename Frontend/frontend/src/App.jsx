import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import FishPredictor from './FishPredictor';
import Navbar from './Navbar';

function App() {
  return (
    <Router>
      <Navbar /> {/* Add Navbar here */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/predict" element={<FishPredictor />} />
      </Routes>
    </Router>
  );
}

export default App;
