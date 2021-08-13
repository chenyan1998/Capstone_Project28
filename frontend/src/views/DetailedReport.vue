<template>
  <html>
    <TopNavigationBar/>
    <body>
      <div id="detailedreportcontainer">
        <div id="sidebar">
          <Sidebar />
          <Wellbeing v-if="report_type === 'Wellbeing'" />
          <CoreValues v-if="report_type === 'CoreValues'" />
          <Personality v-if="report_type === 'Personality'" />
          <Opinion v-if="report_type === 'Opinion'" />
        </div>
      </div>
    </body>
  </html>
</template>

<script>
import Wellbeing from '../components/Wellbeing.vue'
import CoreValues from '../components/CoreValues.vue'
import Personality from '../components/Personality.vue'
import Opinion from '../components/Opinion.vue'
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import { onMounted, onUnmounted } from 'vue'

export default {
    name: 'DetailedReport' ,
    components: { Wellbeing, CoreValues, Personality, Opinion, Sidebar ,TopNavigationBar},
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
body {
	margin: 0;
	height: 100%;
  background: rgb(240, 243, 245);
}
#detailedreportcontainer {
	height: 100%;
}
.reportheading {
  position: relative;
  top: 10%;
  left: 5%;
  text-align: left;
}
.reportheading p {
  width: 90%
}
.report-top-left {
  position: absolute;
  top : 10%;
  left: 18%;
  text-align:left;
  width: 82%;

  /* background: green; */
}
.report-dropdown {
  position: relative;
  left: 5%
}
.reportgraph {
  position: relative;
  top: 30px;
  left: 5%;
  text-align: left;
  width: 90%;
}
.reportleft {
  width: 70%;
  float: left;
}
.reportright {
  position: absolute;
  width: 26%;
  float: left;
  left: 70%;
  top: 5%;
  background-color:#F0F3F5;
  border-color: #646973;
  border-style:solid;
  border-width: 2px;
  padding: 5px;
  max-height: 90%;
  overflow: scroll
}
.reportrighth3{
  font-size: 18px;
  text-align: center;
}
.reportline{
  background:#646973;
	width:90%;
	height:2px;
	position:relative;
	float:left;
  left: 5%
}
.el-dropdown {
   vertical-align: top;
   font-family: Georgia; 
   font-size: 14px;
}
.el-icon-arrow-down {
   font-size: 14px;
}
.el-dropdown-menu {
   max-height: 200px;
   overflow: scroll; 
}


</style>