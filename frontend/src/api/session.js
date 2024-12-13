import apiClient from './apiClient';

export const getSession = async (sessionId) => {
    try {
        const response = await apiClient.get(`sessions/s:${sessionId}/`);
        return response.data;  // Retorna los datos de la sesión
    } catch (error) {
        console.error('Error fetching session:', error);
        throw error;
    }
};

export const createSession = async (courseId, sessionData) => {
    try {
        const response = await apiClient.post(`sessions/create_session/`, {
            ...sessionData,
            course_id: courseId
        });
        return response.data;  // Retorna la respuesta con la nueva sesión creada
    } catch (error) {
        console.error('Error creating session:', error);
        throw error;
    }
};

export const createMaterial = async (sessionId, materialData) => {
    try {
        const response = await apiClient.post(`sessions/s:${sessionId}/create_material`, materialData);
        return response.data;  // Retorna los datos del nuevo material
    } catch (error) {
        console.error('Error creating material:', error);
        throw error;
    }
};

export const createQuestion = async (sessionId, questionData) => {
    try {
        const response = await apiClient.post(`sessions/s:${sessionId}/create_question`, questionData);
        return response.data;  // Retorna los datos de la nueva pregunta creada
    } catch (error) {
        console.error('Error creating question:', error);
        throw error;
    }
};

export const createOptions = async (sessionId, questionId, optionsData) => {
    try {
        const response = await apiClient.post(`sessions/s:${sessionId}/q:${questionId}/create_options`, {
            options: optionsData
        });
        return response.data;  // Retorna la respuesta con el mensaje de éxito
    } catch (error) {
        console.error('Error creating options:', error);
        throw error;
    }
};

export const getQuestions = async (sessionId) => {
    try {
        const response = await apiClient.get(`sessions/s:${sessionId}/show_questions`);
        return response.data;  // Retorna las preguntas de la sesión
    } catch (error) {
        console.error('Error fetching questions:', error);
        throw error;
    }
};

export const getOptions = async (sessionId, questionId) => {
    try {
        const response = await apiClient.get(`sessions/s:${sessionId}/q:${questionId}/show_options`);
        return response.data;  // Retorna las opciones de la pregunta
    } catch (error) {
        console.error('Error fetching options:', error);
        throw error;
    }
};