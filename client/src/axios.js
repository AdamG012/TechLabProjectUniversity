import axios from "axios";
import { API_URL } from "./config.json";

const transport = axios.create({
  baseURL: API_URL,
  withCredentials: true
});

export default transport;
