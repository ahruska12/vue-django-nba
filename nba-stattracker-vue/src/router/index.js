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
          name: 'PlayerComparison',
          component: () => import('../components/PlayerComparison')
      },
      {
        path: '/Team/:id',
        name: 'TeamComparison',
        component: () => import('../components/TeamComparison')
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
      }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
