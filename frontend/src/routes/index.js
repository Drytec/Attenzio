import {
    Routes, Route, BrowserRouter as Router
  } from 'react-router-dom';
  
  import { Home, Login, SelectTypeUser, StudentCourses, SelectTypeuser, Main, TeacherCourses, AdminCourses, TeacherRegister, StudentRegister } from '../pages';
  
  const Approutes = () => {
    return (
      <div>
        <Router>
            <Routes>
                <Route path="/" element={<Home/>}></Route>
                <Route path="users/main" element={<Main/>}></Route>
                <Route path="users/login" element={<Login/>}></Route>
                <Route path="select_type_user" element={<SelectTypeUser/>}></Route>
                <Route path="users/student_register" element={<StudentRegister/>}></Route>
                <Route path="users/teacher_register" element={<TeacherRegister/>}></Route>
                <Route path="courses/student_courses" element={<Courses/>}></Route>
                <Route path="courses/teacher_courses" element={<TeacherCourses/>}></Route>
                <Route path="courses/admind_courses" element={<AdminCourses/>}></Route>
            </Routes>
        </Router>
      </div>
    )
  }
  export default Approutes;
  