<template>
    <div class="row justify-content-center">
      <div class="col-md-5">
        <h1>Player Comparison</h1>
        <div class="form-group">
            
          <label for="player1">Player 1:</label>
          <select class="form-control" v-model="player1">
            <option v-for="player in players" :value="player.name" :key="player.id">{{player.name}}</option>

          </select>
          <label for="player2">Player 2:</label>
          <select class="form-control" v-model="player2">
            <option v-for="player in players" :value="player.name" :key="player.id">{{player.name}}</option>
          </select>
        </div>
        <div v-if="player1 && player2">
            <div>{{ player1 }} vs {{ player2 }}</div>
          
          <table class="table">
            <thead>
              <tr>
                <th>Category</th>
                <th>{{comparisons1.player1_name}}</th>
                <th>{{comparisons1.player2_name}}</th>
                <th>Result</th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="(comparison, index) in comparisons1.comparisons" :key="comparison">
                <td>{{index}}</td>
                <td>{{comparison.player1_value}}</td>
                <td>{{comparison.player2_value}}</td>
                <td>{{comparison.result}}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else>
          <p>Please select two players to compare</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import router from '../router';
  import {APIService} from '../http/APIService';
  const apiService = new APIService();
  
  export default {
    
    data() {
      return {
        players: [],
        validUserName: "Guest",
        player1: null,
        player2: null,
        comparisons1: [],
        category:'',
      };
    },
    watch: {
      player1: {
        immediate: true,
        handler() {
          if (this.player1 && this.player2) {
            this.compareplayers();
          }
        },
      },
      player2: {
        immediate: true,
        handler() {
          if (this.player1 && this.player2) {
            this.comparePlayers();
          }
        },
      },
    },
    mounted(){
        this.getPlayers();        
    },
    
    methods: {
        getPlayers() {
                 apiService.getPlayerList().then(response => {
                     this.players = response.data.data;
                     this.playerSize = this.players.length;
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

        comparePlayers() {
            const player1Id = this.getPlayerId(this.player1);
            const player2Id = this.getPlayerId(this.player2);

            axios.get(`/api/teams/compare/${player1Id}/${player2Id}`)
            .then(response => {
                this.comparisons1 = response.data.data;               
                if (localStorage.getItem("isAuthenticates")
                             && JSON.parse(localStorage.getItem("isAuthenticates")) === true) {
                             this.validUserName = JSON.parse(localStorage.getItem("log_user"));
                }
            })
            
            .catch(error => {
            console.log(error)
                     if (error.response.status === 401) {
                         localStorage.removeItem('isAuthenticates');
                         localStorage.removeItem('log_user');
                         localStorage.removeItem('token');
                         router.push("/AuthUser");
                     }
                 })
      },
      getPlayerId(playerName) {
      const player = this.players.find(t => t.name === playerName);
      console.log('na d player',player)
      return player ? player.player_id : null;
    },
    
    },
  };
  </script>