<template>
  <div>
    <div v-if="currentFile" class="progress">
      <div
        class="progress-bar progress-bar-info progress-bar-striped"
        role="progressbar"
        :aria-valuenow="progress"
        aria-valuemin="0"
        aria-valuemax="100"
        :style="{ width: progress + '%' }"
      >
        {{ progress }}%
      </div>
    </div>
    <div class = "UF-1">
        <label  type="primary" class="btnbtn-default">
          <input size="small" width="5" class="file-prew" type="file" ref="file" @change="selectFile" />
        </label>

        <button style="position: absolute ;top: 39% ;right:5%; " size = "small" type="success" round class="btn btn-success" :disabled="!selectedFiles" @click="upload">
          Upload<i class="el-icon-upload el-icon--right"></i>
        </button>
    </div>
    <br />
    <div class="alertalert-light" role="alert">{{ message }}</div>
    
    
    
    <div class="UF-card">
      <div size="small" type="primary" class="UFcard-header">List of Files</div>
      <ul class="list-group list-group-flush">
        <li
          class="list-group-item"
          v-for="(file, index) in fileInfos"
          :key="index"
        >
          <a :href="file.url">{{ file.name }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import UploadService from "../services/UploadFilesService";

export default {
  name: "upload-files",
  data() {
    return {
      selectedFiles: undefined,
      currentFile: undefined,
      progress: 0,
      message: "",
      fileInfos: []

    };
  },
  methods: {
      selectFile() {
      this.selectedFiles = this.$refs.file.files;},
      upload() {
      this.progress = 0;

      this.currentFile = this.selectedFiles.item(0);
      UploadService.upload(this.currentFile, event => {
        this.progress = Math.round((100 * event.loaded) / event.total);
      })
        .then(response => {
          this.message = response.data.message;
          return UploadService.getFiles();
        })
        .then(files => {
          this.fileInfos = files.data;
        })
        .catch(() => {
          this.progress = 0;
          this.message = "Could not upload the file!";
          this.currentFile = undefined;
        });

      this.selectedFiles = undefined;
    },
    mounted() {
    UploadService.getFiles().then(response => {
      this.fileInfos = response.data;
    });}

  
  }
};
</script>

<style>
.UF-1{
  padding: 10px;
  width: 100%;
}

.UFcard-header {
  position: relative;
  width: 100%;
  left: 0%;
  border-radius: 5px;
  padding: 10px;
  border-style: solid;
  border-width: 0.05px;
  border-color:lightgray;
  overflow:visible;
  background-color: #D7DCE1;
}

.UF-card{

}


</style>