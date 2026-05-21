//API service layer between your React frontend and backend server.

import axios from "axios";         //Axios helps send HTTP requests

const API = axios.create({
  baseURL: "http://localhost:5000"
});

export const getScreeningQuestions = () =>
  API.get("/questions/screening");

export const getFeatureQuestions = (condition) =>
  API.get(`/questions/${condition}`);

export const generateResponse = (data) =>
  API.post("/generate_response", data);