<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="5"/>
      <div class = "top-left-individual">
         <div id="individual">
              <h3>Employee List</h3>
              <el-dropdown @command="handleLevel">
                <el-button style="width:300px;">
                  {{level}}<i class="el-icon-arrow-down el-icon--right"></i>
                </el-button>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item command = "High">High</el-dropdown-item>
                    <el-dropdown-item command = "Low">Low</el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
          </div>
          
          <table id ="individualtable">
              <tr>
                  <th>Employee ID</th>
                  <th>EES Score</th>
                  <th>Flight Risk Label</th>
                  <th>View Details</th>
              </tr>
              <tr v-for="individual in individuallist" :key="individual">
                  <td>{{round(individual.Employee_id)}}</td>
                  <td>{{round(individual.EES_score)}}</td>
                  <td>
                    <el-tag v-if="individual.Flight_risk_label === 'Low Flight Risk'" size='small' type="success">
                      Low
                    </el-tag>
                    <el-tag v-if="individual.Flight_risk_label === 'High Flight Risk'" size='small' type="danger">
                      High
                    </el-tag>
                  </td>
                  <td>
                    <router-link :to="{name: 'IndividualDetails', params: {Employee_id: individual.Employee_id}}">
                      <el-button type="text" size="small">View</el-button>
                    </router-link>
                  </td>
              </tr>
          </table>
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
      let level = ref('Sort by Risk Level')
      let individuallist = ref ([])
      const error = ref (null)
      const highrisk_list = ref([])
      const load = async () =>{
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
      const round = (num) => {
        let truncated = num
        if (num.length > 5) {
            truncated = truncated.substr(0,5);
        }
        return truncated
      }
      const handleLevel = (command) => {
        if (command == 'High')
          individuallist.value.sort(function(a, b) {
            var textA = a.Flight_risk_label.toUpperCase();
            var textB = b.Flight_risk_label.toUpperCase();
            return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
          })
        else 
          individuallist.value.sort(function(a, b) {
            var textA = a.Flight_risk_label.toUpperCase();
            var textB = b.Flight_risk_label.toUpperCase();
            return (textA > textB) ? -1 : (textA < textB) ? 1 : 0;
          })

      }
      return{level, individuallist, error, round, handleLevel}
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

#individual{
  height: 100px;

}
#individualtable {
  font-family: Georgia; 
  font-size: 14px;
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