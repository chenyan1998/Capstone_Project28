<template>
<html>
  <div class = "top-left">
  <div class = "heading">
  <h3> Personality Report</h3>
  <p class ="toppara"> Understanding personality help to build our leadership style, to resolve conflicts more effectively, to communicate more effectively, to understand how others make decisions and to retain key staff. </p>
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

}
</script>

<style>

</style>