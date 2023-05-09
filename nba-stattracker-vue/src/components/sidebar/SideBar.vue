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
        <div></div>
        <div></div>
      </span>
      <span v-else>NBA Stat Tracker</span>
    </h1>

                  <SidebarLink icon="fas fa-home" to="/">Home Page</SidebarLink>
                  <SidebarLink icon="fas fa-people-group" :to="{ name: 'Team', params: { id: 'compare' } }">Team Compare</SidebarLink>
                  <SidebarLink icon="fas fa-people-arrows" :to="{ name: 'Player', params: { id: 'compare' } }">Player Compare</SidebarLink>
                  <SidebarLink icon="fas fa-person" :to="{name:'ListPlayers'}">Player List</SidebarLink>
                  <SidebarLink icon="fas fa-sitemap" :to="{name:'ListTeams'}">Team List</SidebarLink>
                  <SidebarLink icon="fas fa-basketball" v-if="!authenticated" @click="login"  :to="{name: 'AuthUser'}">Log in</SidebarLink>
                  <SidebarLink icon="fas fa-list" v-if="!authenticated" @click="register" :to="{name: 'RegisterUser'}">Register</SidebarLink>
                  <SidebarLink icon="fas fa-list" v-if="authenticated" @click="favorite" :to="{name: 'TeamFavorites'}">Favorites</SidebarLink>
                  <SidebarLink icon="fas fa-list" v-if="authenticated" @click="logout" :to="{name: 'AuthUser'}">Logout</SidebarLink>


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
    --sidebar-bg-color: #182c45;
    --sidebar-item-hover: #ff7300;
    --sidebar-item-active: #276749;
    --button-color: black;
    --button-background-color: rgb(255, 202, 0);
}
</style>

<style scoped>
.sidebar {
  color: #ff6a00;
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

  color: rgb(255, 106, 0);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

</style>