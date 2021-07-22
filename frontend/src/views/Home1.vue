<template>
<html>
  <TopNavigationBar/>
  <Sidebar :current_path="1" />
  
    <div class="container1" style="width:950px">
        <img  src= "@/assets/HomeIntroduction.png" alt="homeintro" class="homeintroduction" >
       
         <router-link :to="{name: 'SurveyHomepage'}">
            <el-button class ="btn1">Check Survey Results</el-button>
         </router-link>  
       
    </div>

    <div class = "homeheading">
      <h3> Departments </h3>
      <p> Best and Worst performing departments by Survey Question type </p>

      <div class="homerow">
          <div class="homecolumnleft">

            <el-card class="box-card" >
              <div  class="clearfix">
                <span> Wellbeing </span>
                <router-link :to="{name: 'Department'}">
                <el-button style="float: right; padding: 3px 0" type="text">Check Details</el-button>
                </router-link>              </div>
              <div v-for="bw in bestworstW" :key="bw" class="text item">
                <br>
                <br>
                <p> Highest Department: {{bw.label_x}} </p>
                <p> Highest Score: {{bw.data_x}} </p>
                <p> Lowest Department: {{bw.label_y}}</p>
                <p> Lowest Score: {{bw.data_y}} </p>
                <br>
              </div>
            </el-card>
            <br>
            <el-card class="box-card">
              <div  class="clearfix">
                <span>Personality</span>
                <router-link :to="{name: 'Department'}">
                <el-button style="float: right; padding: 3px 0" type="text">Check Details</el-button>
                </router-link>
              </div>
              <div v-for="bw in bestworstW" :key="bw" class="text item">
                <br>
                <br>
                <p> Highest Department: {{bw.label_x}} </p>
                <p> Highest Score: {{bw.data_x}} </p>
                <p> Lowest Department: {{bw.label_y}}</p>
                <p> Lowest Score: {{bw.data_y}} </p>
                <br>
              </div>
            </el-card>
          </div>
          
          <div class="homecolumnmiddle">
            <el-card class="box-card">
              <div  class="clearfix">
                <span>Core Values</span>
                <router-link :to="{name: 'Department'}">
                <el-button style="float: right; padding: 3px 0" type="text">Check Details</el-button>
                </router-link>              </div>
              <div v-for="bw in bestworstW" :key="bw" class="text item">
                <br>
                <br>
                <p> Highest Department: {{bw.label_x}} </p>
                <p> Highest Score: {{bw.data_x}} </p>
                <p> Lowest Department: {{bw.label_y}}</p>
                <p> Lowest Score: {{bw.data_y}} </p>
                <br>
              </div>
            </el-card>
            <br>
            <el-card class="box-card">
              <div  class="clearfix">
                <span>Opinion</span>
                <router-link :to="{name: 'Department'}">
                <el-button style="float: right; padding: 3px 0" type="text">Check Details</el-button>
                </router-link>              </div>
              <div v-for="bw in bestworstW" :key="bw">
                <br>
                <br>
                <p> Highest Department: {{bw.label_x}} </p>
                <p> Highest Score: {{bw.data_x}} </p>
                <p> Lowest Department: {{bw.label_y}}</p>
                <p> Lowest Score: {{bw.data_y}} </p>
                <br>
              </div>
            </el-card>

          </div>

      </div>
    </div>

       <div id="risklevel" style="width:970px">
            <h3> Flight Risk Level </h3>
            <p>The solution that will be developed is a Flight Risk Indicator Software that will assess an employee’s inputs to an engagement survey and determine if the employee is at risk of leaving the organisation. The output will come in the form of several indicative metrics to highlight the potential reasons for the employee’s engagement, or the lack thereof, with the organisation. Viewing such metrics in conjunction with existing HR tools will better enable the HR team to identify and address the unhappiness with the organisation that an employee is facing, which can help to reduce the turnover rate and result in a better working culture and environment for the organisation.</p>
            <p> List of employees identified to have high Flight Risk level </p>
                <table id ="riskleveltable" style="width:970px">
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
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
                <br>
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
                const data_xW = parseFloat(data[0]["data_x"]).toFixed(2);
                const data_yW = parseFLoat(data[0]["data_y"]).toFixed(2);
          }
      load3()

    return {userlist, employeelist, bestworstW, error, error2, error3}
    }}
</script>

<style>

.container1 {
	border-radius: 45px;
  width: 400px;
	height: 700px;
	margin: auto;
  position: absolute;
  width: 78%;
  left: 18%;
  top: 10%;
}
.container1 img {
  width: 100%;
  height: auto;
}
.container1 .btn1 {
  position: absolute;
  top: 58%;
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
  top: 65%;
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
  top: 75%;
  text-align: left;
}

.homecolumnleft {
  position: absolute;
  width: 38%;
  float: left;
  left: 40%;
}

.homecolumnmiddle {
  width: 38%;
  float: left;
  left: 48%;
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
  top:160%;
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

.text {
    font-size: 14px;
  }

.item {
    margin-bottom: 18px;
  }

.clearfix:before,
.clearfix:after {
    display: table;
    content: "";
  }
.clearfix:after {
    clear: both
  }

.box-card1 {
  
  background-color: rgba(82, 184, 175, 0.75);
	border-radius: 45px;
	height: 300px;
  width: 180px;
	margin: auto;
  position: absolute;
  width: 30%;
  left: 18%;
  top: 60%;
  }

</style>