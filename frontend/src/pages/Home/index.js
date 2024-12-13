import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './styles.css';

const Home = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('access_token') || sessionStorage.getItem('access_token');
        if (token) {
            setIsLoggedIn(true);
        }
    }, []);

    return (
        <div className="landing-container">
            <p>Bienvenido, elige una opción para continuar</p>
            <div className="button-container">
                <Link to="users/login" className="button-link">Iniciar Sesión</Link>

                {!isLoggedIn && (
                    <Link to="select_type_user" className="button-link">Registrarse</Link>
                )}
            </div>
        </div>
    );
};

export default Home;

