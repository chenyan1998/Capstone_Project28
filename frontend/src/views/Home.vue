<template>
  <div class="home">
    <div v-for="nav in nav_list" :key="nav">
      <router-link :to="{name: nav}">
            <button>{{nav}}</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue'
export default {
  name: 'Home',
  setup(){
    const nav_list = ref(['ReportHomepage','SurveyHomepage'])
    console.log(nav_list.value)
    return {nav_list}
  }
}
</script>
