import axios from './axios'; // Import the global axios instance

export const loginUser = async (email: string, password: string) => {
  const response = await axios.post('/auth/login/', { email, password });
  return response.data;
};

export const registerUser = async (username: string,email: string, password: string) => {
  const response = await axios.post('/auth/register/', { username,email, password });
  return response.data;
};

