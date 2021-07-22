<template>
  <div id="app">
    <div class="container" style="width:600px">
      <div class = "title" style="margin: 20px">
        <h3> DB Schenker Survey Results </h3>
        <h4> Upload Survey Results </h4>
      </div>

      <upload-files></upload-files>
    </div>
  </div>
</template>

<script>
import UploadFiles from "../components/UploadFiles_tem";

export default {
  name: "App",
  components: {
    UploadFiles
  }
};
</script>

<style>
.container  {
  background-color: hsla(50, 33%, 25%, .75);
	border-radius: 20px;
	width: 300px;
	height: 300px;
	margin: auto;
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
}


</style>