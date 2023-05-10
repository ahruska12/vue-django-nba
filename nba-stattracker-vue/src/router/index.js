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
        path: '/TeamFavoriteList',
        name: 'TeamFavorites',
        component: () => import('../components/TeamFavorites')
      },
      {
        path: '/PlayerFavoriteList',
        name: 'PlayerFavorites',
        component: () => import('../components/PlayerFavorites')
      },
      {
          path: '/Player/:id',
          name: 'Player',
          component: () => import('../components/PlayerComparison')
      },
      {
        path: '/Team/:id',
        name: 'Team',
        component: () => import('../components/TeamComparison'),
        props: true
    },
      {
          path: '/AuthUser',
          name: 'AuthUser',
          component: () => import('../components/AuthUser')
      },
      {
          path: '/RegisterUser',
          name: 'RegisterUser',
          component: () => import('../components/RegisterUser')
      },
      {
        path: '/StatDefinitions',
        name: 'StatDefinitions',
        component: () => import('../components/StatDefinitions')
    }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
