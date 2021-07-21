<template>
  <html>
      <div class = "top-left-report">
        
          <div class = "heading">
            <h3> Opinion Report</h3>
            <p> Employees' opinions helps us in finding problems in workforce, whether it's a problem with other employees or ones the employee themselves has.   </p>
          </div>

          <div id = "report-dropdown">
            <el-dropdown @command="handleDepartment">
              <el-button style="width:300px;">
                {{current_departmentO}}<i class="el-icon-arrow-down el-icon--right"></i>
              </el-button>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item command = "all">All</el-dropdown-item>
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
              <p> Average Score by Question </p>
              <column-chart :data="report_dataO" xtitle="Question" ytitle="Mean Score" min = '0' max='5'></column-chart>
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
      all:[],
      data_filteredO: [],
      report_dataO: [],
      current_departmentO: 'Department'
    };
  },
  methods:{
    handleDepartment(command){
          this.current_departmentO = command
          console.log(command)
          console.log('oops', this.data_filteredO)
          let data_selectedO = []
          if (command == 'all'){
            console.log('all selected')
            data_selectedO = this.all
          } else{
            console.log('all unselected')
            data_selectedO = this.data_filteredO.filter(data3 =>{
            return data3.department.includes(command)})
          }

          console.log('********',data_selectedO)
          const data_x = data_selectedO[0]["data_x"];
          const data_y = data_selectedO[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_dataO  = arr
          this.data_filteredO = data_selectedO
        
          }
  },
  async mounted() {
    let data_O = await fetch ('http://127.0.0.1:8000/report/opinion');
    console.log(data_O)
    const data = await data_O.json()
    console.log('data',data)
    const data_selectedO = data.filter(data =>{
        return data.department.includes("HSSE")})
    console.log('data_selected',data_selectedO)
    this.data_filteredO = data
    this.all = data
    const data_x = data_selectedO[0]["data_x"];
    const data_y = data_selectedO[0]["data_y"];
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseFloat(data_y[index])])
    
    });
    this.report_dataO  = arr
    }}
    

   

</script>



<style>

</style>