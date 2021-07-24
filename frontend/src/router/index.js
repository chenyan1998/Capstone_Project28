import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ReportHomepage from '../views/ReportHomepage.vue'
import SurveyHomepage from '../views/SurveyHomepage.vue'
import Login from '../views/Login.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import Profile from '../views/Profile.vue'
import DetailedReport from '../views/DetailedReport.vue'
import Individual from '../views/Individual.vue'
import Uploadfile from '../views/UploadFiles_tem.vue'
import Uploadfile_window from '../views/UploadFiles_tem1.vue'
import IndividualDetails from '../views/IndividualDetails.vue'

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
    path: '/uploadfile',
    name: 'Uploadfile',
    component: Uploadfile
  },
  {
    path: '/uploadfilewindow',
    name: 'Uploadfile1',
    component: Uploadfile_window
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
  },
  {
    path: '/individual',
    name: 'Individual',
    component: Individual
  },
  {
    path: '/individualdetails/:Employee_id',
    name: 'IndividualDetails',
    component: IndividualDetails,
    props: true
  }
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
