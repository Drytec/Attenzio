import apiClient from './apiClient';

/**
 * Función para permitir a un estudiante unirse a un curso.
 *
 * @param {number} courseId - ID del curso al que el estudiante desea unirse.
 * @returns {object} - Respuesta del servidor con el mensaje de éxito o error.
 */
export const getCourses = async () => {
    try {
        const response = await apiClient.get('courses/get_courses/');
        return response.data.courses;
    } catch (error) {
        console.error('Error fetching teacher courses:', error);
        throw error;
    }
};

/**
 * Función para permitir a un estudiante unirse a un curso.
 *
 * @param {number} courseId - ID del curso al que el estudiante desea unirse.
 * @returns {object} - Respuesta del servidor con el mensaje de éxito o error.
 */
export const joinCourse = async (courseId) => {
    try {
        const response = await apiClient.post(`courses/join_course/${courseId}/`);
        return response.data;  // Devuelve el mensaje de éxito.
    } catch (error) {
        console.error('Error joining course:', error);
        throw error;
    }
};

export const createCourse = async (courseData) => {
    try {
        const response = await apiClient.post('courses/create_course/', courseData);
        return response.data;
    } catch (error) {
        console.error('Error creating course:', error);
        throw error;
    }
};

export const getCourseDetails = async (courseId) => {
    try {
        const response = await apiClient.get(`courses/c:${courseId}/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching course details:', error);
        throw error;
    }
};

