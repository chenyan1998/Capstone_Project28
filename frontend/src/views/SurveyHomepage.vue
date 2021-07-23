<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="3" />
    
  <div class = "top-left-survey">

      <div id="sendsurvey">
            <h3>Pending Completion of Surveys</h3>
                <table id ="surveytable">
                  <tr>
                      <th>Name</th>
                      <th>Employee ID</th>
                      <th>Company Email Address</th>
                      <th>Department</th>
                  </tr>
                  <tr v-for="employee in uncompletedsurvey" :key="employee">
                      <td>{{employee.name}}</td>
                      <td>{{employee._id}}</td>
                      <td>{{employee.email}}</td>
                      <td>{{employee.department}}</td>
                  </tr>
                </table>
      </div>
      <div id="sendsurveybutton">
            <el-row>
                 <el-button style="width:200px; ">Send Out Reminder</el-button>
            </el-row>
      </div>
      <div id = "surveycompletion">
          <h3> Survey Completion Rate </h3>
          <div id ="surveycompletionchart">
              <pie-chart :data="uncompleted"></pie-chart>
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
      const uncompletedsurvey = ref ([])
      const error = ref(null)
      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/email')
              if (!data.ok){
                  throw Error('no data available')
              }
              uncompletedsurvey.value = await data.json()
          }
              catch (err){
                  error.value = err.message
              }
          }
      load()
      return {uncompletedsurvey,error}
      }
    ,data(){return{
      uncompleted:[]
      };
    },
    async mounted(){
    let data2 = await fetch ('http://127.0.0.1:8000/email/completion_rate');
    const surveycompletionrate = await data2.json() 
    let x = surveycompletionrate*100
    let y = parseInt(Math.round(((1-surveycompletionrate)*100)))
    let uncompleted = [['Completed', x],['Uncompleted', y]]
    
    console.log("....", uncompleted)
    },

    
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
  width : 300px;
}


</style>