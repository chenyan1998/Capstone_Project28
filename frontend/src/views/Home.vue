<template>
  <div class="home">
    <Sidebar :current_path="1" />
    <!-- <div v-for="nav in nav_list" :key="nav">
      <router-link :to="{name: nav}">
            <button>{{nav}}</button>
      </router-link>
    </div> -->
  </div>
</template>
<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
export default {
  name: 'Home',
  components: {Sidebar},
  setup(){
    const nav_list = ref(['Profile','ReportHomepage','SurveyHomepage'])
    return {nav_list}
  }
}
</script>



