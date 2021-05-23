<template>
  <div class="home">
    <div v-for="report_type in report_list" :key="report_type">
      <router-link :to="{name: 'DetailedReport', params: {report_type : report_type}}">
            <button>{{report_type}}</button>
      </router-link>
    </div>
    <button>Export</button>
  </div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
export default {
    name: 'ReportHomepage',
    components: {Sidebar},
    setup(){
    const report_list = ref(['DepartmentReport', 'QuestionReport', 'IndividualReport'])
    return {report_list}
  }
}
</script>

<style>

</style>