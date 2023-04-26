import axios from 'axios';
const API_URL ='https://fullstack2023.pythonanywhere.com/';

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

  getPlayer(param_pk) {
    const url = `${API_URL}/api/players/${param_pk}`;
    let jwtToken = localStorage.getItem('token');
    console.log(":::jwtToken:::::"+jwtToken);
    const headers = {Authorization: `jwt ${jwtToken}`};
    return axios.get(url, {headers: headers});
  }

  getPlayerList() {
    const url = `${API_URL}/api/players/`;
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
