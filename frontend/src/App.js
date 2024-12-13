import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import StudentRegister from './pages/StudentRegister';
import StudentCourses from './pages/StudentCourses';
import './App.css';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1><span style={{ color: "red" }}>Attenzio</span>App</h1>
                <Router>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                        <Route path="/studentRegister" element={<StudentRegister/>}></Route>
                        <Route path="/studentCourses" element={<StudentCourses/>}></Route>
                    </Routes>
                </Router>
            </header>
        </div>
    );
}

export default App;