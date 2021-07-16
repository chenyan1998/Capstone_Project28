<template>
<html>
  <div class = "top-left">

    <div class = "heading">
      <h3> Core Values Report</h3>
      <p class ="toppara"> DB Schenker's Core Values : 
      <br>1.  Play fair, be honest &nbsp;&nbsp;&nbsp; 2.  Be one team with one goal 
      <br>3.  Walk the talk &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.  Win together  
      <br>5.  Push limits   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6.  Take customers further </p>
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


    <div class = "reportgraph">
      <p> Average Score by Question </p>
      <column-chart :data="report_data3"></column-chart>
    </div>

</div>
</html>
</template>

<script>
export default {
    
  data() {
    return {
      report_data3: [],
    };
  },
  async mounted() {
    let data3 = await fetch ('http://127.0.0.1:8000/report/coreValues');
    const data = await data3.json()
    const data_x = data[0]["data_x"];
    const data_y = data[0]["data_y"];
    console.log("datax", data_x);
    console.log("datay", data_y);
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseInt(data_y[index])])
    });
    this.report_data3  = arr
    console.log(report_data3)
    },
};
    
</script>

<style>

</style>