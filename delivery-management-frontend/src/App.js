import React from 'react';
import './styles.css'; 
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ComponentForm from './components/ComponentForm';
import VehicleForm from './components/VehicleForm';
import IssueForm from './components/IssueForm';
import RevenueGraphs from './components/RevenueGraphs';

function App() {
  return (
    <Router>
      <div className="container">
        <h1>Delivery Management System</h1>
        <Routes>
          <Route path="/components" element={<ComponentForm />} />
          <Route path="/vehicles" element={<VehicleForm />} />
          <Route path="/issues" element={<IssueForm />} />
          <Route path="/revenue" element={<RevenueGraphs />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
