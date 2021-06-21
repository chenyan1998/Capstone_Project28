<template>
<html>
  <div class = "top-left">
  <div class = "heading">
  <h3> Opinion Report</h3>
  <p class ="toppara"> Employees' opinions helps us in finding problems in workforce, whether it's a problem with other employees or ones the employee themselves has.  </p>
  </div>
  <div id = "e6">
<el-dropdown>
  <el-button style="width:200px;">
    Survey Year<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>2021</el-dropdown-item>
      <el-dropdown-item>2020</el-dropdown-item>
      <el-dropdown-item>2019</el-dropdown-item>
      <el-dropdown-item>2018</el-dropdown-item>
      <el-dropdown-item>2017</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>
<div id = "e4">
<el-dropdown>
  <el-button style="width:200px;">
    Arranged by<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Average Score</el-dropdown-item>
      <el-dropdown-item>Number of Abnormal Scores</el-dropdown-item>
      <el-dropdown-item>Standard Deviation</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>
</div>
</html>
</template>

<script>
export default {
    methods: {
      handleClick() {
        alert('button click');
      }
    }
  }

</script>

<style>

</style>