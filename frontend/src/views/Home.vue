<template>
<html>
  <TopNavigationBar/>
  <Sidebar :current_path="1" />
  
    <div class="container1">
        <img  src= "@/assets/HomeIntroduction.png" alt="homeintro" class="homeintroduction" >
        <el-button class ="btn1">Import Survey Results</el-button>
        <el-button class ="btn2">Analyze Results</el-button>
    </div>

    <div class = "homeheading">
      <h3> Departments </h3>
      <p> Best and Worst performing departments by Survey Question type </p>
    
      <div class="homerow">
          <div class="homecolumnleft">

              <div class="bestdepartment">
                <h3> Wellbeing </h3>
                <p> Highest Department:</p>
                <p> Lowest Department:</p>
                <br>
              </div>    
              <br>
              <div class="bestdepartment">
                <h3> Personality </h3>
                <p> Highest Department:</p>
                <p> Lowest Department:</p>
                <br>
              </div>
          </div>

          <div class="homecolumnmiddle">
              <div class="bestdepartment">
                <h3> Core Values </h3>
                <p> Highest Department:</p>
                <p> Lowest Department:</p>
                <br>
              </div>

              <br>
              <div class="bestdepartment">
                <h3> Opinion </h3>
                <p> Highest Department:</p>
                <p> Lowest Department:</p>
                <br>
              </div>
          </div>

          <div class="homecolumnright">
              <div class="pendingcompletion">
                <el-space direction="vertical">
                  <el-card>
                    <template #header>
                      <div>
                        <span>Pending completion</span>
                      </div>
                    </template>
                    <div v-for="user1 in userlist" :key="user1" class="text item" >
                      {{ user1.name }}
                    </div>
                    <br><br><br>
                    <el-button style="width:100%;" class="homebtn">Details</el-button><br><br>
                    <el-button style="width:100%;" class="homebtn">Send Reminders</el-button>
                    
            
                  </el-card>
                </el-space>
              </div>
          </div>
      </div>
    </div>

       <div id="risklevel">
            <h3> Flight Risk Level </h3>
            <p> List of employees identified to have high Flight Risk level </p>
                <table id ="riskleveltable">
                  <tr>
                      <th>Name</th>
                      <th>Employee ID</th>
                      <th>Company Email Address</th>
                      <th>Phone Number</th>
                      <th>Position</th>
                  </tr>
                  <tr v-for="employee in employeelist" :key="employee">
                      <td>{{employee.name}}</td>
                      <td>12345</td>
                      <td>{{employee.email}}</td>
                      <td>{{employee.employee_details}}</td>
                      <td>{{employee.employee_risk_level}}</td>
                  </tr>
                </table>
      </div>
    

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

.container1 {
  position: absolute;
  width: 78%;
  left: 18%;
  top: 13%;
}
.container1 img {
  width: 100%;
  height: auto;
}

.container1 .btn1 {
  position: absolute;
  top: 72%;
  left: 79%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  background-color: #D7DCE1;
  color: black;
  cursor: pointer;
  width: 20%;
}
.container1 .btn2 {
  position: absolute;
  top: 82%;
  left: 78%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  background-color: #D7DCE1;
  color: black;
  cursor: pointer;
  width: 20%;
}

.homeheading{
  position: absolute;
  width: 78%;
  left: 18%;
  top: 100%;
  text-align: left;
}

.homecolumnleft {
  width: 38%;
  float: left;
}

.homecolumnmiddle {
  width: 38%;
  float: left;
}

.homecolumnright {
  width: 24%;
  float: left;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

.bestdepartment {
  width:90%;
  background-color: #CAE7EA;
  border-radius: 25px;
  padding: 10px;
}

.pendingcompletion{
  text-align:center;
  position: absolute;
  top: 20%;
  left: 80%;
}

#risklevel{
  position: absolute;
  top:170%;
  left: 18%;
  text-align: left;
}

#riskleveltable {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  position: relative;
  top: 20%;
  width: 180%;
  border: 1px solid #b8bcc0;
  text-align: left;
}

#riskleveltable td, th {
  border: 1px solid #b8bcc0;
  text-align: left;
  padding: 1%;
}


#riskleveltable tr:nth-child(1) {
  background-color: #D7DCE1;
}
#riskleveltable tr {
  background-color: #ffffff;
}

</style>