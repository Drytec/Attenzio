import axios from 'axios';

const apiClient = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const apiClientWithAuth = () => {
    const token = localStorage.getItem('jwt');  // Obtén el token del localStorage

    if (token) {
        // Si existe un token, agrégalo al encabezado de las solicitudes
        apiClient.defaults.headers['Authorization'] = `Bearer ${token}`;
    } else {
        // Si no hay token, puedes hacer algo, por ejemplo, redirigir a login
    }

    return apiClient;
};
export default apiClient;