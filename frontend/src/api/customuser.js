import apiClient from './apiClient';

export const loginUser = async (credentials) => {

    try {
        const response = await apiClient.post('users/login/', credentials);
        return response.data;
    } catch (error) {
        console.error('Error logging in:', error);
        throw error;
    }
};

export const logoutUser = async () => {
    try {
        const response = await apiClient.post('users/logout/');
        return response.data;
    } catch (error) {
        console.error('Error logging out:', error);
        throw error;
    }
};

export const registerUser = async (userData) => {
    try {
        const response = await apiClient.post('users/register/', userData);
        return response.data;  // Devuelve la respuesta con el mensaje y los datos del usuario registrado
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
};

export const getHomeMessage = async () => {
    try {
        const response = await apiClient.get('users/home/'); // URL de tu API de Home
        return response.data;
    } catch (error) {
        console.error('Error fetching home message:', error);
        throw error;
    }
};
