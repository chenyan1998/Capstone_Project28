<template>
  <div>
      <department-report v-if="report_type === 'DepartmentReport'" />
      <question-report v-if="report_type === 'QuestionReport'" />
      <individual-report v-if="report_type === 'IndividualReport'" />
  </div>
  
</template>

<script>
import DepartmentReport from '../components/DepartmentReport.vue'
import QuestionReport from '../components/QuestionReport.vue'
import IndividualReport from '../components/IndividualReport.vue'
export default {
    // This page is a detailed report page.
    name: 'DetailedReport' ,
    components: { DepartmentReport, QuestionReport, IndividualReport},
    created() {
            this.report_type = this.$route.params.report_type;
    },
    setup(){
    }

}
</script>

<style>

</style>