<template>
  <div>
	  <el-upload drag
	       :limit=limitNum
	       :auto-upload="false"
	       accept=".xlsx"
	       :action="UploadUrl()"
	       :before-upload="beforeUploadFile"
	       :on-change="fileChange"
	       :on-exceed="exceedFile"
	       :on-success="handleSuccess"
	       :on-error="handleError"
	       :file-list="fileList">
	    <i class="el-icon-upload"></i>
	    <div class="el-upload__text">Please drag a file to here ，or <em> click upload button </em></div>
	    <div class="el-upload__tip"  >only allowed to upload xlsx document, the size should be less than 100M </div>
  	</el-upload>
  <br/>
  <el-button size="small" type="primary" @click="uploadFile">Upload File </el-button>
  <el-button size="small"> Cancel </el-button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        limitNum: 1,  // The number of files that allowed to upload at the same time
        fileList: [],   // excel file list 
      }
    },
    methods:{
      // If the number of file exceeds the limits 
      exceedFile(files, fileList) {
        this.$message.warning(`We can only chose  ${this.limitNum} files，you chose  ${files.length + fileList.length} files currently`);
      },
      // If the state of file changes
      fileChange(file, fileList) {
        console.log(file.raw);
        this.fileList.push(file.raw) ;
        console.log(this.fileList);
      },
      // Only allowed to upload xlsx file 
      beforeUploadFile(file) {
        console.log('before upload');
        console.log(file);
        let extension = file.name.substring(file.name.lastIndexOf('.')+1);
        let size = file.size / 1024 / 1024;
        if(extension !== 'xlsx') {
          this.$message.warning('only can upload xlsx file ');
        }
        if(size > 10) {
          this.$message.warning('The size of file cannot exceed 10M');
        }
      },
      // If the file upload successfully 
      handleSuccess(res, file, fileList) {
        this.$message.success(' Upload successsfully ! ');
      },
      // If the file upload fail
      handleError(err, file, fileList) {
        this.$message.error('Upload Failure !!');
      },
      UploadUrl:function(){
       // 因为action参数是必填项，我们使用二次确认进行文件上传时，直接填上传文件的url会因为没有参数导致api报404，所以这里将action设置为一个返回为空的方法就行，避免抛错
        return ""
      },
      uploadFile() {
        if (this.fileList.length === 0){
          this.$message.warning('Please upload files ');
        } else {
          let form = new FormData();
          form.append('file', this.fileList);
          this.$axios({
            method:"post",
            url: "http://127.0.0.1:8000/report",
            headers:{
              'Content-type': 'multipart/form-data'
            },
            data:form
          }).then(
            res=>{

            },err =>{
            });
        }
      }

    }
  }
</script>

<style scoped>

</style>
