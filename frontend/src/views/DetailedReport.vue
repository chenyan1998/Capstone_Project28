<template>
  <el-row>
      <el-col :span="4"><h5>menu</h5><Sidebar/></el-col>  
      <el-col :span="12">
        <Wellbeing v-if="report_type === 'Wellbeing'" />
        <CoreValues v-if="report_type === 'CoreValues'" />
        <Personality v-if="report_type === 'Personality'" />
        <Opinion v-if="report_type === 'Opinion'" />
      </el-col>
  </el-row>
</template>

<script>
import Wellbeing from '../components/Wellbeing.vue'
import CoreValues from '../components/CoreValues.vue'
import Personality from '../components/Personality.vue'
import Opinion from '../components/Opinion.vue'
import Sidebar from '../components/Sidebar'
import { onMounted, onUnmounted } from 'vue'

export default {
    // This page is a detailed report page.
    name: 'DetailedReport' ,
    components: { Wellbeing, CoreValues, Personality, Opinion, Sidebar},
    created() {
       this.report_type = this.$route.params.report_type;     
    },
    beforeUpdate(){
      this.report_type = this.$route.params.report_type;
    },
    setup(){
      onMounted(()=>{
            console.log('component mounted')
        })
      onUnmounted(()=>{
            console.log('component unmounted')
        })
    }

}
</script>

<style>

</style>