<template>
<html>
<div class = "top-left">
  <div class = "heading">
  <h3> Wellbeing Report</h3>
  <p class ="toppara"> Good health and wellbeing is a core enabler of employee engagement and organisational performance. </p>
  </div>
<div id = "e1">
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
<div id = "e2">
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
<div id = "e3">
<el-dropdown>
  <el-button style="width:200px;">
    Department<i class="el-icon-arrow-down el-icon--right"></i>
  </el-button>
  <template #dropdown>
    <el-dropdown-menu>
      <el-dropdown-item>Air Freight Division</el-dropdown-item>
      <el-dropdown-item>Ocean Freight Division</el-dropdown-item>
      <el-dropdown-item>Finance</el-dropdown-item>
      <el-dropdown-item>Sales and Sales Planning</el-dropdown-item>
      <el-dropdown-item>Contract Logistics/SCM</el-dropdown-item>
      <el-dropdown-item>Fairs, Exhibitions, Events</el-dropdown-item>
      <el-dropdown-item>CEO Office</el-dropdown-item>
      <el-dropdown-item>IT </el-dropdown-item>
      <el-dropdown-item>Global Projects / Industry Soln</el-dropdown-item>
      <el-dropdown-item>Human Resource</el-dropdown-item>
      <el-dropdown-item>HSSE</el-dropdown-item>
      <el-dropdown-item>Centre of Performance Excellence</el-dropdown-item>
    </el-dropdown-menu>
  </template>
</el-dropdown>
</div>



<div class = "graph1">
<div class = "top-left2">
<p> Average Score by Question </p>
<!-- <column-chart :data="[['Qn 1', 3.97], ['Qn 2', 3.98], ['Qn 3', 3.9], ['Qn 4', 3.78],['Qn 5', 3.68],['Qn 6', 3.71],['Qn 7', 3.72]] " width= "900px" height= "400px" min="3" :max="4"></column-chart> -->

<column-chart :data="report_data"></column-chart>


</div>
</div>
</div>

</html>
</template>

<script>

import {ref} from 'vue'

  // export default {
  //   methods: {
  //     handleClick() {
  //       alert('button click');
  //     }, 
  //   },

  //   setup(){
  //   const wellbeingmetrics = ref([])
  //   const error = ref (null)
  //   const data_x = ref([])
  //   const data_y = ref([])
  //   const report_data = ref([])
  //   const load = async () =>{
  //       try{
  //           let data = await fetch ('http://127.0.0.1:8000/report/wellbeing')
  //           if (!data.ok){
  //               throw Error('no data available')
  //           }
  //           wellbeingmetrics.value = await data.json()
  //           // console.log(wellbeingmetrics.value[0]['data_x'])
  //           const data_x = wellbeingmetrics.value[0]['data_x']
  //           const data_y = wellbeingmetrics.value[0]['data_y']
  //           // console.log('datax',data_x)
  //           data_x.forEach((element, index) => {report_data.value.push([element, parseInt(data_y[index])])})
  //           // console.log(report_data.value)
  //       }
  //           catch (err){
  //               error.value = err.message
  //               console.log (error.value)
  //           }
  //       }
  //   load()
  //   // let currentreport = wellbeingmetrics.value
  //   // const data_x = wellbeingmetrics.value[0]['data_x']
  //   // const data_y = ref(wellbeingmetrics.value[0]['data_y'])
  //   console.log('report is', report_data.value)
  //   return {report_data, error}
  // }

      
  // }

  export default {
    
  data() {
    return {
      report_data: [],
    };
  },
  async mounted() {
    console.log("hello");
    let data1 = await fetch ('http://127.0.0.1:8000/report/wellbeing');
    console.log("hello2");
    const data = await data1.json()
    const data_x = data[1]["data_x"];
    const data_y = data[1]["data_y"];
    console.log("datax", data_x);
    console.log("datay", data_y);
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseInt(data_y[index])])
    
    });
    this.report_data  = arr
    console.log(report_data)
  },
};


</script>


<style>

.graph1 {
  padding: 0 350px;
  text-align: left;
  margin-left: 350px;
}

.heading h3 {
  padding: 0 350px;
  text-align: left;
}
.heading p {
  padding-left :350px;
  padding-right : 100px;
  text-align: left;
}
.div container1{
  width: 300px;
  height: 100px;
  padding: 50px;
  border: 1px solid red;
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

#e1 {padding-left : 350px; float:left;}
#e2 {padding-left : 150px; float:left;}
#e3 {padding-left : 150px; float:left;}
#e4 {padding-left : 400px; float:left;}
#e5 {float:middle;}
#e6 {padding-left : 350px; float:left;}
#e8 {float :right;padding-top: 200px;}
  
</style>