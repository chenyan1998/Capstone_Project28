<template>
<html>
  
  <div class="NavBarRow">

    <div class="NavBarA">
      <div class="NavBarColumn">
        <img src = "@/assets/dbschenkerlogo.png" id ="NavBarimg1">  
      </div>
    </div>

    <div class="NavBarB">
      <div class="NavBarColumn">
        <router-link :to="{name: 'Profile'}">
                <img src= "@/assets/avatar.png" id ="NavBarimg2">
            </router-link>  
       
      </div>
    </div>

  </div>
  
</html>
</template>


<style>
div.NavBarA { text-align : left ;}
div.NavBarA img { margin-left : 15px;}
div.NavBarB { text-align : right ;}
div.NavBarB img { margin-right : 10px;}

#NavBarimg1{
  width : 25%;
}

#NavBarimg2{
  width: 5%;
}
.NavBarColumn {
  top: 0;
  left: 0;
  float: left;
  background:white ;
  width: 50%;
  padding: 5px;
  margin:0px ;
}
.NavBarRow {
  top: 0;
  right: 0;
  background:white ;
  content: "";
  clear: both;
  display: table;
  margin: 0px ;
  height: 10%;
  width: 100%;
}
</style>