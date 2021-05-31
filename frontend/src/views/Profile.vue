<template>
    <el-row>
        <el-col :span="4"><h5>menu</h5><Sidebar :current_path="3" /></el-col>  
        <el-col :span="12"> <h2>Profile page</h2></el-col>
    </el-row>
</template>

<script>
import Sidebar from '../components/Sidebar'

export default {
    name: 'Profile',
    components: {Sidebar}
}
</script>

<style>

</style>