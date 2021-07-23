<template>
<html>
  <Sidebar :current_path="6" />
  <div id="loginpage">
    <img id = "loginimage" src= "@/assets/login.jpeg" align="left" >
    <br>
    <br>
    <br>
    <br>
    <div id = "login1" align = "right">
        <img src= "@/assets/dbschenkerlogo2.png" id="logo">
        <div class="login">
              <h1>Login to Web App</h1>
              <div id = "login2" align = "middle">
                  <form method="post" action="">
                      <p><input type="text" name="login" value="" placeholder="Username or Email"></p>
                      <p><input type="password" name="password" value="" placeholder="Password"></p>
                        
                      <p class="remember_me">
                            <label>
                                <input type="checkbox" name="remember_me" id="remember_me">
                                Remember me on this computer
                            </label>
                      </p>
                      <div class = "nav" align ="right">
                            <router-link to ="/home"> Login </router-link>
                      </div>
                      <router-view/>
                    </form>
                    <br> 

                <p class="a" align="right"> Forgot your password?   <a href="#">
                    <div id = "nav2"> 
                      <router-link to ="/forgotpassword"> Click here to reset it. </router-link> 
                    </div>
                    </a>
                </p>
              </div>
        </div>
    </div>
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

#loginpage {
  height: 100%;
  width:100%
}
#loginimage {
  position : absolute;
  width : 70% ;
  height : 100%;
  left : 0%;
}

#login1{
  position: absolute;
  width : 30%;
  height: 100%;
  right : 0%;
}
#logo{
  position :relative;
  width : 70%;
  height :20%;
  right: 15%;
}

.login {
  position: relative;
  height: 35%;
  width: 100%;
  background: white;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

#login2{
  background: white;
}

.login h1 {
  font-size: 15px;
  font-weight: bold;
  color: #555;
  text-align: center;
  text-shadow: 0 1px white;
  background: #f3f3f3;
  border-bottom: 1px solid #cfcfcf;
  -webkit-box-shadow: 0 1px whitesmoke;
  box-shadow: 0 1px whitesmoke;
}

.login input[type=text], .login input[type=password] {
  position: relative;
  width: 70%;
  left: 0%
}

.login p.remember_me {
  margin-bottom: 5%;
  margin-left: 10%;
  float: left;
  line-height: 20%;
}

.login p.remember_me label {
  font-size: 70%;
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

.nav {
  padding : 1% 8%;
  width : 10%;
  margin-left:50%; 
  font-size: 90%;
  font-weight: bold;
  text-align: center;
  color: #685555;
  text-shadow: 0 1px #f1e3e3;
  background: #efcdcd;
  border: 1px solid;
  border-color: #ceb4b4 #c8b3b3 #c29e9e;
  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
}

.nav:active {
  background: #cde5ef;
  border-color: #9eb9c2 #b3c0c8 #b4ccce;
  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
}

.a {
  margin-right:10%;
  font-size: 11px;
  color: black;
  text-align: right;
  text-shadow: 0 1px darkgrey;
}

.a a:hover {
  text-decoration: underline;
  font-size :15;
}

#nav2 {
  color: #c73d3d;
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
  margin: 1%;
  padding: 0 5%;
  width: 80%;
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
