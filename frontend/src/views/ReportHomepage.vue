<template>
  <el-row>
      <el-col :span="4"><h5>menu</h5><Sidebar/></el-col>  
      <el-col :span="20">
        
        <div v-if="metrics.length">
          <el-carousel :span="20">
            <el-carousel-item v-for="metric in metrics" :key="metric">
              <h3>{{metric.name}} &nbsp; &nbsp; &nbsp; &nbsp; {{metric._id}}</h3>
            </el-carousel-item>
          </el-carousel>
        </div>
        <el-skeleton v-else v-loading.fullscreen.lock="true" element-loading-text="Loading..."/>
        <el-divider></el-divider> 
        <el-calendar v-model="value"/>
      </el-col>
  </el-row>
</template>

<script>
import Sidebar from '../components/Sidebar'
import getSummaryMetrics from '../composables/getSummaryMetrics'
import {ref} from 'vue'
export default {
    name: 'ReportHomepage',
    components: {Sidebar},
    setup(){
    const report_list = ref(['DepartmentReport', 'QuestionReport', 'IndividualReport'])
    const {metrics, error, load} = getSummaryMetrics()
    const value = ref(new Date())
    load()
    return {report_list, metrics, error, value}
  }
}
</script>

<style>
.el-carousel__item h3 {
    color: #465774;
    font-size: 24px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>