<template>
<html>
      <TopNavigationBar/>
      <Sidebar :current_path="5"/>
      <div class = "top-left-individual" style="width:1100px">
            <div id="table2" style="width:1000px">
            <div class = "title" style="margin: 20px">
              <el-table :data="tableData3" height="450" border style="width: 100%">
                <el-table-column prop="date" label="日期" width="180"> </el-table-column>
                <el-table-column prop="name" label="姓名" width="180"></el-table-column>
                <el-table-column prop="name" label="姓名" width="180"></el-table-column>
                <el-table-column prop="name" label="姓名" width="180"></el-table-column>
                <el-table-column prop="address" label="地址"></el-table-column></el-table>
            </div>
            </div>
      </div>

</html>
</template>

<script>
import Sidebar from '../components/Sidebar'
import TopNavigationBar from '../components/TopNavigationBar.vue'
import {ref} from 'vue'

export default {
  name: 'Individual',
  components: {Sidebar, TopNavigationBar},
    data() {
      return {
        tableData3: [{
          date: '2016-05-03',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-02',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-04',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-01',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-08',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },{
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },{
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },{
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },{
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        },{
          date: '2016-05-06',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }, {
          date: '2016-05-07',
          name: '王小虎',
          address: '上海市普陀区金沙江路 1518 弄'
        }]
      }
    }
  }

</script>


<style>

.top-left-individual {
  position: absolute;
  top : 10%;
  left: 20%;
  width: 75%;
}

</style>