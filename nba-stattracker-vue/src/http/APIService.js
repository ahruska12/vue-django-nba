import axios from 'axios';
const API_URL ='https://fullstack2023.pythonanywhere.com';


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
  getPlayer(param_pk) {
    const url = `${API_URL}/api/players/${param_pk}`;
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
  getPlayerList() {
    const url = `${API_URL}/api/players/`;
    let jwtToken = localStorage.getItem('token');
    console.log(":::jwtToken:::::"+jwtToken);
    const headers = {Authorization: `jwt ${jwtToken}`};
    return axios.get(url, {headers: headers});

  }

  getTeamById(teamId) {
    return axios.get(`${API_URL}/api/teams/${teamId}`);
  }
  getPlayerById(playerId) {
    return axios.get(`${API_URL}/api/players/${playerId}`);
  }
  getTeamComparison(team1Id, team2Id) {
  const url = `${API_URL}/api/teams/compare/${team1Id}/${team2Id}/`;
  let jwtToken = localStorage.getItem('token');
  console.log(":::jwtToken:::::"+jwtToken);
  const headers = {Authorization: `jwt ${jwtToken}`};
  return axios.get(url, {headers: headers});
  }
  getPlayerComparison(player1Id, player2Id) {
  const url = `${API_URL}/api/teams/compare/${player1Id}/${player2Id}/`;
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
