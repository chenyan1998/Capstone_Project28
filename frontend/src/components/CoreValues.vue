<template>
  <html>
    <div class = "report-top-left">
      <div class="reportleft">
          <div class = "reportheading">
              <h3> Core Values Report</h3>
              <p> DB Schenker's Core Values : </p>

              <table id="corevaluetable" style="font-family: Georgia; font-size: 14px;">
                <tr>
                  <td>1.  Play fair, be honest</td>
                  <td>2.  Be one team with one goal</td>
                  <td>3.  Walk the talk</td>
                </tr>
                <tr>
                  <td>4.  Win together</td>
                  <td>5.  Push limits </td>
                  <td>6.  Take customers further</td>
                </tr>
              
              </table>
          </div>
          <br>

          <div class = "report-dropdown">
              <el-dropdown @command="handleDepartment">
                <el-button style="width:300px;">
                  {{current_departmentC}}<i class="el-icon-arrow-down el-icon--right"></i>
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
              <br>X axis : c_1_mean = Mean score of CoreValues Qn 1 </p> <br>
              <column-chart :data="report_dataC" xtitle="Question" ytitle="Mean Score" min = '0' max='5'></column-chart>
          </div>
      </div>

      <div class="reportright">
        <h3 class="reportrighth3"> List of Core Values Survey Questions</h3>
        <div class="reportline"></div>
        <br>
              <h4> Question 1 </h4>
              <p>I feel that I am supported and respected at work   </p>

              <h4> Question 2 </h4>
              <p>In the work environment, me and my team cooperate well with good teamwork  </p>

              <h4> Question 3 </h4>
              <p>In my work area/team, we all take personal responsibility   </p>

              <h4> Question 4 </h4>
              <p>In my company, we share knowledge across working areas   </p>

              <h4> Question 5 </h4>
              <p>In my work area/team, we continuously challenge the status quo   </p>

              <h4> Question 6 </h4>
              <p>In my work area/team, we make decisions with a focus on our customers   </p>

      </div>

    </div>
  </html>
</template>


<script>
export default {
  data() {
    return {
      All:[],
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
          data_selectedC = this.data_filteredC.filter(data3 =>{
          return data3.department.includes(command)})
          

          console.log('********',data_selectedC)
          const data_x = data_selectedC[0]["data_x"];
          const data_y = data_selectedC[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_dataC  = arr
          this.data_filteredC = data
        
          }
  },
  async mounted() {
    let data_C = await fetch ('http://127.0.0.1:8000/report/coreValues');
    console.log(data_C)
    const data = await data_C.json()
    console.log('data',data)
    const data_selectedC = data.filter(data =>{
        return data.department.includes("All")})
    console.log('data_selected',data_selectedC)
    this.data_filteredC = data
    this.All = data
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
#corevaluetable td{
  padding: 0px 50px 0px 0px;
  border-collapse: collapse
}
</style>