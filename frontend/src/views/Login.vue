<template>
  <div class="login">
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
  name: 'Login',
  setup(){
    const nav_list = ref(['Home','ForgotPassword'])
    return {nav_list}
  }
}
</script>

<style>

</style>