<template>
<html>
  <TopNavigationBar/>
  <div class="home">
    
    <Sidebar :current_path="1" />
    <!-- <div v-for="nav in nav_list" :key="nav">
      <router-link :to="{name: nav}">
            <button>{{nav}}</button>
      </router-link>
    </div> -->
  </div>
  <div class="heading1">
  <h5> What are employee's completion rate over time? </h5>
  </div>
  <div class="graph1">
  <img src="@/assets/wellbeing.png" class="image1" width ="500" height = "250" align = "middle" top ="10">
  </div>

  <div class="box">
    <el-space direction="vertical">
    <el-card class="box-card" style="width: 250px" v-for="i in 1" :key="i">
      <template #header>
        <div class="card-header">
          <span>Pending completion</span>
        </div>
      </template>
      <div v-for="o in 6" :key="o" class="text item">
        {{ 'List item ' + o }}
      </div>
      <br>
      <div class="button">
      <el-button style="width:130px;" type="primary">Details</el-button>
      <br>
      <br>
      <el-button style="width:130px;" type="primary">Send reminder</el-button>
      </div>
    </el-card>
  </el-space>
  </div>

  <div class="dropdown1">
  <el-dropdown>
  <el-button style="width:200px;">
    Department<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Last 7 days</el-dropdown-item>
      <el-dropdown-item>Last 14 days</el-dropdown-item>
      <el-dropdown-item>Last 30 days</el-dropdown-item>
      <el-dropdown-item>Last month</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>

<div class="heading2">
  <h5>What are the average EEI score by question over time?</h5>
</div>
<div class="graph2">
<img src="@/assets/eei.jpg" class="image2" width ="780" height = "500" align = "middle" top ="10">
</div>

<div class="dropdown2">
  <el-dropdown>
  <el-button style="width:200px;">
    Department<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Last 7 days</el-dropdown-item>
      <el-dropdown-item>Last 14 days</el-dropdown-item>
      <el-dropdown-item>Last 30 days</el-dropdown-item>
      <el-dropdown-item>Last month</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>

<div class="heading3">
  <h5>What are the average wellbeing by question over time?</h5>
</div>
<div class="graph3">
  <img src="@/assets/graph.jpg" class="image3" width ="340" height = "320" align = "middle" top ="10">
</div>

<div class="dropdown3">
  <el-dropdown>
  <el-button style="width:200px;">
    Department<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Last 7 days</el-dropdown-item>
      <el-dropdown-item>Last 14 days</el-dropdown-item>
      <el-dropdown-item>Last 30 days</el-dropdown-item>
      <el-dropdown-item>Last month</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>

<div class="heading4">
  <h5>What are the average core value score by question over time?</h5>
</div>
<div class="graph4">
  <img src="@/assets/graph.jpg" class="image4" width ="340" height = "320" align = "middle" top ="10">
</div>

<div class="dropdown4">
  <el-dropdown>
  <el-button style="width:200px;">
    Department<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Last 7 days</el-dropdown-item>
      <el-dropdown-item>Last 14 days</el-dropdown-item>
      <el-dropdown-item>Last 30 days</el-dropdown-item>
      <el-dropdown-item>Last month</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>

<br>
<br>


  <el-table
    :data="tableData" id="table1"
    border
    style="width: 50%">
    <el-table-column
      prop="name"
      label="Name"
      width="180">
    </el-table-column>
    <el-table-column
      prop="id"
      label="Employee ID"
      width="180">
    </el-table-column>
    <el-table-column
      prop="department"
      label="Department">
    </el-table-column>
    <el-table-column
      prop="position"
      label="Position">
    </el-table-column>
  </el-table>

<div class="dropdown5">
  <el-dropdown>
  <el-button style="width:130px;">
    Department<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Last 7 days</el-dropdown-item>
      <el-dropdown-item>Last 14 days</el-dropdown-item>
      <el-dropdown-item>Last 30 days</el-dropdown-item>
      <el-dropdown-item>Last month</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>

 <el-divider class="divider"><i></i></el-divider>

</html>
</template>


<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import getEmployeeList from '../composables/getEmployeeList'

export default {
  name: 'Home',
  components: {Sidebar, TopNavigationBar},
  setup(){
    const nav_list = ref(['Profile','ReportHomepage','SurveyHomepage'])
    const {metrics, error, load} = getEmployeeList
    return {nav_list, metrics, error, load}
  },
data() {
      return {
        tableData: [{
          name: 'Tom',
          id: '123456',
          department: 'HR',
          position: 'Manager'
        }, {
          name: 'Alex',
          id: '123545',
          department: 'HR',
          position: 'Executive'
        }]
      }
    }
    
}
</script>

<style>
.heading1{
  position: absolute;
  top: 100px;
  left: 370px;
}

.heading2{
  position: absolute;
  top: 680px;
  left: 370px;
}

.heading3{
  position: absolute;
  top: 1330px;
  left: 370px;
}

.heading4{
  position: absolute;
  top: 1330px;
  left: 750px;
}

.image1{
  position: absolute;
  top: 150px;
  left: 370px;
}

.image2{
  position: absolute;
  top: 730px;
  left: 370px;
}

.image3{
  position: absolute;
  top: 1380px;
  left: 370px;
}

.image4{
  position: absolute;
  top: 1380px;
  left: 750px;
}

.box-card{
  position: absolute;
  top: 150px;
  left: 900px;
}

.dropdown1{
  position: absolute;
  top: 410px;
  left: 370px;
}

.dropdown2{
  position: absolute;
  top: 1240px;
  left: 370px;
}

.dropdown3{
  position: absolute;
  top: 1710px;
  left: 370px;
}

.dropdown4{
  position: absolute;
  top: 1710px;
  left: 750px;
}

.dropdown5{
  position: absolute;
  top: 640px;
  left: 1100px;
}

.box-card{
  background: aquamarine;
}

#table1{
  position: absolute;
  top: 540px;
  left: 370px;
}

.divider{
  position: absolute;
  top: 1240px;
  left: 0px;
}
</style>


