<template>
  <html>
    <TopNavigationBar/>
    <Sidebar :current_path="4"/>
    <div class = "top-left-individual">
      <div id="individual">
        <h3>Employee List</h3>
        <el-table
          :data="employees"
          border
          style="width: 80%">
          <el-table-column
            prop="Employee_id"
            label="Employee_id"
            width="240">
          </el-table-column>
          <el-table-column
            prop="EES_score"
            label="EES_score"
            width="240">
          </el-table-column>
          <el-table-column
            prop="Flight_risk_label"
            label="Flight_risk_label"
            width="240">
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
      const employees = ref ([])
      const error = ref (null)
      const highrisk_list = ref([])
      const load = async () =>{
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
    }

    
  }

</script>


<style>

.top-left-individual {
  position: absolute;
  top : 10%;
  left: 20%;
  width: 75%;
  /* background-color: green; */
}

#individual {
  position: relative;
  left: 10%;
  text-align: left;
}


#individualtable {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  position: relative;
  width: 90%;
}

#individualtable td, th {
  border: 1px solid #b8bcc0;
  text-align: left;
  padding: 8px;
}

#individualtable tr:nth-child(1) {
  background-color: #D7DCE1;
}
#individualtable tr {
  background-color: #ffffff;
}
</style>