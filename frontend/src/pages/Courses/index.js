import React, { useEffect, useState } from 'react';
import { getStudentCourses, getTeacherCourses, joinCourse, createCourse } from '../../api/course';
import './styles.css';

const Courses = ({ userRole }) => {
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

     
      const response =
        userRole === 'student'
          ? await getStudentCourses(userId, headers)
          : await getTeacherCourses(userId, headers);

      setCourses(response);
    } catch (error) {
      console.error('Error al obtener los cursos:', error);
      setError('No se pudieron cargar los cursos.');
    }
  };

  useEffect(() => {
    fetchCourses();
  }, [userRole]);

  const handleAction = async () => {
    if (userRole === 'student') {
      
      if (selectedCourse) {
        try {
          await joinCourse(selectedCourse.course_id);
          alert('Te has matriculado con éxito.');
        } catch (error) {
          console.error('Error al matricularse en el curso:', error);
          alert('Error al matricularse en el curso.');
        }
      } else {
        alert('Selecciona un curso para matricularte.');
      }
    } else if (userRole === 'teacher') {
      
      const courseName = prompt('Introduce el nombre del curso:');
      const courseSchedule = prompt('Introduce el horario del curso:');

      if (courseName && courseSchedule) {
        try {
          await createCourse({ course_name: courseName, course_schedule: courseSchedule });
          alert('Curso creado con éxito.');
          fetchCourses(); 
        } catch (error) {
          console.error('Error al crear el curso:', error);
          alert('Error al crear el curso.');
        }
      }
    }
  };

  return (
    <div className="container">
      <h1>{userRole === 'student' ? 'Mis Cursos' : 'Cursos que Imparto'}</h1>

      {error && <p className="error">{error}</p>}

      <ul className="course-list">
        {courses.map((course) => (
          <li key={course.course_id} className="course-item">
            <button
              onClick={() => setSelectedCourse(course)}
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
        onClick={handleAction}
        className="action-button"
      >
        {userRole === 'student' ? 'Matricular' : 'Crear curso'}
      </button>
    </div>
  );
};

export default Courses;
