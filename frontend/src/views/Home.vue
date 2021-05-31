<template>
  <el-row>
        <el-col :span="4"><h5>menu</h5><Sidebar :current_path="1" /></el-col>  
        <el-col :span="12"> <h2>Profile page</h2></el-col>
  </el-row>
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



