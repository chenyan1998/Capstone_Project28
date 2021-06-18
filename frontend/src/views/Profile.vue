<template>
    <el-row>
        <el-col :span="4"><h5>menu</h5><Sidebar :current_path="3" /></el-col>  
        <el-col :span="20">
            <el-descriptions class="margin-top" title="With border" :column="3" :size="size" border>
    <template #extra>
      <el-button type="primary" size="small">Operation</el-button>
    </template>
    <el-descriptions-item>
      <template #label>
        <i class="el-icon-user"></i>
        Username
      </template>
      kooriookami
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <i class="el-icon-mobile-phone"></i>
        Telephone
      </template>
      18100000000
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <i class="el-icon-location-outline"></i>
        Place
      </template>
      Suzhou
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <i class="el-icon-tickets"></i>
        Remarks
      </template>
      <el-tag size="small">School</el-tag>
    </el-descriptions-item>
    <el-descriptions-item>
      <template #label>
        <i class="el-icon-office-building"></i>
        Address
      </template>
      No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
    </el-descriptions-item>
  </el-descriptions>
        </el-col>
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