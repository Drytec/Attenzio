import {
    Routes, Route, BrowserRouter as Router
  } from 'react-router-dom';
  
  import { Home, Login, Register, StudentRegister, StudentCourses, TeacherRegister } from '../pages';
  
  const Approutes = () => {
    return (
      <div>
        <Router>
            <Routes>
              <Route path="/" element={<Home/>}></Route>
              <Route path="/login" element={<Login/>}></Route>
              <Route path="/register" element={<Register/>}></Route>
              <Route path="/studentRegister" element={<StudentRegister/>}></Route>
              <Route path="/teacherRegister" element={<TeacherRegister/>}></Route>
              <Route path="/studentCourses" element={<StudentCourses/>}></Route>
            </Routes>
        </Router>
      </div>
    )
  }
  export default Approutes;
  