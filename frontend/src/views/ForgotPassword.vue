<template>
<html>
<div class="container">
  <img src="@/assets/resetpassword.png" alt="Snow" style="width:100%;">
  <div class="centered">
    <h3>Note : If you continue, DB Schenker will send a link to your company email address. Click the link in the message, and enter a new password on the page that opens.
      </h3>
    <div class="resetpassword1">
  <form method="post" action="">
    <p><input type="text" name="login" value="" placeholder="Username or Email"></p>
    <br>
    <p class="submit"><input type="submit" name="commit" value="Reset Password"></p>
  </form>
  
  
  </div>
  
    <div id = "nav4">
    <router-link to ="/"> Back to Login Page </router-link>
    </div>
    <router-view/>
  </div>
</div>
</html>
</template>

<script>
export default {
    name: 'ForgotPassword'
}
</script>

<style>
.container {
  position: relative;
  text-align: center;
  color: white;
}
.top-left {
  position: absolute;
  top: 80px;
  left: 20px;
}

.top-left4 {
  position: absolute;
  top: 0px;
  left: 1000px;
  width : 180px;
}


.html {
  height: 100%;
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black;
}

.submit {
  text-align : right

}

#nav4 {
  text-align : right

}
</style>