import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const Home = () => {
  return (
    <div className="landing-container">
      <p>Bienvenido, elige una opción para continuar</p>
      <div className="button-container">
        <Link to="users/login" className="button-link">Iniciar Sesión</Link>
        <Link to="select_type_user" className="button-link">Registrarse</Link>
      </div>
    </div>
  );
};

export default Home;
