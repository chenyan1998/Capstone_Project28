<template>
  <el-row class="tac">
  <el-col :span="4" left-align>
    <h5>Menu</h5>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <el-submenu index="1">
        <template #title>
          <i class="el-icon-document"></i>
          <span>Report</span>
        </template>
          <el-menu-item index="1-1" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'DepartmentReport'}});
              }">Department Report</el-menu-item>
          <el-menu-item index="1-2" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'QuestionReport'}});
              }">Question Report</el-menu-item>
          <el-menu-item index="1-3" @click="()=>{
              this.$router.push({name: 'DetailedReport', params: {report_type : 'IndividualReport'}});
              }">Individual Report</el-menu-item>    
      </el-submenu>
      <el-menu-item index="2" @click="()=>{
              this.$router.push({name: 'SurveyHomepage'})}">
        <i class="el-icon-menu"></i>
        <span>Survey</span>
      </el-menu-item>
      <el-menu-item index="4" @click="()=>{
              this.$router.push({name: 'Profile'})}">
        <i class="el-icon-setting"></i>
        <span>Profile</span>
      </el-menu-item>
    </el-menu>
  </el-col>
  
</el-row>
</template>

<script>
export default {
}
</script>

<style>

</style>