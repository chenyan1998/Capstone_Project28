<template>
  <div>
      <TopNavigationBar/>
      <Sidebar :current_path="4"/>
      <div class = "top-left-individualdetails">
        <el-descriptions title="Employee Analysis" border>
          <el-descriptions-item label="Employee ID">{{round(employee.Employee_id)}}</el-descriptions-item>
          <el-descriptions-item label="EES Score">{{round(employee.EES_score)}}</el-descriptions-item>
          <el-descriptions-item label="Flight Risk Level">
            <el-tag v-if="employee.Flight_risk_label === 'Low Flight Risk'" size='small' type="success">
              Low
            </el-tag>
            <el-tag v-if="employee.Flight_risk_label === 'High Flight Risk'" size='small' type="danger">
              High
            </el-tag>
          </el-descriptions-item>
        </el-descriptions>
        <div>
          <apexchart type="radar" height="450" :options="chartOptions" :series="series"></apexchart>
        </div>
    
      </div>
  </div>
</template>
 
<script>
import VueApexCharts from "vue3-apexcharts";
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
export default {
    name: 'IndividualDetails',
    components: {Sidebar, TopNavigationBar, apexchart: VueApexCharts},
    props: ['Employee_id'],
    data() {
      return {
        employee: [],
        arr: [],
        series:[{
          name: 'Series 1',
          data: [100,100,100,100,100],
        }],
        chartOptions:{
          chart: {
            height: 1350,
            type: 'radar',
          },
          xaxis: {
            categories: ['EES_Score', 'Wellbeing', 'Core Values', 'Personality', 'Opinion']
          },
          yaxis: {
            min: 0,
            max: 100
          }
        }
      }
    },
    methods:{
      round(num){
        let truncated = num
        if (num !== undefined && num.length > 5) {
            truncated = truncated.substr(0,5);
        }
        return truncated
      }
    },
    async mounted() {
      let vm = this
      let employee_id = Math.floor(vm.Employee_id)
      let data = await fetch ('http://localhost:8000/report/individuals/' + employee_id)
      this.employee = await data.json()
      this.employee = this.employee[0]
      this.arr = [this.employee.EES_score.substr(0,5),
        this.employee.Wellbeing.substr(0,5), 
        this.employee.Core_values.substr(0,5), 
        this.employee.Personality.substr(0,5),
        this.employee.Opinion.substr(0,5)]
      this.series = [{
        name: 'Series 1',
        data: this.arr,
        }]
    },
}
</script>

<style>
.top-left-individualdetails {
  position: absolute;
  top : 10%;
  left: 18%;
  width: 78%;
  text-align: left;
}

.el-descriptions {font-family: Georgia; font-size : 24px}
</style>