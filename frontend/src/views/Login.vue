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
        <img id="logo" src= "@/assets/dbschenkerlogo2.png">
        <div class="loginpageright">
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
                      <div class = "loginnav" align ="right">
                            <router-link to ="/home" style="color: #5a4949"> Login </router-link>
                      </div>
                      <router-view/>
                    </form>
                    <br> 

                <font class="forgotpasswordbutton" align="right"> Forgot your password?
                    <div id = "loginnav2"> 
                      <router-link to ="/forgotpassword" style="color: #c73d3d"> Click here to reset it. </router-link> 
                    </div>
                </font>
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
  max-height: 100%;
  width : 100%;
  overflow: hidden
}
#loginimage {
  position : absolute;
  width : 70%;
  height : 100%;
  left : 0%;
}

#login1{
  position: absolute;
  top: 0%;
  width : 30%;
  height: 100%;
  right : 0%;
  background-color: #F0F3F5;
}
#logo{
  position :absolute;
  top:15%;
  width : 70%;
  height :20%;
  right: 15%;
}

.loginpageright {
  position: absolute;
  top:38%;
  height: 35%;
  width: 100%;
  background: white;
  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
}

#login2{
  background: white;
}

.loginpageright h1 {
  font-size: 15px;
  font-weight: bold;
  color: #555;
  text-align: center;
  text-shadow: 0 1px white;
  background: #D7DCE1;
  border-bottom: 1px solid #cfcfcf;
  -webkit-box-shadow: 0 1px whitesmoke;
  box-shadow: 0 1px whitesmoke;
}

.loginpageright input[type=text], .loginpageright input[type=password] {
  position: relative;
  width: 70%;
  left: 0%
}

.loginpageright p.remember_me {
  margin-bottom: 5%;
  margin-left: 10%;
  float: left;
  line-height: 20%;
}

.loginpageright p.remember_me label {
  font-size: 11px;
  color: #777;
  cursor: pointer;
}
.loginpageright p.remember_me input {
  position: relative;
  bottom: 1px;
  margin-right: 4px;
  vertical-align: middle;
}

.loginpageright p.submit {
  text-align: right;
}

.loginnav {
  padding : 1% 5%;
  width :20%;
  margin-left:50%; 
  font-size: 14px;
  font-family: Georgia;
  font-weight: bold;
  text-align: center;
  text-shadow: 0 1px #f1e3e3;
  background: #efcdcd;
  border: 1px solid;
  border-color: #ceb4b4 #c8b3b3 #c29e9e;
  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
  display: inline;
}

.loginnav:active {
  background: #cde5ef;
  border-color: #9eb9c2 #b3c0c8 #b4ccce;
  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
}

.forgotpasswordbutton {
  font-size: 11px;
  color: black;
  text-align: right;
  font-family: Georgia;

}

.forgotpasswordbutton :hover {
  text-decoration: underline;
  font-size :15;
}

#loginnav2 {
  text-decoration: underline;
  font-size :15;
  display: inline;
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
