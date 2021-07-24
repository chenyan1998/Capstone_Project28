<template>
  <html>
      <div class = "report-top-left">
        <div class="reportleft">
            <div class = "reportheading">
              <h3> Opinion Report</h3>
              <p> Employees' opinions helps us in finding problems in workforce, whether it's a problem with other employees or ones the employee themselves has.   </p>
            </div>

            <div class = "report-dropdown">
              <el-dropdown @command="handleDepartment">
                <el-button style="width:300px;">
                  {{current_departmentO}}<i class="el-icon-arrow-down el-icon--right"></i>
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
                <br>X axis : o_1_mean = Mean score of Opinion Qn 1 </p> <br>
                <column-chart :data="report_dataO" xtitle="Question" ytitle="Mean Score" min = '0' max='5'></column-chart>
            </div>
        </div>
        <div class="reportright">
          <h3 class="reportrighth3"> List of Opinions and Emotion Survey Questions</h3>
          <div class="reportline"></div>
          <br>
              <h4> Question 1 </h4>
              <p>I am developing the necessary skills to achieve my career goals   </p>

              <h4> Question 2 </h4>
              <p>I feel a sense of belonging to my work community   </p>

              <h4> Question 3 </h4>
              <p>I always have positive thoughts, and I feel that I am getting what I want out of my job   </p>

              <h4> Question 4 </h4>
              <p>Feedback we get from our work is used to improve operations more than to criticise people   </p>

              <h4> Question 5 </h4>
              <p>Higher ups in my department and the company take our opinions seriously   </p>
        
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
      All:[],
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
          data_selectedO = this.data_filteredO.filter(data3 =>{
          return data3.department.includes(command)})
          

          console.log('********',data_selectedO)
          const data_x = data_selectedO[0]["data_x"];
          const data_y = data_selectedO[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_dataO  = arr
          this.data_filteredO = data
        
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
    this.All = data
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