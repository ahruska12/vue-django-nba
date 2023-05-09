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
        <div>V</div>
        <div>S</div>
      </span>
      <span v-else>NBA StatTracker</span>
    </h1>

                  <router-link class="btn-primary" to="/">Home Page</router-link>
                  <router-link class="btn-secondary" :to="{ name: 'Team', params: { id: 'compare' } }">Team Comparison</router-link>
                  <router-link class="btn-secondary" :to="{ name: 'Player', params: { id: 'compare' } }">Player Comparison</router-link>
                  <router-link class="btn-secondary" :to="{name:'ListPlayers'}">Player List</router-link>
                  <router-link class="btn-secondary" :to="{name:'ListTeams'}">Team List</router-link>
                  <router-link class="btn-secondary" v-if="!authenticated" @click="login"  :to="{name: 'AuthUser'}">Log in</router-link>
                  <router-link class="btn-secondary" v-if="!authenticated" @click="register" :to="{name: 'RegisterUser'}">Register</router-link>
                  <router-link class="btn-secondary" v-if="authenticated" @click="favorite" :to="{name: 'TeamFavorites'}">Favorites</router-link>
                  <router-link class="btn-secondary" v-if="authenticated" @click="logout" :to="{name: 'AuthUser'}">Logout</router-link>

      <SidebarLink to="/image" icon="fas fa-image">Icon Here</SidebarLink>

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
</style>