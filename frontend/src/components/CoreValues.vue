<template>
<html>
  <div class = "top-left">
  <div class = "heading">
  <h3> Core Values Report</h3>
  <p class ="toppara"> DB Schenker's Core Values : 
    <br>1.  Play fair, be honest  
    <br>2.  Be one team with one goal 
    <br>3.  Walk the talk
    <br>4.  Win together  
    <br>5.  Push limits 
    <br>6.  Take customers further </p>
  </div>
  <div id = "e1">
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