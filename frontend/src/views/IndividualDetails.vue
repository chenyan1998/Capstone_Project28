<template>
  <div>
      <TopNavigationBar/>
      <Sidebar :current_path="4"/>
      <div class = "top-left-individualdetails">
        <el-descriptions title="Employee Analysis">
          <el-descriptions-item label="Employee ID">{{Employee_id}}</el-descriptions-item>
          <el-descriptions-item label="EES Score">{{employee.EES_score}}</el-descriptions-item>
          <el-descriptions-item label="Flight Risk Level">
            <el-tag v-if="employee.Flight_risk_label === 'Low Flight Risk'" size='small' type="success">
              Low
            </el-tag>
            <el-tag v-if="employee.Flight_risk_label === 'High Flight Risk'" size='small' type="danger">
              High
            </el-tag>
          </el-descriptions-item>
        </el-descriptions>
        <pie-chart :data="[['EES Score', employee.EES_score],
          ['Wellbeing', employee.Wellbeing],
          ['Core Values', employee.Core_values],
          ['Personality', employee.Personality], 
          ['Opinion', employee.Opinion]]">
        </pie-chart>
      </div>
  </div>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import {ref} from 'vue'
export default {
    name: 'IndividualDetails',
    components: {Sidebar, TopNavigationBar},
    props: ['Employee_id'],
    setup(props){
      console.log('this is the props', props)
      const employee = ref([])
      const error = ref()
      const load = async () =>{
        try{
            let data = await fetch ('http://localhost:8000/report/individuals/' + props.Employee_id)
            if (!data.ok){
                throw Error('no data available')
            }
            console.log('ook?')
            employee.value = await data.json()
            employee.value = employee.value[0]
            console.log(employee.value.Wellbeing)
        }
            catch (err){
                error.value = err.message
            }
        }
      load()
      return {employee}
    }
}
</script>

<style>
.top-left-individualdetails {
  position: absolute;
  top : 15%;
  left: 20%;
  width: 75%;
  /* background: green; */
}

#profiletable {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  position: relative;
  left: 20%;
  text-align: left;
  border-spacing: 5px;
  width :70%;
  border: 0px solid white;
}

#profiletable td, th {
  text-align: left;
  padding: 10px;
}
</style>