<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="5" />
      <div class = "top-left-profile">
            <img  src= "@/assets/avatar.png" alt="Avatar" class="avatar1" width ="100" height = "100">
        <el-descriptions title="User Information" :column="4" width="100" border>
        <el-descriptions-item v-if="edit_status === true" label="ID" span="4">
          <el-input v-model="singleuser._id" :disabled="true"></el-input>
        </el-descriptions-item>
        <el-descriptions-item v-if="edit_status === false " label="ID" span="4">{{singleuser._id}}</el-descriptions-item>
        <el-descriptions-item v-if="edit_status === true" label="Name" span="4">
          <el-input v-model="singleuser.name"></el-input>
        </el-descriptions-item>
        <el-descriptions-item v-if="edit_status === false" label="Name" span="4">{{singleuser.name}}</el-descriptions-item>
        <el-descriptions-item v-if="edit_status === true" label="Department" span="4">
          <el-input v-model="singleuser.department"></el-input>
        </el-descriptions-item>
        <el-descriptions-item v-if="edit_status === false" label="Department" span="4">{{singleuser.department}}</el-descriptions-item>
        <el-descriptions-item v-if="edit_status === true" label="Email" span="4">
          <el-input v-model="singleuser.email"></el-input>
        </el-descriptions-item>
        <el-descriptions-item v-if="edit_status === false" label="Email" span="4">{{singleuser.email}}</el-descriptions-item>
        <el-descriptions-item v-if="edit_status === true" label="Password" span="4">
          <el-input v-model="singleuser.password" show-password></el-input>
        </el-descriptions-item>
        <el-descriptions-item v-if="edit_status === false" label="Password" span="4">******</el-descriptions-item>
        </el-descriptions>
        <el-button v-if="edit_status === false" type="danger" plain @click="handleEdit">Edit</el-button>
        <el-button v-if="edit_status === true" type="success" plain @click="handleSave">Save</el-button>
      </div>
</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import { ElNotification } from 'element-plus';
import {ref, h} from 'vue'
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
              console.log('singleuser:',singleuser.value)
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
          }
      load()
      let edit_status = ref(false)
      const handleEdit = () =>{
        edit_status.value = true
        console.log('handle Edit')
      }
      const handleSave = async () =>{
        
        console.log('handle Save')
        try{
              let data = await fetch ('http://localhost:8000/user/' + singleuser.value._id,
               {
                  method: "POST",
                  body: JSON.stringify(singleuser.value),
                  headers: {
                      "Content-type": "application/json; charset=UTF-8"
                  }
                })
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')
              }
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
        ElNotification({
        title: 'Saved!',
        message: h('i', { style: 'color: teal' }, 'Information Saved')
        });
        edit_status.value = false
      }
    return {singleuser, edit_status, handleEdit, handleSave, error}
  }
}
</script>


<style>

.top-left-profile {
  position: absolute;
  top : 15%;
  left: 20%;
  width: 75%;
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