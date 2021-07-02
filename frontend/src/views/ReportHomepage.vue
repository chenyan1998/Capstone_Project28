<template>
<html>
  <TopNavigationBar/>
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
import getReportMetric from '../composables/getReportMetric'
export default {
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar},
    setup(){
    const report_list = ref(['DepartmentReport', 'QuestionReport', 'IndividualReport'])
    const {metrics, error, load} = getReportMetric()
    return {report_list, metrics, error, load}
  }
}
</script>

<style>

</style>