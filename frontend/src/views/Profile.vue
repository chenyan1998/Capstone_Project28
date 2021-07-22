<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="4" />
      <div class = "top-left-profile">
            <img  src= "@/assets/avatar.png" alt="Avatar" class="avatar1" width ="100" height = "100">
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

.top-left-profile {
  position: absolute;
  top : 15%;
  left: 20%;
  width: 75%;
  /* background: green; */
}

#profiletable {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  position: relative;
  left: 20%;
  text-align: left;
  border-spacing: 5px;
  width :70%;
  border: 0px solid white;
}

#profiletable td, th {
  text-align: left;
  padding: 10px;
}
</style>