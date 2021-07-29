<template>
    <html>
        <div class = "report-top-left">
          <div class="reportleft">
              <div class = "reportheading">
                  <h3> Wellbeing Report</h3>
                  <p> Good health and wellbeing is a core enabler of employee engagement and organisational performance. </p>
              </div>

              <div class = "report-dropdown">
                  <el-dropdown @command="handleDepartment">
                    <el-button style="width:300px;">
                      {{current_departmentW}}<i class="el-icon-arrow-down el-icon--right"></i>
                    </el-button>
                    <template #dropdown>
                      <el-dropdown-menu>
                        <el-dropdown-item command = "All">All</el-dropdown-item>
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
          <div class="reportright">
            <h3 class="reportrighth3"> List of Wellbeing Survey Questions</h3>
            <div class="reportline"></div>
            <br>
              <h4> Question 1 </h4>
              <p>I am emotionally strong and resilient whereby I can bounce back after a disappointment or problem </p>

              <h4> Question 2 </h4>
              <p>I am in a comfortable environment (work and home) and I contribute towards making my environment a safer and healthier place</p>

              <h4> Question 3 </h4>
              <p>I can critically consider the opinions and information presented by others and provide constructive feedback   </p>

              <h4> Question 4 </h4>
              <p>I feel capable of making important decisions  </p>

              <h4> Question 5 </h4>
              <p>I get personal satisfaction and enrichment from my current work   </p>

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
      current_departmentW: 'Department',
      All:[],
    };
  },
  methods:{
    handleDepartment(command){
          this.current_departmentW = command
          let data_selectedW = []
          data_selectedW = this.data_filteredW.filter(data3 =>{
            return data3.department.includes(command)})

          // data_selectedW = this.data_filteredW.filter(data3 =>{
          // return data3.department.includes(command)})
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
        return data.department.includes("All")})
    this.data_filteredW = data
    this.All = data
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