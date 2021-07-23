<template>
    <html>
        <div class = "top-left-report">
          
          <div class = "heading">
              <h3> Wellbeing Report</h3>
              <p> Good health and wellbeing is a core enabler of employee engagement and organisational performance. </p>
          </div>

          <div id = "report-dropdown">
              <el-dropdown @command="handleDepartment">
                <el-button style="width:300px;">
                  {{current_departmentW}}<i class="el-icon-arrow-down el-icon--right"></i>
                </el-button>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item command = "Air Freight Division">Air Freight Division</el-dropdown-item>
                    <el-dropdown-item command = "Ocean Freight Division">Ocean Freight Division</el-dropdown-item>
                    <el-dropdown-item command = "Finance">Finance</el-dropdown-item>
                    <el-dropdown-item command = "Sales and Sales Planning">Sales and Sales Planning</el-dropdown-item>
                    <el-dropdown-item command = "Contract Logistics/SCM">Contract Logistics/SCM</el-dropdown-item>
                    <el-dropdown-item command = "Fairs, Exhibitions, Events">Fairs, Exhibitions, Events</el-dropdown-item>
                    <el-dropdown-item command = "CEO Office" disabled>CEO Office</el-dropdown-item>
                    <el-dropdown-item command = "IT">IT </el-dropdown-item>
                    <el-dropdown-item command = "Global Projects">Global Projects / Industry Soln</el-dropdown-item>
                    <el-dropdown-item command = "Human Resource">Human Resource</el-dropdown-item>
                    <el-dropdown-item command = "HSSE">HSSE</el-dropdown-item>
                    <el-dropdown-item command = "Centre of Performance Excellence">Centre of Performance Excellence</el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
          </div>

          <div class = "reportgraph">
              <h3> Average Score by Question </h3>
              <p> Y axis : Mean Score of each question (Max score 5)
              <br>X axis : w_1_mean = Mean score of Wellbeing Qn 1 </p> <br>
              <column-chart :data="report_dataW" xtitle="Question" ytitle="Mean Score" min = '0' max='5'></column-chart>
          </div>

        </div>
    </html>
</template>

<script>

import {ref} from 'vue'
import {onMounted, onUnmounted} from 'vue'

export default {
    
  data() {
    return {
      data_filteredW: [],
      report_dataW: [],
      current_departmentW: 'Department'
    };
  },
  methods:{
    handleDepartment(command){
          this.current_departmentW = command
          let data_selectedW = []
          data_selectedW = this.data_filteredW.filter(data3 =>{
          return data3.department.includes(command)})
          const data_x = data_selectedW[0]["data_x"];
          const data_y = data_selectedW[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_dataW  = arr
          this.data_filteredW = data
        
          }
  },
  async mounted() {
    let data_W = await fetch ('http://127.0.0.1:8000/report/wellbeing');
    const data = await data_W.json()
    const data_selectedW = data.filter(data =>{
        return data.department.includes("HSSE")})
    this.data_filteredW = data
    const data_x = data_selectedW[0]["data_x"];
    const data_y = data_selectedW[0]["data_y"];
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseFloat(data_y[index])])
    });
    this.report_dataW  = arr
    }}
    

   

</script>


<style>


</style>