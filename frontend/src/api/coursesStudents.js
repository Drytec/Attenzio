import apiClient from './apiClient';
const getStudentCourses = async (userId, authToken) => {
  try {

    const headers = {
      Authorization: `Bearer ${authToken}`,
    };

  
    const response = await apiClient.get(`/students/${userId}/courses/`, { headers });


    return response.data;
  } catch (error) {

    console.error('Error al obtener los cursos del estudiante:', error);
    throw error;
  }
};


(async () => {
  const userId = 1; 
  const authToken = 'tu-token-de-autenticacion'; 

  try {
    const courses = await getStudentCourses(userId, authToken);
    console.log('Cursos del estudiante:', courses);
  } catch (error) {
    console.error('No se pudieron obtener los cursos:', error);
  }
})();
