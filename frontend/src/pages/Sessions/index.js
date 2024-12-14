import React, { useEffect, useState } from 'react'; 
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Routes, Route, Link, useParams } from 'react-router-dom';
import './styles.css'; 
import { getCourses } from '../../api/course';


const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const data = await getCourses();
        setCourses(data);
      } catch (err) {
        setError('Error fetching courses');
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Courses</h1>
      <ul>
        {courses.map((course) => (
          <li key={course.course_id}>
            <Link to={`/courses/${course.course_id}`}>{course.course_name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};


const CourseDetails = () => {
  const { courseId } = useParams();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCourse = async () => {
      try {
        const data = await getCourses();
        const selectedCourse = data.find((c) => c.course_id === parseInt(courseId));
        if (selectedCourse) setCourse(selectedCourse);
        else throw new Error('Course not found');
      } catch (err) {
        setError('Error fetching course details');
      } finally {
        setLoading(false);
      }
    };

    fetchCourse();
  }, [courseId]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>{course?.course_name}</h1>
      <p>Schedule: {course?.course_schedule}</p>
    </div>
  );
};


const AppRoutes = () => (
  <Routes>
    <Route path="/" element={<CourseList />} />
    <Route path="/courses/:courseId" element={<CourseDetails />} />
  </Routes>
);

const App = () => {
  return (
    <Router>
      <AppRoutes />
    </Router>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));

export { CourseDetails };
