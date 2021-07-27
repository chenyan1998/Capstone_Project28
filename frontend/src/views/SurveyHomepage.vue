<template>
<html>
    <TopNavigationBar/>
    <Sidebar :current_path="1" />
    <div id="surveyhomepage">
        <div class="surveycontainer1">
            <div class = "surveytitle">
                <h3> DB Schenker Survey Results </h3>
                <div class="reportline"></div>
                <br/>
                <h4> Upload Survey Results </h4>
            <br/>
            <upload-files></upload-files>
            </div>
        </div>
          
        <div class="surveycontainer2">
            <div class = "surveytitle">
                <h3> Survey Completion Rate </h3>
                <div class="reportline"></div>
                
                <br/>           
                <h4> Completed Survey Numbers : {{completionnumber}}</h4><br/>
                <h4> Survey Completed Rate : {{completionrate*100}}% </h4><br/>
                <br/>
                <br/>
                <br/>
                <el-button id = "sendsurveybutton">
                    Send Out Survey
                </el-button>
            </div>
        </div>

        <div class="surveycontainer3">
            <div class = "surveytitle">
                <h3> Survey Introduction </h3>
                <div class="reportline"></div>
                <br/>
                <p style ="text-align:left; padding:10px">Our Survey questions consist of 4 main components. 
                    There are a total of 25 questions, aiming to measure employee's engagement level, as well as employee's flight risk.  </p>

                    <h4> 1. Wellbeing</h4>
                    <br/><p> There are 5 questions , including areas such as workplace wellbeing and emotional wellbeing.</p>
                    <h4> 2. Core Values</h4>
                    <br/><p>  There are 6 questions, where all 6 DB Schenker's core values are put into consideration to structure these questions.</p>
                    <h4> 3. Personality</h4>
                    <br/><p>  There are 7 questions, neurotism and agreeabless are the main factors included for consideration.</p>
                    <h4> 4. Opinions</h4>
                    <br/><p>  There are 5 questions, structured to understand the opinions and emotion of employees.
                </p>
            </div>
        </div>

        <div class = "surveycontainer4">
        <div id="sendsurvey" >
                <h3>Send Out New Surveys</h3>
                    <table id ="surveytable" style="font-family: Georgia; font-size: 14px;">
                    <tr>
                        <th>Name</th>
                        <th>Employee ID</th>
                        <th>Company Email Address</th>
                        <th>Employee Details</th>
                    </tr>
                    <tr v-for="employee in employees" :key="employee">
                        <td>{{employee.name}}</td>
                        <td>{{employee._id}}</td>
                        <td>{{employee.email}}</td>
                        <td>{{employee.employee_details}}</td>
                    </tr>
                    </table>
        </div>
        </div>
    </div>

</html>
</template>

<script>
import TopNavigationBar from '../components/TopNavigationBar.vue'
import Sidebar from '../components/Sidebar'
import UploadFiles from "../components/UploadFiles_tem";
import {ref} from 'vue'
export default {
    
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar,UploadFiles},
    setup(){
      const employees = ref ([])
      const error = ref (null)

      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/employee')
              if (!data.ok){
                  throw Error('no data available')
              }
              employees.value = await data.json()
          }
              catch (err){
                  error.value = err.message
              }
          }
      load()
      const completionrate = ref ()
      const error2 = ref (null)

      const load2 = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/email/completion_rate')
              if (!data.ok){
                  throw Error('no data available')
              }
              completionrate.value = await data.json()
              completionrate.value = completionrate.value[0]
          }
              catch (err){
                  error2.value = err.message
              }
          }
      load2()
      const completionnumber = ref ()
      const error3 = ref (null)

      const load3 = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/email/completion_number')
              if (!data.ok){
                  throw Error('no data available')
              }
              completionnumber.value = await data.json()
              completionnumber.value = completionnumber.value[0]
          }
              catch (err){
                  error3.value = err.message
              }
          }
      load3()
      // const {employees, error, load} = getEmployeeList()
      // load()
      return{employees,completionrate,completionnumber}
    }
}
</script>

<style>

#surveyhomepage{
    position: absolute; 
    padding: 5%;
    height: 100%;  
    width: 80%;
    top: 0%; 
    left: 18%;
}

.surveycontainer1 {
    position: absolute;
    float: left;
    width: 33%;
    left: 2%;
    height: 35%;
    border-color: #646973;
    border-style:solid;
    border-width: 2px;
    }

.surveytitle{
    text-align: middle;
    width: 100%;
    font-family: Georgia; 
    font-size : 16px;
    padding: 5px
}

.surveycontainer2 {
    position: absolute;
    float: left;
    width: 33%;
    left: 37%;
    height: 35%;
    border-color: #646973;
    border-style:solid;
    border-width: 2px;
    }

#sendsurveybutton{
    position:absolute;
    width: 40%;
    left: 30%;
    top: 62%
}

.surveycontainer3 {
    position: absolute;
    float: left;
    width: 28%;
    left: 72%;
    border-style: groove;
    background-color: #D7DCE1;
    }

.surveycontainer4{
    position: absolute;
    width: 68%;
    height: 50%;
    left: 2%;
    top: 47%;
    text-align: left;
    overflow: scroll;
}

#surveytable {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  position: relative;
  top: 10%;
  left: 0%;
  width: 100%;
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


</style>