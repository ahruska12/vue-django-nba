<template>  
    <div class="row justify-content-center">
      <div class="col-md-5">
        <h1>Team Comparison</h1>
        <div class="form-group">
          <label for="team1">Team 1:</label>
          <select class="form-control" v-model="team1">
            <option v-for="team in teams" :value="team.name" :key="team.id">{{team.name}}</option>
          </select>
          <label for="team2">Team 2:</label>
          <select class="form-control" v-model="team2">
            <option value="" disabled selected>Please select an option</option>
            <option v-for="team in teams" :value="team.name" :key="team.id">{{team.name}}</option>
          </select>
        </div>
      
        <div v-if="team1 && team2">          
            <div class=""><h1>{{ team1 }} vs {{ team2 }}</h1></div>
          
          <table class="table">
            <thead>
              <tr>
                <th>Category</th>
                <th>{{comparisons.team1_name}}</th>
                <th>{{comparisons.team2_name}}</th>
                <th>Result</th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="(comparison, index) in comparisons.comparisons" :key="comparison">
                <td>{{index}}</td>
                <td>{{comparison.team1_value}}</td>
                <td>{{comparison.team2_value}}</td>
                <td>{{comparison.result}}</td>

              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          <p>Please select two teams to compare</p>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>

  import router from '../router';
  import {APIService} from '../http/APIService';


  const apiService = new APIService();
  
  export default {
    
    data() {
      return {
        teams: [],
        validUserName: "Guest",
        team1: null,
        team2: null,
        comparisons: [],
        category:'',
      };
    },
    watch: {
      team1: {
        immediate: true,
        handler() {
          if (this.team1 && this.team2) {
            this.compareTeams();
          }
        },
      },
      team2: {
        immediate: true,
        handler() {
          if (this.team1 && this.team2) {
            this.compareTeams();
          }
        },
      },
    },
    mounted(){
        this.getTeams();   
 
    },
        
    methods: {
        getTeams() {
                 apiService.getTeamList().then(response => {
                     this.teams = response.data.data;
                     this.teamSize = this.teams.length;

                     if (localStorage.getItem("isAuthenticates")
                         && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
                         this.validUserName = JSON.parse(localStorage.getItem("log_user"));
                     }
                 }).catch(error => {
                  
                     if (error.response.status === 401) {
                         localStorage.removeItem('isAuthenticates');
                         localStorage.removeItem('log_user');
                         localStorage.removeItem('token');
                         router.push("/AuthUser");
                     }
                 })
            },

      compareTeams() {
        if (!this.team1 || !this.team2) {
            this.
          alert('Please select two teams to compare');
          return;
        }
        
        const team1Id = this.getTeamId(this.team1);
        const team2Id = this.getTeamId(this.team2);

        apiService.getTeamComparison(team1Id,team2Id)
        .then(response => {
            this.comparisons = response.data.data;
            if (localStorage.getItem("isAuthenticates")
                         && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
                         this.validUserName = JSON.parse(localStorage.getItem("log_user"));
            }
        })        
          .catch(error => {            

            if (error.response.status === 401) {

              localStorage.removeItem('isAuthenticates');
              localStorage.removeItem('log_user');
              localStorage.removeItem('token');
              router.push("/AuthUser");
              }
          })

      },
      getTeamId(teamName) {
      const team = this.teams.find(t => t.name === teamName);
      return team ? team.team_id : null;
    },
 
    },
  };
  </script>
  <style>
  .teamName{
    width: 100%;
  };
  table, td {
    width: auto ! important;
  }
</style>