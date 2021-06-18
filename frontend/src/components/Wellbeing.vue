<template>
<html>
<div class = "top-left">
  <div class = "heading">
  <h3> Wellbeing Report</h3>
  <p class ="toppara"> Good health and wellbeing is a core enabler of employee engagement and organisational performance. </p>
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
<div id = "e2">
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
<div id = "e3">
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



<div class = "graph1">
<div class = "top-left2">
<p> Average Score by Question </p>
<p>
<img src = "@/assets/wellbeing.png" width ="900" height = "450">  </p>
</div>
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

.graph1 {
  padding: 0 350px;
  text-align: left;
  margin-left: 350px;
}

.heading h3 {
  padding: 0 350px;
  text-align: left;
}
.heading p {
  padding-left :350px;
  padding-right : 100px;
  text-align: left;
}
.div container1{
  width: 300px;
  height: 100px;
  padding: 50px;
  border: 1px solid red;
}
.el-dropdown {
    vertical-align: top;

  }
  .el-dropdown + .el-dropdown {
    margin-left: 15px;

  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
.el-dropdown-menu {
   max-height:200px;
   overflow:scroll; 
}

.toppara {

  text-align: center;
  padding-left: 50px;
  padding-right: 50px;
}

#e1 {padding-left : 350px; float:left;}
#e2 {padding-left : 150px; float:left;}
#e3 {padding-left : 150px; float:left;}
#e4 {padding-left : 500px; float:left;}
#e5 {float:middle;}
#e6 {padding-left : 350px; float:left;}
#e8 {float :right;padding-top: 200px;}
  
</style>