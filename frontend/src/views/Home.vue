<template>
<html>
  <TopNavigationBar/>
  <Sidebar :current_path="1" />
  
        <div class="homeintroduction" >
          <h2> Welcome</h2>
          <p> This app is aming to </p>
          <div class="homecolumnlefta">
           <img  src= "@/assets/homepic1.png" style="width:50%">
            <p> 1. Design an accessible and quantifiable employee engagement indicator </p>

          </div>
          <div class="homecolumnmiddlea">
            <img  src= "@/assets/homepic2.png" style="width:50%">
            <p> 2. Predicting employee flight risk using holistic measures </p>
          
          </div>
          <div class="homecolumnrighta">
            <img  src= "@/assets/homepic3.png" style="width:50%">
            <p> 3. Without adding an additional layer of processing nor intruding on the employees' privacy </p>
          </div>
          <div id ="homeintroductionbelow">
            <p> Please press the value on the right to import the survey results, and produce analysed reports </p>
            <router-link :to="{name: 'SurveyHomepage'}">
                <el-button class ="btn1" style="font-family: Georgia; font-size: 14px;" >Check Survey Results</el-button>
            </router-link>  
          </div>
        </div>

        <div class = "homedepartment">
          <h3> Departments </h3>
          <p> Best and Worst performing departments by Survey Question type </p>

          <div class="homerow">
              <div class="homecolumnleft">

                <el-card class="homebox-card" >
                  <div  class="homeclearfix">
                    <span> Wellbeing </span>
                    <el-tooltip class="homecheckdetails" effect="light" content="Workplace well-being plays an important role in the sustainability of organizations and individuals, Promote health and high productivity of the individuals in the organization.">
                      <el-button>Check Details</el-button>
                    </el-tooltip>          
                  </div>
                  <div v-for="bw in bestworstW" :key="bw" class="text item">
                    <br>
                    <br>
                    <p> Highest Department: {{bw.label_x}} </p>
                    <p> Highest Score: {{round(bw.data_x[0])}} </p>
                    <p> Lowest Department: {{bw.label_y}}</p>
                    <p> Lowest Score: {{round(bw.data_y[0])}} </p>
                    <br>
                  </div>
                </el-card>
                <br>
                <el-card class="homebox-card">
                  <div  class="homeclearfix">
                    <span>Personality</span>
                    <el-tooltip class="homecheckdetails" effect="light" content="Personality traits are predictors of employee satisfaction, which may influence employee satisfaction level with the emotional commitment of the organization. ">
                      <el-button>Check Details</el-button>
                    </el-tooltip>   
                  </div>
                  <div v-for="bw in bestworstP" :key="bw" class="text item">
                    <br>
                    <br>
                    <p> Highest Department: {{bw.label_x}} </p>
                    <p> Highest Score: {{round(bw.data_x[0])}} </p>
                    <p> Lowest Department: {{bw.label_y}}</p>
                    <p> Lowest Score: {{round(bw.data_y[0])}} </p>
                    <br>
                  </div>
                </el-card>
              </div>
              
              <div class="homecolumnright">
                <el-card class="homebox-card">
                  <div  class="homeclearfix">
                    <span>Core Values</span>
                    <el-tooltip class="homecheckdetails1" effect="light" content="Core values are what support the vision, shape the culture and reflect what a company values. They are the essence of the company's identity – the principles, beliefs or philosophy of values.">
                      <el-button>Check Details</el-button>
                    </el-tooltip>                
                  </div>
                  <div v-for="bw in bestworstC" :key="bw" class="text item">
                    <br>
                    <br>
                    <p> Highest Department: {{bw.label_x}} </p>
                    <p> Highest Score: {{round(bw.data_x[0])}} </p>
                    <p> Lowest Department: {{bw.label_y}}</p>
                    <p> Lowest Score: {{round(bw.data_y[0])}} </p>
                    <br>
                  </div>
                </el-card>
                <br>
                <el-card class="homebox-card">
                  <div  class="homeclearfix">
                    <span>Opinion</span>
                    <el-tooltip class="homecheckdetails2" effect="light" content="Opinions refer to the employee’s perception of their role in the organisation. The stronger the sense of belonging, the greater the level of engagement. ">
                      <el-button>Check Details</el-button>
                    </el-tooltip>   
                  </div>
                  <div v-for="bw in bestworstO" :key="bw" class="text item">
                    <br>
                    <br>
                    <p> Highest Department: {{bw.label_x}} </p>
                    <p> Highest Score: {{round(bw.data_x[0])}} </p>
                    <p> Lowest Department: {{bw.label_y}}</p>
                    <p> Lowest Score: {{round(bw.data_y[0])}} </p>
                    <br>
                  </div>
                </el-card>

              </div>

          </div>
        </div>

        <div class="homeflightrisklevel">
              <h3> Flight Risk Level </h3>
              <!-- <p>The solution that will be developed is a Flight Risk Indicator Software that will assess an employee’s inputs to an engagement survey and determine if the employee is at risk of leaving the organisation. The output will come in the form of several indicative metrics to highlight the potential reasons for the employee’s engagement, or the lack thereof, with the organisation. Viewing such metrics in conjunction with existing HR tools will better enable the HR team to identify and address the unhappiness with the organisation that an employee is facing, which can help to reduce the turnover rate and result in a better working culture and environment for the organisation.</p> -->
              <p> List of employees identified to have high Flight Risk level </p>
                  <table id ="homeriskleveltable">
                    <tr>
                        <th>Name</th>
                        <th>Employee ID</th>
                        <th>Company Email Address</th>
                        <th>Employee Details</th>
                        <th>Risk Level</th>
                    </tr>
                    <tr v-for="employee in employeelist" :key="employee">
                        <td>{{employee.name}}</td>
                        <td>{{employee._id}}</td>
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
                let data = await fetch ('http://127.0.0.1:8000/report/p_total_mean')
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
      const round = (num) => {
        let truncated = num
        if (num.length > 5) {
            truncated = truncated.substr(0,5);
        }
        return truncated
      }

    return {userlist, employeelist, bestworstW, bestworstC, bestworstP, bestworstO, round} 
    }}
