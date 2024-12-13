import apiClient from './apiClient';
import { apiClientWithAuth } from './apiClient';

export const loginUser = async (credentials) => {
    try {
        const response = await apiClientWithAuth().post('login/', credentials);
        const token = response.data.token;

        localStorage.setItem('jwt', token);

        return response.data;
    } catch (error) {
        console.error('Error logging in:', error);
        throw error;
    }
};

export const logoutUser = async () => {
    try {
        const response = await apiClient.post('logout/');
        return response.data;
    } catch (error) {
        console.error('Error logging out:', error);
        throw error;
    }
};

export const registerUser = async (userData) => {
    try {
        const response = await apiClient.post('register/', userData);
        return response.data;  // Devuelve la respuesta con el mensaje y los datos del usuario registrado
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
};

export const getHomeMessage = async () => {
    try {
        const response = await apiClient.get('/api/home/'); // URL de tu API de Home
        return response.data;
    } catch (error) {
        console.error('Error fetching home message:', error);
        throw error;
    }
};
