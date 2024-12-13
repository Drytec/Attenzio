import React from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const SelectTypeUser = () => {
    return (
        <div className="register-container">
            <h2>Registrarse</h2>
            <p>Selecciona tu rol para continuar:</p>
            <div className="button-container">
                <Link to="/users/student_register" className="role-button">Estudiante</Link>
                <Link to="/users/teacher_register" className="role-button">Profesor</Link>
            </div>
        </div>
    );
};

export default SelectTypeUser;
