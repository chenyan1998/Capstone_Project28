<template>
<html>
<div class = "top-left2">
  
  <div class = "heading">
    <h3> Wellbeing Report</h3>
    <p class ="toppara"> Good health and wellbeing is a core enabler of employee engagement and organisational performance. </p>
  </div>

  <div id = "dropdown1">
    <el-dropdown>
      <el-button style="width:200px;">
        Survey Year<i class="el-icon-arrow-down el-icon--right"></i>
      </el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>2021</el-dropdown-item>
          <el-dropdown-item>2020</el-dropdown-item>
          <el-dropdown-item>2019</el-dropdown-item>
          <el-dropdown-item>2018</el-dropdown-item>
          <el-dropdown-item>2017</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>

  <div id = "dropdown2">
    <el-dropdown>
      <el-button style="width:200px;">
        Question Number<i class="el-icon-arrow-down el-icon--right"></i>
      </el-button>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item>Question 1</el-dropdown-item>
          <el-dropdown-item>Question 2</el-dropdown-item>
          <el-dropdown-item>Question 3</el-dropdown-item>
          <el-dropdown-item>Question 4</el-dropdown-item>
          <el-dropdown-item>Question 5</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>

  <div id = "dropdown3">
    <el-dropdown @command="handleDepartment">
      <el-button style="width:200px;">
        {{current_department}}<i class="el-icon-arrow-down el-icon--right"></i>
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
          <el-dropdown-item command = "CEO Office">CEO Office</el-dropdown-item>
          <el-dropdown-item command = "IT">IT </el-dropdown-item>
          <el-dropdown-item command = "Global Projects / Industry Soln">Global Projects / Industry Soln</el-dropdown-item>
          <el-dropdown-item command = "Human Resource">Human Resource</el-dropdown-item>
          <el-dropdown-item command = "HSSE">HSSE</el-dropdown-item>
          <el-dropdown-item command = "Centre of Performance Excellence">Centre of Performance Excellence</el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
  </div>

  <div class = "reportgraph">
    <p> Average Score by Question </p>
    <column-chart :data="report_data" xtitle="Question" ytitle="EEI Score" min = '0' max='5'></column-chart>
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
      data_filtered: [],
      report_data: [],
      current_department: 'Department'
    };
  },
  methods:{
    handleDepartment(command){
          this.current_department = command
          console.log(command)
          console.log('oops', this.data_filtered)
          let data_selected = []
          if (command == 'all'){
            console.log('all selected')
            data_selected = this.all
          } else{
            console.log('all unselected')
            data_selected = this.data_filtered.filter(data3 =>{
            return data3.department.includes(command)})
          }

          console.log('********',data_selected)
          const data_x = data_selected[0]["data_x"];
          const data_y = data_selected[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_data  = arr
          this.data_filtered = data_selected
        
          }
  },
  async mounted() {
    let data1 = await fetch ('http://127.0.0.1:8000/report/wellbeing');
    console.log(data1)
    const data = await data1.json()
    console.log('data',data)
    const data_selected = data.filter(data =>{
        return data.department.includes("HSSE")})
    console.log('data_selected',data_selected)
    this.data_filtered = data
    this.all = data
    const data_x = data_selected[0]["data_x"];
    const data_y = data_selected[0]["data_y"];
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseFloat(data_y[index])])
    
    });
    this.report_data  = arr
    }}
    

   

</script>


<style>

.graph1 {
  padding: 0 350px;
  text-align: left;
  margin-left: 350px;
}



.el-dropdown {
    vertical-align: top;
}

.el-dropdown + .el-dropdown {
    margin-left: 15px;
}
  
.el-icon-arrow-down {
    font-size: 12px;
 }

.el-dropdown-menu {
   max-height:200px;
   overflow:scroll; 
}

.toppara {
  text-align: center;
  padding-left: 50px;
  padding-right: 50px;
}

/* Report */
#dropdown1 {
  position: absolute;
  left : 30%; 
  }
#dropdown2 {
  position: absolute;
  left : 55%; 
  }
#dropdown3 {
  position: absolute;
  left : 80%; 
  }
#dropdown4 {
  position: absolute;
  left : 40%; 
  }
#dropdown5 {
  position: absolute;
  left : 70%; 
  }
#dropdown6 {
  position: absolute;
  left : 100%; 
  }
#dropdown7 {
  position: absolute;
  left : 25%; 
  }
#dropdown8 {
  position: absolute;
  left : 50%; 
  }
#dropdown9 {
  position: absolute;
  left : 75%; 
  }
  
</style>