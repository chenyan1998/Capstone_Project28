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

    <label  type="primary" class="btnbtn-default">
      <input size="small" width="5" background-color= "lightblue" class="file-prew" type="file" ref="file" @change="selectFile" />
    </label>

    <button style="margin-left: 160px;" size = "small" type="success" round class="btn btn-success" :disabled="!selectedFiles" @click="upload">
      Upload<i class="el-icon-upload el-icon--right"></i>
    </button>

    <br />
    <div class="alertalert-light" role="alert">{{ message }}</div>
    <br />
    <br />
    
    <div class="card">
      <div size="small" type="primary" class="card-header">List of Files</div>
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
.card-header {
    background-color: rgb(94, 54, 54);
    border-radius: 90px;
}


</style>