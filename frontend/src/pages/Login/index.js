import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const Login = () => {
  return (
    <div className="login-container">
      <form className="login-form">
        <label htmlFor="email">Email address</label>
        <input type="email" id="email" placeholder="Email address" />

        <label htmlFor="password">Password</label>
        <input type="password" id="password" placeholder="Password" />

        <Link to="/dashboard" className="login-button">Iniciar sesión</Link>
      </form>
    </div>
  );
};

export default Login;
