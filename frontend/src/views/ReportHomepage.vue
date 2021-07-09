<template>
<html>
  <TopNavigationBar/>
  <Sidebar :current_path="2" />
  <div class="home">
    <div v-for="report_type in report_list" :key="report_type">
      <router-link :to="{name: 'DetailedReport', params: {report_type : report_type}}">
            <button>{{report_type}}</button>
      </router-link>
    </div>
    <button>Export</button>
  </div>

  
</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
import TopNavigationBar from '../components/TopNavigationBar.vue'
export default {
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar}
}
</script>

<style>

</style>