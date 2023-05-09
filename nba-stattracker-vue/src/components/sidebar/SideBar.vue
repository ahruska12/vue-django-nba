<script>
import SidebarLink from './SidebarLink'
import { collapsed, toggleSidebar, sidebarWidth } from './state'

export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth }
  }
}
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div>NBA</div>
        <div>App</div>
      </span>
      <span v-else>NBA Stat </span>
    </h1>

                  <SidebarLink icon="fas fa-home" to="/">Home Page</SidebarLink>
                  <router-link class="btn-secondary" :to="{ name: 'Team', params: { id: 'compare' } }">Team Comparison</router-link>
                  <router-link class="btn-secondary" :to="{ name: 'Player', params: { id: 'compare' } }">Player Comparison</router-link>
                  <router-link class="btn-secondary" :to="{name:'ListPlayers'}">Player List</router-link>
                  <router-link class="btn-secondary" :to="{name:'ListTeams'}">Team List</router-link>
                  <router-link class="btn-secondary" v-if="!authenticated" @click="login"  :to="{name: 'AuthUser'}">Log in</router-link>
                  <router-link class="btn-secondary" v-if="!authenticated" @click="register" :to="{name: 'RegisterUser'}">Register</router-link>
                  <router-link class="btn-secondary" v-if="authenticated" @click="favorite" :to="{name: 'TeamFavorites'}">Favorites</router-link>
                  <router-link class="btn-secondary" v-if="authenticated" @click="logout" :to="{name: 'AuthUser'}">Logout</router-link>


    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
    --sidebar-bg-color: #2f855a;
    --sidebar-item-hover: #38a169;
    --sidebar-item-active: #276749;
    --button-color: black;
    --button-background-color: rgb(255, 202, 0);
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

.btn-primary {
  color: var(--button-color);
  background-color: var(--button-background-color);
  border-radius: var(--border-radius);
}

.btn-primary:hover {
  box-shadow: inset 0 0 0 20rem var(--darken-1);
}

.btn-primary:active {
  box-shadow: inset 0 0 0 20rem var(--darken-2),
    inset 0 3px 4px 0 var(--darken-3),
    0 0 1px var(--darken-2);
}

.btn-primary:disabled,
.btn-primary.is-disabled {
  opacity: .5;
}

</style>