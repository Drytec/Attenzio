import apiClient from './apiClient';

/**
 * Obtiene los detalles de una sesión específica.
 *
 * @param {number} sessionId - El ID de la sesión a obtener.
 * @returns {Object} Los detalles de la sesión.
 */
export const getSession = async (sessionId) => {
    try {
        const response = await apiClient.get(`sessions/s:${sessionId}/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching session:', error);
        throw error;
    }
};

/**
 * Crea una nueva sesión asociada a un curso específico.
 *
 * @param {number} courseId - El ID del curso al que se asociará la sesión.
 * @param {Object} sessionData - Datos de la nueva sesión (nombre, descripción, fechas, etc.).
 * @returns {Object} Los detalles de la nueva sesión creada.
 */
export const createSession = async (courseId, sessionData) => {
    try {
        const response = await apiClient.post(`sessions/create_session/`, {
            ...sessionData,
            course_id: courseId
        });
        return response.data;
    } catch (error) {
        console.error('Error creating session:', error);
        throw error;  // Propaga el error.
    }
};

/**
 * Crea un material asociado a una sesión específica.
 *
 * @param {number} sessionId - El ID de la sesión donde se asociará el material.
 * @param {Object} materialData - Los datos del material (enlace o archivo).
 * @returns {Object} Los detalles del material creado.
 */
export const createMaterial = async (sessionId, materialData) => {
    try {
        const response = await apiClient.post(`sessions/s:${sessionId}/create_material`, materialData);
        return response.data;
    } catch (error) {
        console.error('Error creating material:', error);
        throw error;
    }
};

/**
 * Crea una nueva pregunta asociada a una sesión específica.
 *
 * @param {number} sessionId - El ID de la sesión donde se asociará la pregunta.
 * @param {Object} questionData - Los datos de la nueva pregunta (texto, tipo, etc.).
 * @returns {Object} Los detalles de la nueva pregunta creada.
 */
export const createQuestion = async (sessionId, questionData) => {
    try {
        const response = await apiClient.post(`sessions/s:${sessionId}/create_question`, questionData);
        return response.data;
    } catch (error) {
        console.error('Error creating question:', error);
        throw error;
    }
};

/**
 * Crea opciones de respuesta para una pregunta específica de una sesión.
 *
 * @param {number} sessionId - El ID de la sesión que contiene la pregunta.
 * @param {number} questionId - El ID de la pregunta a la que se asociarán las opciones.
 * @param {Array} optionsData - Un array de objetos que representan las opciones (texto y si son correctas o no).
 * @returns {Object} Los detalles de las opciones creadas.
 */
export const createOptions = async (sessionId, questionId, optionsData) => {
    try {
        const response = await apiClient.post(`sessions/s:${sessionId}/q:${questionId}/create_options`, {
            options: optionsData
        });
        return response.data;
    } catch (error) {
        console.error('Error creating options:', error);
        throw error;
    }
};

/**
 * Obtiene todas las preguntas asociadas a una sesión específica.
 *
 * @param {number} sessionId - El ID de la sesión para obtener sus preguntas.
 * @returns {Array} Un array con las preguntas de la sesión.
 */
export const getQuestions = async (sessionId) => {
    try {
        const response = await apiClient.get(`sessions/s:${sessionId}/show_questions`);
        return response.data;
    } catch (error) {
        console.error('Error fetching questions:', error);
        throw error;
    }
};

/**
 * Obtiene todas las opciones de respuesta asociadas a una pregunta específica.
 *
 * @param {number} sessionId - El ID de la sesión que contiene la pregunta.
 * @param {number} questionId - El ID de la pregunta para obtener sus opciones de respuesta.
 * @returns {Array} Un array con las opciones de la pregunta.
 */
export const getOptions = async (sessionId, questionId) => {
    try {
        const response = await apiClient.get(`sessions/s:${sessionId}/q:${questionId}/show_options`);
        return response.data;
    } catch (error) {
        console.error('Error fetching options:', error);
        throw error;
    }
};