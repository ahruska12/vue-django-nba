import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import '@fortawesome/fontawesome-free/js/all'

import 'bootstrap/dist/css/bootstrap.min.css'

createApp(App).use(store, axios).use(router).mount('#app')
