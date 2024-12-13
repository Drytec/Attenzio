import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.REACT_APP_API_URL, // Utiliza la URL base definida en el archivo .env
    headers: {
        'Content-Type': 'application/json',
    },
});

export default apiClient;
