<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="5"/>
      <div class = "heading">

        <div id="sendsurvey">
              <h3>Employee List</h3>
                  <table id ="surveytable">
                    <tr>
                        <th>Name</th>
                        <th>Employee ID</th>
                        <th>Company Email Address</th>
                        <th>Employee Detail</th>
                        <th>Risk Level</th>
                    </tr>
                    <tr v-for="employees in employeeslist" :key="employees">
                        <td>{{employees.name}}</td>
                        <td>12345</td>
                        <td>{{employees.email}}</td>
                        <td>{{employees.employee_details}}</td>
                        <td>{{employees.employee_risk_level}}</td>
                    </tr>
                  </table>
        </div>
        <div id="sendsurveybutton">
              <el-row>
                  <el-button style="width:200px; ">Check Individual Report</el-button>
              </el-row>
        </div>



      </div>

</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import {ref} from 'vue'

export default {
    name: 'Individual',
    components: {Sidebar, TopNavigationBar},
    setup(){
      const employeeslist = ref ([])
      const error = ref (null)

      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/employee')
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')

              }
              employeeslist.value = await data.json()
              console.log(employees.value[0])
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
          }
      load()
      return{employeeslist, error}
    }
  }

</script>


<style>



</style>