</script>

<style>

p{font-family: Georgia; font-size: 14px;}

h3{font-family: Georgia; font-size : 22px}

h4{font-family: Georgia; font-size : 16px}

.homeintroduction{
  position: absolute; padding: 5%;
  background-color: #167D86; color: white;
  height: 60%;  width: 78%;
  top: 10%; left: 18%;
}

.homeintroduction h2{
  text-decoration: underline;
  text-decoration-color: #EC0016;
  font-family: Papyrus;
  font-weight: bold;
  font-size: 50px;
}

.homeintroduction p{
  font-size: 14px;  
  font-family: Monaco;
}

.homerow{
  position: absolute;
  height: 90%;
  width: 100%;
  top:10%;
  overflow: scroll
}

.homecolumnlefta,.homecolumnrighta {
  width: 33%; float: left; padding : 0.5% 3% 0% 3%;
}

.homecolumnmiddlea {
  width: 33%; float: left; padding : 0% 3% 0% 3%;
}

#homeintroductionbelow{
  position:absolute;  padding: 1%;
  top:75%; left:5%; width:90%; height:15%;
  text-align: left;
  background-color: #F0F3F5; color: #646973;
  opacity: 90%;
}

#homeintroductionbelow p{
  position: absolute; width: 65%;
  left: 5%; top: 30%;
}

#homeintroductionbelow .btn1 {
  position: absolute;
  left:85%; top:50%; width: 20%;
  transform: translate(-50%, -50%); -ms-transform: translate(-50%, -50%);
  background-color: #D7DCE1; color: black;
  cursor: pointer;
}

.homedepartment{
  position: absolute;
  width: 78%;
  left: 18%;
  top: 75%;
  text-align: left;
  height: 80%
}

.homebox-card{
  background-color:white;
}

.homecheckdetails{
  position: relative;
  top: 5%;
  left: 55%;
  width: 30%;
  font-family: Georgia; 
  font-size: 14px;
  overflow: auto;
}

.homecheckdetails1{
  position: relative;
  top: 5%;
  left: 53.5%;
  width: 30%;
  font-family: Georgia; 
  font-size: 14px;
  overflow: auto;
  
}
.homecheckdetails2{
  position: relative;
  top: 5%;
  left: 60%;
  width: 30%;
  font-family: Georgia; 
  font-size: 14px;
  overflow: auto;
}

.homecolumnleft {
  width: 49%;
  float: left;
  overflow: scroll;
}

.homecolumnright {
  position: absolute;
  width: 49%;
  float: left;
  left: 51%;
  overflow: scroll;
}

.homeflightrisklevel{
  position : absolute;
  top: 160%;
  left : 18%;
  text-align: left;
  width: 78%;
  height:70%;
  float: left
}

#homeriskleveltable {
  font-family: Georgia;
  font-size: 14px;
  border-collapse: collapse;
  top: 20%;
  width: 100%;
  border: 1px solid #b8bcc0;
  text-align: left;
}

#homeriskleveltable td, th {
  border: 1px solid #b8bcc0;
  text-align: left;
  padding: 1%;
}

#homeriskleveltable tr:nth-child(1) {
  background-color: #D7DCE1;
}

#homeriskleveltable tr {
  background-color: #ffffff;
}

.homeclearfix:before, .homeclearfix:after {
    display: table;
    content: "";
  }
.homeclearfix:after {
    clear: both
  }




</style>