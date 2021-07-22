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

              <div class="bestdepartment" v-for="bw in bestworstW" :key="bw">
                <h3> Wellbeing </h3>
                <p> Highest Department: {{bw.label_x}} </p>
                <p> Highest Score: {{bw.data_x}} </p>
                <p> Lowest Department: {{bw.label_y}}</p>
                <p> Lowest Score: {{bw.data_y}} </p>
                <br>
              </div>    
              <br>
              <div class="bestdepartment" v-for="bp in bestworstP" :key="bp">
                <h3> Personality </h3>
                <p> Highest Department: {{bp.label_x}} </p>
                <p> Highest Score: {{bp.data_x}} </p>
                <p> Lowest Department: {{bp.label_y}}</p>
                <p> Lowest Score: {{bp.data_y}} </p>
                <br>
              </div> 
          </div>

          <div class="homecolumnmiddle">
              <div class="bestdepartment" v-for="bc in bestworstC" :key="bc">
                <h3> Core Values </h3>
                <p> Highest Department: {{bc.label_x}} </p>
                <p> Highest Score: {{bc.data_x}} </p>
                <p> Lowest Department: {{bc.label_y}}</p>
                <p> Lowest Score: {{bc.data_y}} </p>
                <br>
              </div> 

              <br>
              <div class="bestdepartment" v-for="bo in bestworstO" :key="bo">
                <h3> Opinion </h3>
                <p> Highest Department: {{bo.label_x}} </p>
                <p> Highest Score: {{bo.data_x}} </p>
                <p> Lowest Department: {{bo.label_y}}</p>
                <p> Lowest Score: {{bo.data_y}} </p>
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
import UploadFiles from "../components/UploadFiles_tem";

export default {

    name: 'Home',
    components: {Sidebar, TopNavigationBar,UploadFiles},

    setup(){
      const userlist = ref ([])
      const error = ref (null)
      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/email')
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
      const bestworstW = ref ([])
      const error3 = ref (null)
      let data_xW = ref()
      let data_yW = ref()
      const load3 = async () =>{
            try{
                let data = await fetch ('http://127.0.0.1:8000/report/w_total_mean')
                if (!data.ok){
                    throw Error('no data available')
                    }
                bestworstW.value = await data.json()
                }
                catch (err){
                    error3.value = err.message
                    }
                data_xW = Math.round((bestworstW.value[0]["data_x"]*10)/10).toFixed(1);
                data_yW = Math.round((bestworstW.value[0]["data_y"]*10)/10).toFixed(1);
                console.log("...",data_xW)
                console.log("...",data_yW)
          }
      load3()
      const bestworstC = ref ([])
      const error4 = ref (null)
      const load4 = async () =>{
            try{
                let data = await fetch ('http://127.0.0.1:8000/report/c_total_mean')
                if (!data.ok){
                    throw Error('no data available')
                    }
                bestworstC.value = await data.json()
                }
                catch (err){
                    error4.value = err.message
                    }
          }
      load4()
      const bestworstP = ref ([])
      const error5 = ref (null)
      const load5 = async () =>{
            try{
                let data = await fetch ('http://127.0.0.1:8000/report/w_total_mean')
                if (!data.ok){
                    throw Error('no data available')
                    }
                bestworstP.value = await data.json()
                }
                catch (err){
                    error5.value = err.message
                    }
          }
      load5()
      const bestworstO = ref ([])
      const error6 = ref (null)
      const load6 = async () =>{
            try{
                let data = await fetch ('http://127.0.0.1:8000/report/o_total_mean')
                if (!data.ok){
                    throw Error('no data available')
                    }
                bestworstO.value = await data.json()
                }
                catch (err){
                    error6.value = err.message
                    }
          }
      load6()

    return {userlist, employeelist, bestworstW, bestworstC, bestworstP, bestworstO, error, error2, error3, error4, error5, error6} 
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
  height: 270px;
}

.pendingcompletion{
  text-align:center;
  position: absolute;
  top: 20%;
  left: 80%;
}

#risklevel{
  position: absolute;
  top:190%;
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