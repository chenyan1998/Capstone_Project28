<template>
  <html>
    <TopNavigationBar/>
    <body>
      <div id="container">
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
    // This page is a detailed report page.
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
html {
	height: 100%;
}

body {
	margin: 0;
	height: 100%;
  background: rgb(240, 243, 245);
}

#container {
	height: 100%;
}

#sidebar {
	vertical-align: top;
	height: 100%;
	overflow: auto;
}

#content {
	vertical-align: top;
	height: 100%;
	overflow: auto;
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

.reportgraph {
  position: relative;
  top: 50px;
  left: 350px;
  text-align: left;
  width: 500px;
}


</style>