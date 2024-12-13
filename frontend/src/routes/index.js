import {
    Routes, Route, BrowserRouter as Router
  } from 'react-router-dom';
  
  import { Home, Login, SelectTypeUser, TeacherRegister, StudentRegister } from '../pages';
  
  const Approutes = () => {
    return (
      <div>
        <Router>
            <Routes>
                <Route path="/" element={<Home/>}></Route>
                <Route path="users/login" element={<Login/>}></Route>
                <Route path="select_type_user" element={<SelectTypeUser/>}></Route>
                <Route path="users/student_register" element={<StudentRegister/>}></Route>
                <Route path="users/teacher_register" element={<TeacherRegister/>}></Route>
            </Routes>
        </Router>
      </div>
    )
  }
  export default Approutes;
  