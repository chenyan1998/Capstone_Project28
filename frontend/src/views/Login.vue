<template>
<html>
  <Sidebar :current_path="4" />

  <img src= "@/assets/login.jpeg" class="loginbackground" width ="1050" height = "730" align = "left">
  <br>
  <br>
  <br>
  <br>
  <img src= "@/assets/dbschenkerlogo2.png" class="logo" width ="300" height = "180" align = "middle" top ="10">
  <div class="login">
    <div class="login">
      
  <h1>Login to Web App</h1>
  <form method="post" action="">
    <p><input type="text" name="login" value="" placeholder="Username or Email"></p>
    <p><input type="password" name="password" value="" placeholder="Password"></p>
    
    <p class="remember_me">
      <label>
        <input type="checkbox" name="remember_me" id="remember_me">
        Remember me on this computer
      </label>
  
    
    </p>
    
    <div id = "nav">
    <router-link to ="/home"> Login </router-link>
    </div>
    <router-view/>
   

  </form>
  
  <br> 
  </div>
  
 
  <p class="a"> Forgot your password?   <a href="#">
    
    <div id = "nav2"> 
      <router-link to ="/forgotpassword"> Click here to reset it. </router-link> 
    </div>
    </a>
  </p>

  </div>
  



  
</html>
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

#nav {
  padding: 0 30px;
  margin-right : 30px;
  margin-left : 1305px;
  height: 29px;
  font-size: 15px;
  font-weight: bold;
  text-align: center;
  color: #685555;
  text-shadow: 0 1px #f1e3e3;
  background: #efcdcd;
  border: 1px solid;
  border-color: #ceb4b4 #c8b3b3 #c29e9e;
  border-radius: 16px;
  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
}
#nav:active {
  background: #cde5ef;
  border-color: #9eb9c2 #b3c0c8 #b4ccce;
  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
}

#nav2 {
  color: #c73d3d;
  text-decoration: none;
  font-size :25;
}
#nav2:hover {
  text-decoration: underline;
  font-size :15;
}
.login {
  background: white;
  border-radius: 5px;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

.login:before {
  content: '';
  background: rgba(0, 0, 0, 0.08);
  border-radius: 4px;
}

.login h1 {
  font-size: 15px;
  font-weight: bold;
  color: #555;
  text-align: center;
  text-shadow: 0 1px white;
  background: #f3f3f3;
  border-bottom: 1px solid #cfcfcf;
  border-radius: 3px 3px 0 0;
  -webkit-box-shadow: 0 1px whitesmoke;
  box-shadow: 0 1px whitesmoke;
}

.login p:first-child {
  margin-top: 0;
}


.login input[type=text], .login input[type=password] {
  width: 278px;
}

.login p.remember_me {
  margin-bottom: 10px;
  margin-left: 20px;
  float: left;
  line-height: 40px;
}

.login p.remember_me label {
  font-size: 12px;
  color: #777;
  cursor: pointer;
}
.login p.remember_me input {
  position: relative;
  bottom: 1px;
  margin-right: 4px;
  vertical-align: middle;
}


.login p.submit {
  text-align: right;
}

.a {
  margin-right : 30px;
  font-size: 11px;
  color: black;
  text-align: right;
  text-shadow: 0 1px darkgrey;
}


.a a:hover {
  text-decoration: underline;
  font-size :15;
}

:-moz-placeholder {
  color: #c9c9c9 !important;
  font-size: 13px;
}

::-webkit-input-placeholder {
  color: #ccc;
  font-size: 13px;
}

input {
  font-family: 'Lucida Grande', Tahoma, Verdana, sans-serif;
  font-size: 14px;
}

input[type=text], input[type=password] {
  margin: 5px;
  padding: 0 10px;
  width: 200px;
  height: 34px;
  color: #404040;
  background: white;
  border: 1px solid;
  border-color: #c4c4c4 #d1d1d1 #d4d4d4;
  border-radius: 2px;
  outline: 5px solid #eff4f7;
  -moz-outline-radius: 3px;
  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
}

input[type=text]:focus, input[type=password]:focus {
  border-color: #020202;
  outline-color: #dceefc;
  outline-offset: 0;
}


.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
  line-height: 34px;
}
</style>
