import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Experience {
  id: number;
  company: string;
  position: string;
  duration: string;
  description: string;
  is_current: boolean;
  created_at: string;
}

export interface Project {
  id: number;
  title: string;
  description: string;
  technologies: string;
  github_url?: string;
  created_at: string;
}

export interface Skill {
  id: number;
  name: string;
  category: string;
  proficiency: number;
  created_at: string;
}

export interface Education {
  id: number;
  institution: string;
  degree: string;
  field_of_study: string;
  gpa: string;
  graduation_date: string;
  location: string;
  created_at: string;
}

export interface ContactMessage {
  name: string;
  email: string;
  message: string;
}

export const getExperiences = async (): Promise<Experience[]> => {
  const response = await api.get<Experience[]>('/experiences');
  return response.data;
};

export const getProjects = async (): Promise<Project[]> => {
  const response = await api.get<Project[]>('/projects');
  return response.data;
};

export const getSkills = async (): Promise<Skill[]> => {
  const response = await api.get<Skill[]>('/skills');
  return response.data;
};

export const getEducation = async (): Promise<Education[]> => {
  const response = await api.get<Education[]>('/education');
  return response.data;
};

export const sendContactMessage = async (message: ContactMessage): Promise<void> => {
  await api.post('/contact', message);
};

export default api;
