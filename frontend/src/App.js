import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import AppRoutes from './routes';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1><span style={{ color: "red" }}>Attenzio</span>App</h1>
                <Router>
                    <AppRoutes />
                </Router>
            </header>
        </div>
    );
}

export default App;
