import apiClient from './apiClient';

/**
 * Inicia sesión de un usuario con sus credenciales.
 *
 * @param {Object} credentials - Las credenciales del usuario (usualmente un objeto con 'email' y 'password').
 * @returns {Object} Los datos de la respuesta del servidor (por ejemplo, información del usuario).
 * @throws {Error} Si ocurre un error durante el proceso de login, el error se lanza para ser manejado por el componente o flujo que invoque esta función.
 */
export const loginUser = async (credentials) => {
    try {
        const response = await apiClient.post('users/login/', credentials);

        if (response.status === 200) {
            // Guardar el token JWT en localStorage
            localStorage.setItem('authToken', response.data.access_token);

            // Devolver los datos de la respuesta, incluyendo el mensaje de éxito y los datos del usuario
            return response.data;
        }
    } catch (error) {
        console.error('Error logging in:', error);
        throw error;
    }
};


/**
 * Cierra sesión del usuario actual.
 *
 * @returns {Object} Los datos de la respuesta del servidor (por ejemplo, un mensaje de confirmación).
 * @throws {Error} Si ocurre un error durante el proceso de logout, el error se lanza para ser manejado por el componente o flujo que invoque esta función.
 */
export const logoutUser = async () => {
    try {
        // Hacer la petición de cierre de sesión en el backend
        const response = await apiClient.post('users/logout/');

        // Eliminar el token del almacenamiento local o de sesión
        localStorage.removeItem('access_token');
        sessionStorage.removeItem('access_token');

        return response.data;
    } catch (error) {
        console.error('Error logging out:', error);
        throw error;
    }
};

/**
 * Registra un nuevo usuario con los datos proporcionados.
 *
 * @param {Object} userData - Los datos del usuario a registrar (nombre, correo electrónico, contraseña, etc.).
 * @returns {Object} Los datos de la respuesta del servidor (por ejemplo, un mensaje de éxito o los detalles del nuevo usuario).
 * @throws {Error} Si ocurre un error durante el proceso de registro, el error se lanza para ser manejado por el componente o flujo que invoque esta función.
 */
export const registerUser = async (userData) => {
    try {
        const response = await apiClient.post('users/register/', userData);

        const { access_token } = response.data;
        localStorage.setItem('access_token', access_token);
        sessionStorage.setItem('access_token', access_token);

        return response.data;
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
};


/**
 * Obtiene el mensaje de bienvenida o mensaje principal para el usuario.
 *
 * @returns {Object} Los datos de la respuesta del servidor (por ejemplo, un mensaje personalizado de bienvenida).
 * @throws {Error} Si ocurre un error durante la solicitud, el error se lanza para ser manejado por el componente o flujo que invoque esta función.
 */
export const getHomeMessage = async () => {
    try {
        const response = await apiClient.get('users/home/');
        return response.data;
    } catch (error) {
        console.error('Error fetching home message:', error);
        throw error;
    }
};

