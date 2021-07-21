<template>
<html>
      
      <div class = "top-left-uncompleted">
            <div id="uncompleted">
                    <h3>List of Employees that have yet to completed the survey</h3>
                    <table id ="uncompleted-table">
                        <tr>
                            <th>Name</th>
                            <th>Employee ID</th>
                            <th>Company Email Address</th>
                            <th>Department</th>
                        </tr>
                        <tr v-for="uncompleted in uncompletedsurvey" :key="uncompleted">
                            <td>{{uncompleted.name}}</td>
                            <td>{{uncompleted._id}}</td>
                            <td>{{uncompleted.email}}</td>
                            <td>{{uncompleted.department}}</td>
                        </tr>
                    </table>
            </div>

      </div>

</html>
</template>

<script>
import {ref} from 'vue'

export default {
    setup(){
      const uncompletedsurvey = ref ([])
      const error = ref (null)

      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/email')
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')

              }
              uncompletedsurvey.value = await data.json()
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
          }
      load()
      return{uncompletedsurvey, error}
    }
  }

</script>