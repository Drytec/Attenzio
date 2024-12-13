import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', 
  headers: {
    'Content-Type': 'application/json',
  },
});

export const loginUser = async (email, password) => {
  const response = await api.post('/login/', { email, password });
  return response.data;
};

export const logoutUser = async () => {
  const response = await api.post('/logout/');
  return response.data;
};

export const registerUser = async (userData) => {
  const response = await api.post('/register/', userData);
  return response.data;
};

export const fetchHomeData = async () => {
  const response = await api.get('/home/');
  return response.data;
};

export default api;
