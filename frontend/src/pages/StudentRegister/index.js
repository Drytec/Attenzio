import React, { useState } from "react";
import { registerUser } from '../../api/customuser';
import {useNavigate} from "react-router-dom";

const StudentRegister = () => {
    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        full_name: "",
        document: "",
        address: "",
        email: "",
        phone: "",
        password: "",
        media: null,
        user_type: "student",
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formDataToSend = new FormData();
        Object.keys(formData).forEach((key) => {
            formDataToSend.append(key, formData[key]);
        });

        try {
            const response = await registerUser(formDataToSend);
            alert("Registro exitoso: " + JSON.stringify(response));
            navigate("/");
        } catch (error) {
            console.error("Error al registrar:", error.response?.data || error.message);
            alert("Error al registrar: " + JSON.stringify(error.response?.data || error.message));
        }
    };

    return (
        <form onSubmit={handleSubmit}
              style={{display: "flex", flexDirection: "column", width: "300px", margin: "auto"}}>
            <h2>Profesor</h2>
            <input
                type="text"
                name="full_name"
                placeholder="Nombre completo"
                value={formData.full_name}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="document"
                placeholder="Código de estudiante"
                value={formData.document}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="address"
                placeholder="Dirección"
                value={formData.address}
                onChange={handleChange}
            />
            <input
                type="email"
                name="email"
                placeholder="Correo electrónico"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="phone"
                placeholder="Teléfono"
                value={formData.phone}
                onChange={handleChange}
            />
            <input
                type="password"
                name="password"
                placeholder="Contraseña"
                value={formData.password}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="media"
                placeholder="URL del tabulado"
                value={formData.media}
                onChange={handleChange}
            />
            <button type="submit" style={{backgroundColor: "orange", color: "white", marginTop: "10px"}}>
                Registrarse
            </button>
        </form>
    );
};

export default StudentRegister;


