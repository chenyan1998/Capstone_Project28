<template>
<html>
  <div class = "top-left2">

    <div class = "heading">
      <h3> Personality Report</h3>
      <p class ="toppara"> Understanding personality help to build our leadership style, to resolve conflicts more effectively, to communicate more effectively, to understand how others make decisions and to retain key staff. </p>
    </div>

     <div id = "dropdown7">
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

  <div id = "dropdown8">
    <el-dropdown>
      <el-button style="width:200px;">
        Question Number<i class="el-icon-arrow-down el-icon--right"></i>
      </el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>Question 1</el-dropdown-item>
          <el-dropdown-item>Question 2</el-dropdown-item>
          <el-dropdown-item>Question 3</el-dropdown-item>
          <el-dropdown-item>Question 4</el-dropdown-item>
          <el-dropdown-item>Question 5</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>

  <div id = "dropdown9">
    <el-dropdown>
      <el-button style="width:200px;">
        Department<i class="el-icon-arrow-down el-icon--right"></i>
      </el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>Air Freight Division</el-dropdown-item>
          <el-dropdown-item>Ocean Freight Division</el-dropdown-item>
          <el-dropdown-item>Finance</el-dropdown-item>
          <el-dropdown-item>Sales and Sales Planning</el-dropdown-item>
          <el-dropdown-item>Contract Logistics/SCM</el-dropdown-item>
          <el-dropdown-item>Fairs, Exhibitions, Events</el-dropdown-item>
          <el-dropdown-item>CEO Office</el-dropdown-item>
          <el-dropdown-item>IT </el-dropdown-item>
          <el-dropdown-item>Global Projects / Industry Soln</el-dropdown-item>
          <el-dropdown-item>Human Resource</el-dropdown-item>
          <el-dropdown-item>HSSE</el-dropdown-item>
          <el-dropdown-item>Centre of Performance Excellence</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>

    <div class = "reportgraph">
      <p> Average Score by Question </p>
      <column-chart :data="report_data2"></column-chart>
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
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseInt(data_y[index])])
    });
    this.report_data2  = arr
  },
};
</script>


<style>

</style>