<template>
  <html>
    <div class = "top-left-report">

      <div class = "heading">
          <h3> Core Values Report</h3>
          <p> DB Schenker's Core Values : 
          <br>1.  Play fair, be honest &nbsp;&nbsp;&nbsp; 2.  Be one team with one goal 
          <br>3.  Walk the talk &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.  Win together  
          <br>5.  Push limits   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6.  Take customers further </p>
      </div>

      <div id = "report-dropdown">
          <el-dropdown @command="handleDepartment">
            <el-button style="width:300px;">
              {{current_departmentC}}<i class="el-icon-arrow-down el-icon--right"></i>
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
          <column-chart :data="report_dataC" xtitle="Question" ytitle="Mean Score" min = '0' max='5'></column-chart>
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
      data_filteredC: [],
      report_dataC: [],
      current_departmentC: 'Department'
    };
  },
  methods:{
    handleDepartment(command){
          this.current_departmentC = command
          console.log(command)
          console.log('oops', this.data_filteredC)
          let data_selectedC = []
          if (command == 'all'){
            console.log('all selected')
            data_selectedC = this.all
          } else{
            console.log('all unselected')
            data_selectedC = this.data_filteredC.filter(data3 =>{
            return data3.department.includes(command)})
          }

          console.log('********',data_selectedC)
          const data_x = data_selectedC[0]["data_x"];
          const data_y = data_selectedC[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_dataC  = arr
          this.data_filteredC = data_selectedC
        
          }
  },
  async mounted() {
    let data_C = await fetch ('http://127.0.0.1:8000/report/coreValues');
    console.log(data_C)
    const data = await data_C.json()
    console.log('data',data)
    const data_selectedC = data.filter(data =>{
        return data.department.includes("HSSE")})
    console.log('data_selected',data_selectedC)
    this.data_filteredC = data
    this.all = data
    const data_x = data_selectedC[0]["data_x"];
    const data_y = data_selectedC[0]["data_y"];
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseFloat(data_y[index])])
    
    });
    this.report_dataC  = arr
    }}
    

   

</script>
<style>

</style>