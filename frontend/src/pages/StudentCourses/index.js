import React, { useEffect, useState } from 'react';
import apiClient from '../../api/apiClient';
import './styles.css';

const StudentCourses = () => {
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState(null);
  const [error, setError] = useState(null);

  const userId = 1; 
  const authToken = 'tu-token-de-autenticacion'; 

  const fetchCourses = async () => {
    try {
      const headers = {
        Authorization: `Bearer ${authToken}`,
      };

      const response = await apiClient.get(`/students/${userId}/courses/`, { headers });
      setCourses(response.data.courses);
    } catch (error) {
      console.error('Error al obtener los cursos del estudiante:', error);
      setError('No se pudieron cargar los cursos.');
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const handleCourseClick = (course) => {
    setSelectedCourse(course);
  };

  const handleEnroll = () => {
    alert('Función para matricularse en un curso.');
  };

  return (
    <div className="container">
      <h1>Mis Cursos</h1>

      {error && <p className="error">{error}</p>}

      <ul className="course-list">
        {courses.map((course) => (
          <li key={course.course_id} className="course-item">
            <button
              onClick={() => handleCourseClick(course)}
              className="course-button"
            >
              {course.course_name}
            </button>
          </li>
        ))}
      </ul>

      {selectedCourse && (
        <div className="course-details">
          <h2>Detalles del Curso</h2>
          <p><strong>Nombre:</strong> {selectedCourse.course_name}</p>
          <p><strong>Horario:</strong> {selectedCourse.course_schedule}</p>
        </div>
      )}

      <button
        onClick={handleEnroll}
        className="enroll-button"
      >
        Matricular
      </button>
    </div>
  );
};

export default StudentCourses;