<template>
    <div class="container-fluid">
        <!--Welcome Title -->
        <div class="row align-items-center justify-content-center">
            <div class="col col-12 align-items-center justify-content-center">
                <blockquote>
                    Welcome {{ validUserName }}!
                    <footer>
                        <small>
                            <em>&mdash;NBAStatTracker, your one and only stop for NBA Statistics.</em>
                        </small>
                    </footer>
                </blockquote>
            </div>
        </div>


        <!-- Data table -->
        <div class="row align-items-center justify-content-center">
            <div class="d-md-none" id="collapsable-card" style="width: 80%">
                <div class="card" v-for="player in players" v-bind:key="player">
                    <div class="card-header" :id="'heading' + player.pk">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" :data-bs-target="'#collapse' + player.pk" aria-expanded="true" :aria-controls="'collapse' + player.pk">
                            <h6 style="color: #0275d8; float: left">{{player.name}}</h6>
                        </button>
                    </div>


                    <div :id="'collapse' + player.pk" class="collapse" :aria-labelledby="'heading' + player.pk" data-bs-parent="#collapsable-card">
                        <div class="card-body">
                            <p><b>Player #:</b> {{player.player_id}}</p>
                            <p><b>Name:</b> {{player.name}}</p>
                            <p><b>Information:</b> <br/> {{player.team}}, <br/> {{player.points}}, <br/> {{player.rebounds}} <br/> {{player.assists}} </p>
                            <p><b>{{player.steals}}</b> <b>{{player.blocks}}</b> <b>{{player.games_played}}</b></p>
                            </div>
                        </div>
                    </div>
                </div>


            </div>
            <div class="col col-12 col-md-10 d-none d-xl-block d-lg-block d-md-block">
                <table class="table table-hover" style="overflow-y: auto"
                       :headers="headers">
                    <thead>
                    <tr>
                        <th scope="col">Player ID</th>
                        <th scope="col">Name</th>
                        <th scope="col">Team</th>
                        <th scope="col">Points</th>
                        <th scope="col">Rebounds</th>
                        <th scope="col">Assists</th>
                        <th scope="col">Steals</th>
                        <th scope="col">Blocks</th>
                        <th scope="col">Games Played</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for = "player in players" v-bind:key="player">
                        <th scope="row">{{player.player_id}}</th>
                        <td>{{player.name}}</td>
                        <td>{{player.team}}</td>
                        <td>{{player.points}}</td>
                        <td>{{player.rebounds}}</td>
                        <td>{{player.assists}}</td>
                        <td>{{player.steals}}</td>
                        <td>{{player.blocks}}</td>
                        <td>{{player.games_played}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>




</template>




<!--<script>


    import router from '../router';
    import {APIService} from '../http/APIService';
    const apiService = new APIService();


    export default {
        name: "PlayerList",
        data: () => ({
            players: [],
            validUserName: "Guest",
            playerSize: 0,
            showMsg: '',
            isMobile: false,
            headers: [
                {text: 'Player ID', sortable: false, align: 'left',},
                {text: 'Name', sortable: false, align: 'left',},
                {text: 'Team', sortable: false, align: 'left',},
                {text: 'Points', sortable: false, align: 'left',},
                {text: 'Rebounds', sortable: false, align: 'left',},
                {text: 'Assists', sortable: false, align: 'left',},
                {text: 'Steals', sortable: false, align: 'left',},
                {text: 'Blocks', sortable: false, align: 'left',},
                {text: 'Games Played', sortable: false, align: 'left',}
            ],


        }),
        mounted() {
            // this.getPlayers();
            this.showMessages();
        },
        methods: {
            onResize() {
                if (window.innerWidth > 600)
                    this.isMobile = false;
                else
                    this.isMobile = true;
            },
            showMessages(){
                console.log(this.$route.params.msg)
                if (this.$route.params.msg) {
                    this.showMsg = this.$route.params.msg;
                }
             },
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
            }
        }
    }
</script>
-->

<style>
    button {
        padding: 1rem;
        border: 0;
        cursor: pointer;
    }
</style>
