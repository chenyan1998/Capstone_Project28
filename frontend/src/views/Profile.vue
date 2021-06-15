<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="3" />
<img  src= "@/assets/avatar.png" alt="Avatar" class="avatar1" width ="100" height = "100">
<div class = "top-left3">
  <div class = "heading">
  <h3> Personal Information </h3>
   <table id ="profiletable">
  <tr>
    <th>Name</th>
    <td>Robert E. Lee</td>
  </tr>
  <tr>
    <th>Position</th>
    <td>Senior Manager</td>
  </tr>
  <tr>
    <th>Email</th>
    <td>robert.lee@mail.dbshcenker.com</td>
  </tr>
  <tr>
    <th>Phone Number</th>
    <td>+65 91234567</td>
  </tr>
   <tr>
    <th>Address</th>
    <td>Blk 321 Beta Road #06-679 Singapore 654321 </td>
  </tr>
  
  </table>
  </div>

  </div>

</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
export default {

    name: 'Profile',
    components: {Sidebar, TopNavigationBar}
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