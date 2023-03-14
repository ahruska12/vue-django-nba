<template>
  <div>
    <h1>Welcome to NBA Stats Tracker!</h1>
    <form @submit.prevent="searchPlayer">
      <label for="player-name">Enter Player Name:</label>
      <input type="text" id="player-name" v-model="playerName" required>
      <button type="submit">Search</button>
    </form>
    <div v-if="playerStats">
      <h2>{{ playerStats.name }}</h2>
      <p>Points per game: {{ playerStats.points_per_game }}</p>
      <p>Assists per game: {{ playerStats.assists_per_game }}</p>
      <p>Rebounds per game: {{ playerStats.rebounds_per_game }}</p>
    </div>
  </div>
</template>


