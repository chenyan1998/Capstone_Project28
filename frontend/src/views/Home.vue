<template>
<html>
  <TopNavigationBar/>
  <div class="home">
    
    <Sidebar :current_path="1" />
    <!-- <div v-for="nav in nav_list" :key="nav">
      <router-link :to="{name: nav}">
            <button>{{nav}}</button>
      </router-link>
    </div> -->
  </div>
  <h1> This is Home Page </h1>
</html>
</template>
<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
import TopNavigationBar from '../components/TopNavigationBar.vue'


export default {
  name: 'Home',
  components: {Sidebar, TopNavigationBar},
  setup(){
    const nav_list = ref(['Profile','ReportHomepage','SurveyHomepage'])
    return {nav_list}
  }
}
</script>



