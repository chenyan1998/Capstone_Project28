<template>
<html>
  <div id ="sidebar">
    <el-row class= "tac">
      <el-col :span="4">
        <h5>Menu</h5>
        <el-menu :default-active="current_path" class="el-menu-vertical-demo" menu-trigger="click">
          <el-menu-item index="1" @click="()=>{
                  this.$router.push({name: 'Home'})}">
                  <i class="el-icon-s-home"></i>
            <span>Home</span>
          </el-menu-item>
          <el-submenu index="2">
            <template #title>
              <i class="el-icon-document"></i>
              <span>Report</span>
            </template>
              <el-menu-item index="2-1" @click="()=>{
                  this.$router.push({name: 'DetailedReport', params: {report_type : 'Wellbeing'}});
                  }">Wellbeing Report</el-menu-item>
              <el-menu-item index="2-2" @click="()=>{
                  this.$router.push({name: 'DetailedReport', params: {report_type : 'CoreValues'}});
                  }">Core Values Report</el-menu-item>
              <el-menu-item index="2-3" @click="()=>{
                  this.$router.push({name: 'DetailedReport', params: {report_type : 'Personality'}});
                  }">Personality Report</el-menu-item>    
              <el-menu-item index="2-4" @click="()=>{
                  this.$router.push({name: 'DetailedReport', params: {report_type : 'Opinion'}});
                  }">Opinion Report</el-menu-item>    
          </el-submenu>
          <el-menu-item index="3" @click="()=>{
                  this.$router.push({name: 'SurveyHomepage'})}">
            <i class="el-icon-menu"></i>
            <span>Survey</span>
          </el-menu-item>
          <el-menu-item index="4" @click="()=>{
                  this.$router.push({name: 'Individual'})}">
                  <i class="el-icon-user"></i>
            <span>Individual</span>
          </el-menu-item>
          <el-menu-item index="5" @click="()=>{
                  this.$router.push({name: 'Profile'})}">
            <i class="el-icon-setting"></i>
            <span>Profile</span>
          </el-menu-item>
          <el-menu-item index="6" @click="()=>{
                  this.$router.push({name: 'Login'})}">
                  <i class="el-icon-switch-button"></i>
            <span>Sign Out</span>
          </el-menu-item>
        </el-menu>
     </el-col>
    
   </el-row>
  </div>
</html>
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

#sidebar{
  font-family: Georgia; 
  font-size: 14px;
  text-align: center;
  vertical-align: top;
	height: 100%;
	overflow: scroll;
}
</style>