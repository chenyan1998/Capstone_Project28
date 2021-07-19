<template>
<html>
  
  <div class="NavBarRow">

    <div class="NavBarA">
      <div class="NavBarColumn">
        <img src = "@/assets/dbschenkerlogo.png" width ="170" height = "40">  
      </div>
    </div>

    <div class="NavBarB">
      <div class="NavBarColumn">
        <img src= "@/assets/avatar.png" alt="Avatar" class="avatar" width ="40" height = "40">
      </div>
    </div>

  </div>
  
</html>
</template>

<style>
div.NavBarA { text-align : left ;}
div.NavBarA img { margin-left : 15px;}
div.NavBarB { text-align : right ;}
div.NavBarB img { margin-right : 0px;}

.NavBarColumn {
  top: 0;
  left: 0;
  float: left;
  background:white ;
  width: 47.5%;
  padding: 8px;
  margin:0px ;
}
.NavBarRow::after {
  top: 0;
  right: 0;
  background:white ;
  content: "";
  clear: both;
  display: table;
  margin:0px ;
}
</style>