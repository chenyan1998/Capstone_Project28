<template>
<html>
  <TopNavigationBar/>
  <div class="home">
    <div v-for="report_type in report_list" :key="report_type">
      <router-link :to="{name: 'DetailedReport', params: {report_type : report_type}}">
            <button>{{report_type}}</button>
      </router-link>
    </div>
    <button>Export</button>
  </div>

<el-container style="height: 500px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '3']">
      <el-submenu index="1">
        <template #title><i class="el-icon-message"></i>Home</template>
       
      </el-submenu>
      <el-submenu index="2">
        <template #title><i class="el-icon-menu"></i>Report</template>
      
      </el-submenu>
      <el-submenu index="3">
        <template #title><i class="el-icon-setting"></i>Survey</template>
        <el-menu-item-group>
          <template #title>All</template>
        </el-menu-item-group>
        <el-menu-item-group>
          <template #title>Wellbeing</template>
        </el-menu-item-group>
        <el-menu-item-group>
          <template #title>Core values</template>
        </el-menu-item-group>
        <el-menu-item-group>
          <template #title>Personality</template>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </el-aside>

  <el-container>
    <el-header style="text-align: right; font-size: 12px">
      <el-dropdown>
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <template #dropdown>
          <el-dropdown-menu>
              <el-dropdown-item>View</el-dropdown-item>
              <el-dropdown-item>Add</el-dropdown-item>
              <el-dropdown-item>Delete</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <span>HR</span>
    </el-header>

    <el-main>
      <el-row justify="start">
      <el-select v-model="value1" multiple placeholder="Survey Year">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>

      <el-select
        v-model="value2"
        multiple
        collapse-tags
        style="margin-left: 20px;"
        placeholder="EEI Score">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>

      <el-select
        v-model="value2"
        multiple
        collapse-tags
        style="margin-left: 20px;"
        placeholder="Question">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="0" gutter="10">
          Summary Metrics
        </el-col>
      </el-row>
      <el-row>
        <el-popover
          placement="top-start"
          title="Average EEI Score"
          :width="200"
          :height="400"
          trigger="hover"
          content="this is content, this is content, this is content"
        >
        <template #reference>
          <el-button>68.1</el-button>
        </template>
      </el-popover>

              <el-popover
          placement="top-start"
          title="Average Wellbeing Score"
          :width="200"
          :height="400"
          trigger="hover"
          content="this is content, this is content, this is content"
        >
        <template #reference>
          <el-button>97.3</el-button>
        </template>
      </el-popover>

                    <el-popover
          placement="top-start"
          title="Average Core Value Score"
          :width="200"
          :height="600"
          trigger="hover"
          content="this is content, this is content, this is content"
        >
        <template #reference>
          <el-button>83.5</el-button>
        </template>
      </el-popover>
      </el-row>
      <el-row :gutter="10">
        <el-col :span="0" gutter="10">
          Average Score by Questions
        </el-col>
      </el-row>
      <el-row justify="start" class="x">
        <el-col>
          <img alt="logo" src="../assets/Picture1.jpg">
        </el-col>
      </el-row>
      <el-row>
          <el-button type="primary" round>Check to view survey questions</el-button>
      </el-row>
      
    </el-main>
  </el-container>
</el-container>

  
</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import {ref} from 'vue'
import TopNavigationBar from '../components/TopNavigationBar.vue'
export default {
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar},
    setup(){
    const report_list = ref(['DepartmentReport', 'QuestionReport', 'IndividualReport'])
    return {report_list}
  }
}
</script>

<style>

</style>