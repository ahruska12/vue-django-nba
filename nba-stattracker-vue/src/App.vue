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
                  <router-link class="nav-link pr-3" to="/PlayerList">Player List</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="nav-link pr-3" to="/TeamList">Team List</router-link>
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
