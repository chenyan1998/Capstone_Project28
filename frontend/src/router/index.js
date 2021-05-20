import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ReportHomepage from '../views/ReportHomepage.vue'
import SurveyHomepage from '../views/SurveyHomepage.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/report',
    name: 'ReportHomepage',
    component: ReportHomepage
  },
  {
    path: '/survey',
    name: 'SurveyHomepage',
    component: SurveyHomepage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
