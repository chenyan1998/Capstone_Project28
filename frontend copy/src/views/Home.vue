<template>
<html>
  <TopNavigationBar/>
  <Sidebar :current_path="1" />
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
        <div v-for="user1 in userlist" :key="user1" class="text item">
          {{ user1.name }}
        </div>
        <br>
        <div class="button">
          <el-button style="width:130px;" type="primary">
            Details
          </el-button>
          <br>
          <br>
          <el-button style="width:130px;" type="primary">
            Send reminder
          </el-button>
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

  <table id ="hometable">
    <tr>
      <th>Name</th>
      <th>Employee ID</th>
      <th>Department</th>
      <th>Email</th>
      <th>Risk Level</th>
    </tr>
    <tr v-for="employee1 in employeelist" :key="employee1">
        <td>{{employee1.name}}</td>
        <td>{{employee1._id}}</td>
        <td>{{employee1.department}}</td>
        <td>{{employee1.email}}</td>
        <td>{{employee1.employee_risk_level}}</td>
    </tr>
  </table>

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

  <el-divider class="divider">
    <i></i>
  </el-divider>

</html>
</template>


<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
import TopNavigationBar from '../components/TopNavigationBar.vue'
export default {

    name: 'Home',
    components: {Sidebar, TopNavigationBar},

    setup(){
      const userlist = ref ([])
      const error = ref (null)
      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/user')
              if (!data.ok){
                  throw Error('no data available')
                  }
              userlist.value = await data.json()
              }
              catch (err){
                  error.value = err.message
                  }
          }
      load()
      const employeelist = ref ([])
      const error2 = ref (null)
      const load2 = async () =>{
            try{
                let data = await fetch ('http://127.0.0.1:8000/employee')
                if (!data.ok){
                    throw Error('no data available')
                    }
                employeelist.value = await data.json()
                }
                catch (err){
                    error2.value = err.message
                    }
          }
      load2()

    return {userlist, employeelist, error,error2}
    }}
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

#hometable {
  font-family: arial, sans-serif;
  border-collapse: collapse;

  position: absolute;
  top: 500px;
  left: 370px;
}

#hometable td, th {
  border: 1px solid #b8bcc0;
  text-align: left;
  padding: 12px;
}

#hometable tr:nth-child(1) {
  background-color: #D7DCE1;
}
#hometable tr {
  background-color: #ffffff;
}
</style>