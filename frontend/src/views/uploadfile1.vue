<template>
    <div class="cancelRequest">
        <div>姓名：<input type="text" v-model="name"></div>
        <div>头像：<input type="file" ref="file"></div>
        <div @click="save">保存</div>
    </div>
</template>
 
<script>
export default {
    data(){
        return {
            value:''
        }
    },
    components:{},
    props:{},
    watch:{},
    computed:{},
    methods:{
        save(){
            let formData=new FormData();
            formData.append('name',this.name)
            formData.append('img',this.$refs.file.files[0])
            this.axios.post('/api/user/query',formData,{
                'Content-Type':'multipart/form-data'
            }).then(res=>{
 
            })
        }
    },
    created(){},
    mounted(){}
}
</script>
<style>
 
</style>
