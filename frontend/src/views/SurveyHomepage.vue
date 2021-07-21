<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="3" />
    
  <div class = "top-left-survey">

      <div id="sendsurvey">
            <h3>Send Out New Surveys</h3>
                <table id ="surveytable">
                  <tr>
                      <th>Name</th>
                      <th>Employee ID</th>
                      <th>Company Email Address</th>
                      <th>Phone Number</th>
                      <th>Position</th>
                  </tr>
                  <tr v-for="employee in employees" :key="employee">
                      <td>{{employee.name}}</td>
                      <td>12345</td>
                      <td>{{employee.email}}</td>
                      <td>{{employee.employee_details}}</td>
                      <td>{{employee.employee_risk_level}}</td>
                  </tr>
                </table>
      </div>
      <div id="sendsurveybutton">
            <el-row>
                 <el-button style="width:200px; ">Send Out Survey</el-button>
            </el-row>
      </div>
      <div id = "surveycompletion">
          <h3> Survey Completion Rate </h3>
          <div id ="surveycompletionchart">
              <pie-chart :data="[['Completed', 258], ['Uncompleted', 119]]" legend = "right"></pie-chart>
          </div>
      </div>    

  </div>
</html>
</template>

<script>
import TopNavigationBar from '../components/TopNavigationBar.vue'
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
export default {
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar},
    setup(){
      const employees = ref ([])
      const error = ref (null)

      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/employee')
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')

              }
              employees.value = await data.json()
              console.log(employees.value[0])
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
          }
      load()
      // const {employees, error, load} = getEmployeeList()
      // load()
      console.log('value is', employees)
      return{employees, error}
    }
}
</script>

<style>

.top-left-survey {
  position: absolute;
  top : 10%;
  left: 20%;
  width:75%;
}

#sendsurvey {
  position: relative;
  top: 10%;
  left: 10%;
  text-align: left;
}

#sendsurveybutton {
  position: absolute;
  top: 120%;
  left: 80%;
}

#surveytable {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  position: relative;
  top: 10%;
  left: 0%;
  width: 90%;
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

#surveycompletion {
  position: absolute;
  top: 150%;
  left: 10%;
  text-align: left;
}
#surveycompletionchart {
  position: relative;
  top: 0%;
  left: 230%;
  width : 300px;
}


</style>