<template>
<html>
  <div class="forgotpasswordcontainer">
      <div class="forgotpasswordcentered">
        <h4>Note : If you continue, DB Schenker will send a link to your company email address. Click the link in the message, and enter a new password on the page that opens.</h4>
        <div class="resetpassword1">
          <form class = "forgotpasswordform" method="post" action="">
            <p><input type="text" name="login" value="" placeholder="Username or Email"></p>
            <br>
            <p class="forgotpasswordsubmit"><input type="submit" name="commit" value="Reset Password" style="font-family: Georgia; font-size: 14px;"></p>
          </form>
        </div>
    
        <div id = "forgotpasswordnav">
          <router-link to ="/" style="font-family: Georgia; font-size: 14px; "> Back to Login Page </router-link>
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
.forgotpasswordcontainer {
  position: absolute;
  width: 100%;
  height:100%;
  background-image: linear-gradient(to bottom right, #167D86, #CAE7EA);
  text-align: center;
  color: white;
}

.forgotpasswordcentered {
  position: absolute;
  top: 50%;
  left: 50%;
  background-color: #F0F3F5;
  padding: 3% 10%;
  transform: translate(-50%, -50%);
  border-style: outset;
  border-width: 5px;
  color: black;
}

.forgotpasswordsubmit {
  text-align : right;
}

#forgotpasswordnav {
  text-align : right;
}
</style>