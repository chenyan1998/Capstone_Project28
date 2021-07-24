<template>
<<<<<<< Updated upstream
  <html>
    <TopNavigationBar/>
    <Sidebar :current_path="4"/>
    <div class = "top-left-individual">
        <h3>Employee List</h3>
        <p> Full list of DB Schenker Employees with flight risk identified </p>
            <el-table :data="employees" id ="individualtable">
              <el-table-column 
                prop="Employee_id" 
                label="Employee_id">
              </el-table-column>
              <el-table-column
                prop="EES_score"
                label="EES_score"
                >
              </el-table-column>
              <el-table-column
                prop="Flight_risk_label"
                label="Flight_risk_label"
                >
              </el-table-column>
              <el-table-column
                prop='Employee_id'
                label="Details">
                <router-link :to="{name: 'IndividualDetails', params: {Employee_id: 25443}}">
                  <el-button type="text" size="small">View Details</el-button>
                </router-link>
              </el-table-column>
            </el-table>
        
      
    </div>
  </html>
=======
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="5"/>
      <div class = "top-left-individual">

            <div id="individual">
                    <h3>Employee List</h3>
                    <table id ="individualtable">
                        <tr>
                            <th>Employee ID</th>
                            <th>EES Score</th>
                            <th>Wellbeing Score</th>
                            <th>Core Values Score</th>
                            <th>Personality</th>
                            <th>Opinion</th>
                            <th>Flight Risk Label</th>
                        </tr>
                        <tr v-for="individual in individuallist" :key="individual">
                            <td>{{individual.Employee_id}}</td>
                            <td>{{individual.EES_score}}</td>
                            <td>{{individual.Wellbeing}}</td>
                            <td>{{individual.Core_values}}</td>
                            <td>{{individual.Personality}}</td>
                            <td>{{individual.Opinion}}</td>
                            <td>{{individual.Flight_risk_label}}</td>
                        </tr>
                    </table>
            </div>

      </div>

</html>
>>>>>>> Stashed changes
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import {ref} from 'vue'

export default {
    name: 'Individual',
    components: {Sidebar, TopNavigationBar},
    setup(){
<<<<<<< Updated upstream
      const employees = ref ([])
=======
      const individuallist = ref ([])
>>>>>>> Stashed changes
      const error = ref (null)
      const highrisk_list = ref([])
      const load = async () =>{
<<<<<<< Updated upstream
        try{
            let data = await fetch ('http://localhost:8000/report/individuals')
            if (!data.ok){
                throw Error('no data available')
            }
            employees.value = await data.json()
          }
            catch (err){error.value = err.message}
          }
      load()
      return{employees, error}
=======
          try{
              let data = await fetch ('http://127.0.0.1:8000/report/individuals')
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')

              }
              individuallist.value = await data.json()
          }
              catch (err){
                  error.value = err.message
              }

              
          }
      load()
      return{individuallist, error}
>>>>>>> Stashed changes
    }

    
  }

</script>


<style>

.top-left-individual {
  position: absolute;
  top : 10%;
  left: 18%;
  width: 78%;
  text-align: left;
  max-height: 80%;
  overflow: scroll;
}

#individualtable {
  font-family: Georgia; 
  font-size: 14px;;
  border-collapse: collapse;
  position: relative;
  width: 100%;
  border: 1px solid #b8bcc0;
}

#individualtable td, th {
  border: 1px solid #b8bcc0;
  text-align: left;
  padding: 8px;
}

#individualtable tr:nth-child(odd) {
  background-color: #D7DCE1;
}

</style>