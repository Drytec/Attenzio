import {
    Routes, Route, BrowserRouter as Router
  } from 'react-router-dom';
  
  import { Home, Login, SelectTypeUser, TeacherRegister, StudentRegister, Courses } from '../pages';
  
  const Approutes = () => {
    return (
      <div>
          <Routes>
              <Route path="/" element={<Home/>}></Route>
              <Route path="/users/login" element={<Login/>}></Route>
              <Route path="/select_type_user" element={<SelectTypeUser/>}></Route>
              <Route path="/users/student_register" element={<StudentRegister/>}></Route>
              <Route path="/users/teacher_register" element={<TeacherRegister/>}></Route>
              <Route path="/courses" element={<Courses/>}></Route>
          </Routes>
      </div>
    )
  }
  export default Approutes;
  