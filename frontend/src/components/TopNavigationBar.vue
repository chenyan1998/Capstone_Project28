<template>
 <html>
  
  <div class="row">

    <div class="a">
      <div class="column">
      <img src = "@/assets/dbschenkerlogo.png" width ="150" height = "30">  
    </div>
    </div>

    <div class="b">
      <div class="column">
      <img src= "@/assets/avatar.png" alt="Avatar" class="avatar" width ="30" height = "30">
    </div>
    </div>
  </div>
  
  </html>
</template>

<style>
div.a { text-align : left ;}
div.a img { margin-left : 10px;}
div.b { text-align : right ;}
div.b img { margin-right : 0px;}
.column {
  top: 0;
  left: 0;
  float: left;
  background:white ;
  width: 49.8%;
  padding: 5px;
  margin:0px ;
}
.row::after {
  top: 0;
  right: 0;
  background:white ;
  content: "";
  clear: both;
  display: table;
  margin:0px ;
}
</style>