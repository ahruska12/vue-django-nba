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
                <div class="card" v-for="team in teams" v-bind:key="team">
                    <div class="card-header" :id="'heading' + team.pk">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" :data-bs-target="'#collapse' + team.pk" aria-expanded="true" :aria-controls="'collapse' + team.pk">
                            <h6 style="color: #0275d8; float: left">{{team.name}}</h6>
                        </button>
                    </div>


                    <div :id="'collapse' + team.pk" class="collapse" :aria-labelledby="'heading' + team.pk" data-bs-parent="#collapsable-card">
                        <div class="card-body">
                            <p><b>Team #:</b> {{team.team_id}}</p>
                            <p><b>Name:</b> {{team.name}}</p>
                            <p><b>Information:</b> <br/> {{team.abbreviation}}, <br/> {{team.city}}, <br/> {{team.state}} <br/> {{team.conference}} <br/> {{team.division}}</p>
                            <p><b>{{team.wins}}</b> <b>{{team.losses}}</b> <b>{{team.team_ppg}}</b> <b>{{team.team_rpg}}</b> <b>{{team.team_apg}}</b> <b>{{team.opp_ppg}}</b></p>
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
                        <th scope="col">Team ID</th>
                        <th scope="col">Name</th>
                        <th scope="col">Abbreviation</th>
                        <th scope="col">City</th>
                        <th scope="col">State</th>
                        <th scope="col">Conference</th>
                        <th scope="col">Division</th>
                        <th scope="col">Wins</th>
                        <th scope="col">Losses</th>
                        <th scope="col">Team PPG</th>
                        <th scope="col">Team RPG</th>
                        <th scope="col">Team APG</th>
                        <th scope="col">OPP PPG</th>
                        <th scope="col">Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for = "team in teams" v-bind:key="team">
                        <th scope="row">{{team.team_id}}</th>
                        <!--<td>{{team.team_id}}</td> -->
                        <td>{{team.name}}</td>
                        <td>{{team.abbreviation}}</td>
                        <td>{{team.city}}</td>
                        <td>{{team.state}}</td>
                        <td>{{team.conference}}</td>
                        <td>{{team.division}}</td>
                        <td>{{team.wins}}</td>
                        <td>{{team.losses}}</td>
                        <td>{{team.team_ppg}}</td>
                        <td>{{team.team_rpg}}</td>
                        <td>{{team.team_apg}}</td>
                        <td>{{team.opp_ppg}}</td>
                        <!--<router-link :to="{name: 'ViewTeam', params: { id: team.team_id }}> View </router-link> -->
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>




</template>




<script>


    import router from '../router';
    import {APIService} from '../http/APIService';
    const apiService = new APIService();


    export default {
        name: "TeamList",
        data: () => ({
            teams: [],
            validUserName: "Guest",
            teamSize: 0,
            showMsg: '',
            isMobile: false,
            headers: [
                {text: 'Team ID', sortable: false, align: 'left',},
                {text: 'Name', sortable: false, align: 'left',},
                {text: 'Abbreviation', sortable: false, align: 'left',},
                {text: 'City', sortable: false, align: 'left',},
                {text: 'State', sortable: false, align: 'left',},
                {text: 'Conference', sortable: false, align: 'left',},
                {text: 'Division', sortable: false, align: 'left',},
                {text: 'Wins', sortable: false, align: 'left',},
                {text: 'Losses', sortable: false, align: 'left',},
                {text: 'Team PPG', sortable: false, align: 'left',},
                {text: 'Team RPG', sortable: false, align: 'left',},
                {text: 'Team APG', sortable: false, align: 'left',},
                {text: 'OPP PPG', sortable: false, align: 'left',}

            ],


        }),
        mounted() {
            this.getTeams();
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
            }
        }
    }
</script>


<style>
    button {
        padding: 1rem;
        border: 0;
        cursor: pointer;
    }
</style>

