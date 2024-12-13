import React, { useState } from "react";
import { registerUser } from '../../api/customuser';

const StudentRegister = () => {
  const [formData, setFormData] = useState({
    full_name: "",
    document: "",
    address: "",
    email: "",
    phone: "",
    password: "",
    media: null, 
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFileChange = (e) => {
    setFormData({ ...formData, media: e.target.files[0] });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formDataToSend = new FormData();
    Object.keys(formData).forEach((key) => {
      formDataToSend.append(key, formData[key]);
    });

    try {
      const response = await registerUser(formDataToSend); // Llamada al método de la API
      alert("Registro exitoso: " + JSON.stringify(response));
    } catch (error) {
      console.error("Error al registrar:", error.response?.data || error.message);
      alert("Error al registrar: " + JSON.stringify(error.response?.data || error.message));
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", width: "300px", margin: "auto" }}>
      <h2>Estudiante</h2>
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
        placeholder="Documento"
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
      <label>Subir imagen:</label>
      <input type="file" name="media" onChange={handleFileChange} />
      <button type="submit" style={{ backgroundColor: "orange", color: "white", marginTop: "10px" }}>
        Registrarse
      </button>
    </form>
  );
};

export default StudentRegister;
