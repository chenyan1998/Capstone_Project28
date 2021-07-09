<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="4" />
<img  src= "@/assets/avatar.png" alt="Avatar" class="avatar1" width ="100" height = "100">
<div class = "top-left3">
  <div class = "heading">
  <h3> Personal Information </h3>
   <table id ="profiletable">
  <tr>
    <th>ID</th>
    <td>{{singleuser._id}}</td>
  </tr>
  <tr>
    <th>Name</th>
    <td>{{singleuser.name}}</td>
  </tr>
  <tr>
    <th>Department</th>
    <td>{{singleuser.department}}</td>
  </tr>
  <tr>
    <th>Email</th>
    <td>{{singleuser.email}}</td>
  </tr>
  
  </table>
  </div>

  </div>

</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import {ref} from 'vue'
export default {

    name: 'Profile',
    components: {Sidebar, TopNavigationBar},
    setup(){
      const singleuser = ref ([])
      const error = ref (null)
      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/user/60bdb77c4b2ec88180c75d54')
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')
              }
              singleuser.value = await data.json()
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
          }
      load()
    return {singleuser, error}
  }
}
</script>


<style>
#profiletable {
  font-family: arial, sans-serif;
  border-collapse: collapse;

  position: absolute;
  top: 80px;
  left: 350px;
  text-align: left;
  border-spacing: 5px;
  width :100%
}

#profiletable td, th {
  border: 1px solid #F0F3F5;
  text-align: left;
  padding: 8px;
}
.top-left3 {
  position: absolute;
  top: 230px;
  left: 20px;
}
img.avatar1{
    position : absolute;
    top: 100px;
}
</style>