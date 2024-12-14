import {
  Routes, Route, BrowserRouter as Router
} from 'react-router-dom';

import { Home, Login, SelectTypeUser, TeacherRegister, StudentRegister, Courses, CourseDetails } from '../pages';

const Approutes = () => {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users/login" element={<Login />} />
          <Route path="/select_type_user" element={<SelectTypeUser />} />
          <Route path="/users/student_register" element={<StudentRegister />} />
          <Route path="/users/teacher_register" element={<TeacherRegister />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/courses/:courseId" element={<CourseDetails />} />
        </Routes>
      </Router>
    </div>
  );
};

export default Approutes;

  