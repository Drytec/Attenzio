import React, { useEffect, useState } from 'react';
import { getCourses, joinCourse } from '../../api/course';
import './styles.css';

const Courses = ({ userRole }) => {
  const [courses, setCourses] = useState([]);
  const [error, setError] = useState(null);

  const fetchCourses = async () => {
    try {
      const response = await getCourses();
      if (response.courses && response.courses.length > 0) {
        setCourses(response.courses);
        setError(null);
      } else {
        setCourses([]);
        setError(null);
      }
    } catch (error) {
      console.error('Error al obtener los cursos:', error);
      setError('No se pudieron cargar los cursos.');
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const handleAction = async (courseId) => {
    if (userRole === 'student') {
      try {
        await joinCourse(courseId);
        alert('Te has matriculado con éxito.');
      } catch (error) {
        console.error('Error al matricularse en el curso:', error);
        alert('Error al matricularse en el curso.');
      }
    }
  };

  return (
      <div className="container">
        <h1>Cursos</h1>

        {error && <p className="error">{error}</p>}

        {courses.length === 0 && !error ? (
            <p>No hay cursos disponibles.</p>
        ) : (
            <ul className="course-list">
              {courses.map((course) => (
                  <li key={course.course_id} className="course-item">
                    <div className="course-details">
                      <p><strong>Nombre:</strong> {course.course_name}</p>
                      <p><strong>Horario:</strong> {course.course_schedule}</p>
                    </div>
                    {userRole === 'student' && (
                        <button
                            onClick={() => handleAction(course.course_id)}
                            className="course-button"
                        >
                          Entrar
                        </button>
                    )}
                  </li>
              ))}
            </ul>
        )}
      </div>
  );
};

export default Courses;






