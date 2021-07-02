import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ReportHomepage from '../views/ReportHomepage.vue'
import SurveyHomepage from '../views/SurveyHomepage.vue'
import Login from '../views/Login.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import Profile from '../views/Profile.vue'
import DetailedReport from '../views/DetailedReport.vue'
import Test from '../views/test.vue'

const routes = [
  {
    path: '/',
    redirect: {
      name: 'Login'
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },

  {
    path: '/test',
    name: 'test',
    component: Test
  },

  {
    path: '/home',
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
  },
  {
    path: '/forgotpassword',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/detailedreport',
    name: 'DetailedReport',
    component: DetailedReport
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
