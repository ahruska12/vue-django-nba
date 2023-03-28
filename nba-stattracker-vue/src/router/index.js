import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

const routes = [
  {
          path: '/',
          name: 'HomePage',
          component: () => import('../components/HomePage')
      },
      {
          path: '/PlayerList',
          name: 'ListPlayers',
          component: () => import('../components/ListPlayers')
      },
      {
        path: '/TeamList',
        name: 'ListTeams',
        component: () => import('../components/ListTeams')
      },
      {
          path: '/Player/:id',
          name: 'PlayerStats',
          component: () => import('../components/PlayerStats')
      },
      {
        path: '/Team/:id',
        name: 'TeamStats',
        component: () => import('../components/TeamStats')
      }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
