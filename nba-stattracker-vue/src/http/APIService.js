import axios from 'axios';
const API_URL ='fullstack2023.pythonanywhere.com'; /* 'http://localhost:8000' http://127.0.0.1:8000/ or  'http://127.0.0.1:8000'*/

export class APIService {
  constructor() {

  }

  getTeam(param_pk) {
    const url = `${API_URL}/api/teams/${param_pk}`;
    let jwtToken = localStorage.getItem('token');
    console.log(":::jwtToken:::::"+jwtToken);
    const headers = {Authorization: `jwt ${jwtToken}`};
    return axios.get(url, {headers: headers});
  }

  getTeamList() {
    const url = `${API_URL}/api/teams/`;
    let jwtToken = localStorage.getItem('token');
    console.log(":::jwtToken:::::"+jwtToken);
    const headers = {Authorization: `jwt ${jwtToken}`};
    return axios.get(url, {headers: headers});

  }

  authenticateLogin(credentials) {
    const url = `${API_URL}/auth/`;
    return axios.post(url, credentials);
  }

  registerUser(credentials) {
     const url = `${API_URL}/register/`;
     credentials.customusername = credentials.username
     return axios.post(url, credentials);
  }
}
