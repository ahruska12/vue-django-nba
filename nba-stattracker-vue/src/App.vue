<template>
  <div class="app">
    <header>
        <nav class="navbar justify-content-between flex-nowrap flex-row">
          <div class="container">
            <h1><span>NBA StatTracker</span>App</h1>
              <ul class="nav navbar-nav flex-row float-right">
                <li class="nav-item">
                  <router-link class="nav-link pr-3" to="/">Home Page</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link pr-3" :to="{ name: 'Team', params: { id: 'compare' } }">Team Comparison</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link pr-3" :to="{ name: 'Player', params: { id: 'compare' } }">Player Comparison</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link pr-3" :to="{name:'ListPlayers'}">Player List</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link pr-3" :to="{name:'ListTeams'}">Team List</router-link>
                </li>
                <li class="nav-item" v-if="!authenticated" @click="login" >
                  <router-link class="nav-link pr-3" :to="{name: 'AuthUser'}">Log in</router-link>
                </li>
                <li class="nav-item" v-if="!authenticated" @click="register" >
                  <router-link class="nav-link pr-3" :to="{name: 'RegisterUser'}">Register</router-link>
                </li>
                <li class="nav-item" v-if="authenticated" @click="favorite" >
                  <router-link class="nav-link pr-3" :to="{name: 'TeamFavorites'}">Favorites</router-link>
                </li>
                <li class="nav-item  .justify-content-end" v-if="authenticated" @click="logout" >
                  <router-link class="nav-link pr-3" :to="{name: 'AuthUser'}">Logout</router-link>
                </li>
              
              </ul>
          </div>
        </nav>
    </header>
  <main>
    <router-view class="modify"></router-view>
  </main>
  </div>
</template>


<script>
    import router from './router';
    import {APIService} from './http/APIService';
    const apiService = new APIService();


    export default{
        name: 'App',
        data: () => ({
            authenticated: false,
            dialog: false,
            menu: [
                { title: 'HomePage', url:"/"},
                { title: 'ListPlayers', url:"/PlayerList"},
                { title: 'ListTeams', url:"/TeamList"},
                { title: 'Team', url:"/Team/compare/"},
                { title: 'Player', url:"/Player/compare/"}
            ],
            teams: [],
            team: { id: 'abc' },
            players:[],
            player: { id: 'abc'}
        }),
        mounted() {
            apiService.getTeamList().then(response => {
                this.authenticated = true;
                console.log(response)
            }).catch(error => {
              
              if (error.response.status === 401) {
                    localStorage.removeItem('isAuthenticates');
                    localStorage.removeItem('log_user');
                    localStorage.removeItem('token');
                    this.authenticated = false;
                }
            });
            console.log('this.authenticated--'+this.authenticated);

            apiService.getPlayerList().then(response => {
                this.authenticated = true;
                console.log(response)
            }).catch(error => {
             
                if (error.response.status === 401) {
                    localStorage.removeItem('isAuthenticates');
                    localStorage.removeItem('log_user');
                    localStorage.removeItem('token');
                    this.authenticated = false;
                }
            });
            console.log('this.authenticated--'+this.authenticated);
        
        },
        


        methods: {
        //   getit(){
        //     apiService.getTeamList().then(response => {
        //         this.authenticated = true;
        //         console.log('nait',response)
        //     }).catch(error => {
        //         if (error.response.status === 401) {
        //             localStorage.removeItem('isAuthenticates');
        //             localStorage.removeItem('log_user');
        //             localStorage.removeItem('token');
        //             this.authenticated = false;
        //         }
        //     });
        //     console.log('this.authenticated--'+this.authenticated);
        // },


            logout() {
                localStorage.removeItem('isAuthenticates');
                localStorage.removeItem('log_user');
                localStorage.removeItem('token');
                this.authenticated = false;
                // router.push('/');
                window.location = "/"
            },
            login() {
                router.push("/AuthUser");
            },
        }
    };
</script>



<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 16;
}

nav {
  padding: 30px;
  background-color: rgb(35, 35, 35);
  color:azure;
  text-shadow: 2px 2px 2px black;

  a {
    font-weight: bold;
    color: azure;
    font-size:16;

    &.router-link-exact-active {
      color: #3e72d3;
    }
  }
}
</style>
