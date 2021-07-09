<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="5"/>
      <h1>Individual</h1>

</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import {ref} from 'vue'
export default {
    name: 'Individual',
    components: {Sidebar, TopNavigationBar}
  }

</script>


<style>



</style>