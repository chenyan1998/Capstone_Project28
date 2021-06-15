<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="2" />
<div class = "top-left">
  <div class = "heading">
  <h3> Survey Completion Rate </h3>
  </div>
  <div id = "e1">
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

<br>
<br>
<br> 
<br> 


<div class="row1">
    <div class="row1a">
        <div class="column1">
            <h3>Send Out Surveys</h3>
            <div id = "e7">
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
<br>
<div id = "e7">
<el-dropdown >
  <el-button style="width:200px;">
    Job Level<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Director</el-dropdown-item>
      <el-dropdown-item>Senior Manager</el-dropdown-item>
      <el-dropdown-item>Manager</el-dropdown-item>
      <el-dropdown-item>Assistant Manager</el-dropdown-item>
      <el-dropdown-item>Supervisors</el-dropdown-item>
      <el-dropdown-item>Executives</el-dropdown-item>
      <el-dropdown-item>Non-Executives</el-dropdown-item>
      <el-dropdown-item>Other </el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>
<br>
<div id = "e7">
<el-dropdown >
  <el-button style="width:200px;">
    Type of Collar Job<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>White Collar</el-dropdown-item>
      <el-dropdown-item>Blue Collar</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>
</div>
</div>
</div>
</div>
   <div class="row1b">
        <div class="column1">
            <table id ="surveytable">
  <tr>
    <th>Name</th>
    <th>Employee ID</th>
    <th>Company Email Address</th>
    <th>Phone Number</th>
    <th>Position</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>1000001</td>
    <td>AlfredsFutterkiste@dbschenker.com</td>
    <td>91234567</td>
    <td>Executive</td>
  </tr>
  <tr>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  
  </table>
        </div>
<el-row id ="send">
  <el-button style="width:200px; ">Send Out Survey</el-button>
</el-row>
<br>
<br>
<br> 

<div class="row1">
    <div class="row1a">
        <div class="column1">
<div class = "middle-left">
  <h3> Survey Completion Rate </h3>
  <p> Reminder will be send to individuals pending submission once every </p>
  </div>
  </div>
  </div>
  <div class="row1c">
        <div class="column1">
  <div id = "e8">
<el-dropdown >
  <el-button style="width:200px;">
    Duration<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>1 day</el-dropdown-item>
      <el-dropdown-item>3 days</el-dropdown-item>
      <el-dropdown-item>1 week</el-dropdown-item>
      <el-dropdown-item>2 weeks</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>
</div>
</div>
</div>

</div>
   







</html>
</template>

<script>
import TopNavigationBar from '../components/TopNavigationBar.vue'
import Sidebar from '../components/Sidebar'
export default {
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar}
}
</script>

<style>

div.row1a { text-align : left ;
padding-left: 350px;
}

div.row1b { text-align : left ;
padding-left: 620px;
}

div.row1c { text-align : left ;
padding-left: 550px;
}


.column1 {
  float: left;
  padding: 0px;
}

#surveytable {
  font-family: arial, sans-serif;
  border-collapse: collapse;

  position: absolute;
  top: 280px;
  left: 620px;
}

#surveytable td, th {
  border: 1px solid #b8bcc0;
  text-align: left;
  padding: 8px;
}

#surveytable tr:nth-child(1) {
  background-color: #D7DCE1;
}
#surveytable tr {
  background-color: #ffffff;
}

#send {
  position: absolute;
  top: 500px;
  right: 70px;
}

.middle-left{
  position: absolute;
  top: 550px;
  left: 370px;
}
</style>