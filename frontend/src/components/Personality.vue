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
<div class = "graph1">
<div class = "top-left2">
<p> Average Score by Question </p>
<column-chart :data="report_data2"></column-chart>
</div>
</div>
</div>


</html>

</template>

<script>


export default {
    
  data() {
    return {
      report_data2: [],
    };
  },
  async mounted() {
    let data2 = await fetch ('http://127.0.0.1:8000/report/personality');
    const data = await data2.json()
    const data_x = data[0]["data_x"];
    const data_y = data[0]["data_y"];
    console.log("datax", data_x);
    console.log("datay", data_y);
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseInt(data_y[index])])
    
    });
    this.report_data2  = arr
    console.log(report_data2)
  },
};
</script>

<style>

</style>