<template>
  <html>
      <div class = "report-top-left">
        <div class="reportleft">
          <div class = "reportheading">
              <h3> Personality Report </h3>
              <p> Understanding personality help to build our leadership style, to resolve conflicts more effectively, to communicate more effectively, to understand how others make decisions and to retain key staff. </p>
          </div>

          <div class = "report-dropdown">
            <el-dropdown @command="handleDepartment">
              <el-button style="width:300px;">
                {{current_departmentP}}<i class="el-icon-arrow-down el-icon--right"></i>
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
                <br>X axis : p_1n_mean = Mean score of Personality Qn 1 
                <br>n stands for questions to identify neurotism, and a stands for questions to identify agreeableness</p> 
                
                <br>
              <column-chart :data="report_dataP" xtitle="Question" ytitle="Mean Score" min = '0' max='5'></column-chart>
          </div>
        </div>
        <div class="reportright">
          <h3 class="reportrighth3"> List of Personality Survey Questions</h3>
          <div class="reportline"></div>
          <br>
              <h4> Question 1 </h4>
              <p>I tend to be easily bordered by surrounding things that are happening   </p>

              <h4> Question 2 </h4>
              <p>I will get stressed out easily with external pressure   </p>

              <h4> Question 3 </h4>
              <p>I am afraid that I will make mistakes at all times   </p>

              <h4> Question 4 </h4>
              <p>I often feel blue   </p>

              <h4> Question 5 </h4>
              <p>I always trust others at work   </p>

              <h4> Question 6 </h4>
              <p>I value cooperation over competition   </p>

              <h4> Question 7 </h4>
              <p>I always respect others for who they are   </p>
        </div>

      </div> 
  </html>
</template>

<script>
export default {
    
  data() {
    return {
      All:[],
      data_filteredP: [],
      report_dataP: [],
      current_departmentP: 'Department'
    };
  },
  methods:{
    handleDepartment(command){
          this.current_departmentP = command
          console.log(command)
          console.log('oops', this.data_filteredP)
          let data_selectedP = []
          data_selectedP = this.data_filteredP.filter(data3 =>{
          return data3.department.includes(command)})
          

          console.log('********',data_selectedP)
          const data_x = data_selectedP[0]["data_x"];
          const data_y = data_selectedP[0]["data_y"];
          let arr = [];
          data_x.forEach((element, index) => {
            arr.push([element, parseFloat(data_y[index])])
          
          });
          this.report_dataP  = arr
          this.data_filteredP = data
        
          }
  },
  async mounted() {
    let data_P = await fetch ('http://127.0.0.1:8000/report/personality');
    console.log(data_P)
    const data = await data_P.json()
    console.log('data',data)
    const data_selectedP = data.filter(data =>{
        return data.department.includes("All")})
    console.log('data_selected',data_selectedP)
    this.data_filteredP = data
    this.All = data
    const data_x = data_selectedP[0]["data_x"];
    const data_y = data_selectedP[0]["data_y"];
    let arr = [];
    data_x.forEach((element, index) => {
      arr.push([element, parseFloat(data_y[index])])
    
    });
    this.report_dataP  = arr
    }}
    
</script>

<style>

</style>