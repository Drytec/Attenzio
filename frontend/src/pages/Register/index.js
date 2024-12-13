import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const Register = () => {
  return (
    <div className="register-container">
      <h2>Registrarse</h2>
      <p>Selecciona tu rol para continuar:</p>
      <div className="button-container">
        <Link to="/register/studentRegister" className="role-button">Estudiante</Link>
        <Link to="/register/teacherRegister" className="role-button">Profesor</Link>
      </div>
    </div>
  );
};

export default Register;
