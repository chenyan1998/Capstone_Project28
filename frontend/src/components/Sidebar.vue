<template>
  <el-row class="tac">
  <el-col :span="4">
    <h5>Menu</h5>
    <el-menu
      :default-active="current_path"
      class="el-menu-vertical-demo"
      >
      <el-submenu index="1">
        <template #title>
          <i class="el-icon-document"></i>
          <span>Report</span>
        </template>
          <el-menu-item index="1-1" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'Wellbeing'}});
              }">Wellbeing Report</el-menu-item>
          <el-menu-item index="1-2" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'CoreValues'}});
              }">Core Values Report</el-menu-item>
          <el-menu-item index="1-3" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'Personality'}});
              }">Personality Report</el-menu-item>    
          <el-menu-item index="1-4" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'Opinion'}});
              }">Opinion Report</el-menu-item>    
      </el-submenu>
      <el-menu-item index="2" @click="()=>{
              this.$router.push({name: 'SurveyHomepage'})}">
        <i class="el-icon-menu"></i>
        <span>Survey</span>
      </el-menu-item>
      <el-menu-item index="3" @click="()=>{
              this.$router.push({name: 'Profile'})}">
        <i class="el-icon-setting"></i>
        <span>Profile</span>
      </el-menu-item>
    </el-menu>
  </el-col>
  
</el-row>
</template>

<script>
import { ref } from '@vue/reactivity'
export default {
  name: "Sidebar",
  props: ['current_path'],
  setup(props){
    const current_path = ref(props.current_path)
    return {current_path}
  }
}
</script>

<style>

</style>