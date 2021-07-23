<template>
    <TopNavigationBar/>
    <Sidebar :current_path="1" />
    <div id="home">
        <div class="container_file" style="width:600px">
        <div class = "title" style="margin: 20px">
            <h3> DB Schenker Survey Results </h3>
            <h4> Upload Survey Results </h4>
        </div>
        <br />
        <upload-files></upload-files>
        </div>
          
        <div class="container0_file" style="width:300px">
        <div class = "title" style="margin: 30px" >
            <font size="5" color = "white"> Survey Completion Rate</font><br />
             <br />           
            <font size="3" color = "white"> Completed Survey Numbers : 87</font><br />
            <font size="3" color = "white"> Survey Completed Rate : 85 % </font><br />
            <br />
            <br />
             <br />
            <el-button class = "send_survey_button" style="width:200px; ">Send Out Survey</el-button>
        </div>
        </div>

        <div class="container1_file" style="width:300px">
        <div class = "title" style="margin: 40px">
            <h3> Survey Introduction </h3>
            <p>Employee engagement surveys are a fundamental tool for 
                organisations to measure the employees’ level of commitment to 
                the organisation and have withstood the test of time due to its 
                comprehensiveness in assessing employees’ attitude towards the 
                organisation (Lepold et al., 2018). The primary purpose of such 
                surveys is to identify the factors that drive employees to perform
                 their best for the company as well as factors that reduce their 
                 commitment to the organisation. Once these factors are identified
                 , the management is then able to provide targeted intervention to 
                 help reduce the flight-risk within the organisation to improve their employee relations and the 
                 performance of the organisation.</p>
        </div>
        </div>
        <div class="container2_file" style="width:910px">
        <div class = "title" style="margin: 20px">
            <h3> Survey Questions Explanation </h3>
            <h4> Here is the questions' categories of our survey </h4>
            <p>The survey consists of four categories and questions are chosen from each of the four categories, and narrowed down to only 25 questions in total that are found to be most crucial. The full list of questions can be found in Appendix 6.</p>
            <b>Personality Traits</b>
            <p>Personality traits are a predictor of employee satisfaction, which may influence employee satisfaction with the emotional commitment of the organization. The results of empirical research in public utility enterprises show that Neuroticism is negatively correlated with employee satisfaction, Conscientiousness has no impact, and Agreeableness positively affects employee satisfaction. Employee satisfaction has a strong impact on affective commitment, and there is an important correlation between individual persistence characteristics and individual satisfaction in the workplace. Hence, questions measuring Agreeableness and Neuroticism are chosen amongst the Big 5 Personality Traits.</p>
            <b>Individual Wellbeing</b>
            <p>Workplace well-being plays an important role in the sustainability of organizations and individuals. Organizations that implement wellness programs at work report positive business results, such as improved employee retention, productivity, and a variety of other benefits such as mental health. For individuals, workplace benefits means a healthy and balanced life. The existence of workplace benefits will promote the "health" and high productivity of the individuals in the organization, which in turn will benefit the organization. Hence, questions selected measure the level of wellbeing in various aspects including mental, emotional, workplace wellbeing etc. </p>
            <b>Opinions and Emotions</b>
            <p>Opinions and Emotions refer to the employee’s perception of their role in the organisation. This refers to the interactions which they have with their team, effective communication with their supervisors or the management which ultimately determines whether the employee feels that they are part of the organisation and that their voices are heard. The stronger the sense of belonging, the greater the level of engagement (Johnson, Al & Daimler, 2019).</p>
            <b>Personal Information</b>
            <p>Employee age is an important paradigm for individual differences. Mathieu and Zajac believe that as workers get older, they will have fewer employment options, which may make them feel more favorable about their current jobs. Robinson et al. studied the relationship between age and employee engagement. They noted significant differences in employee engagement scores across age groups. They found that employee engagement declined slightly as workers got older, and was highest when workers entered the oldest group (60 and older). Ahuja et al. observed a modest but significant effect of age on intention to leave in India's IT sector. They found that there are different perceptions of job satisfaction and motivation across the age spectrum. Hence, personal information such as age would affect the satisfaction level and motivation of employees as well.</p>
        </div>
        </div>
    </div>

    <div class = "top-left-survey1_file"  >
      <div id="sendsurvey" >
            <h3>Send Out New Surveys</h3>
                <table id ="surveytable">
                  <tr>
                      <th>Name</th>
                      <th>Employee ID</th>
                      <th>Company Email Address</th>
                      <th>Phone Number</th>
                      <th>Position</th>
                  </tr>
                  <tr v-for="employee in employees" :key="employee">
                      <td>{{employee.name}}</td>
                      <td>12345</td>
                      <td>{{employee.email}}</td>
                      <td>{{employee.employee_details}}</td>
                      <td>{{employee.employee_risk_level}}</td>
                  </tr>
                </table>
      </div>
    </div>


</template>

<script>
import TopNavigationBar from '../components/TopNavigationBar.vue'
import Sidebar from '../components/Sidebar'
import UploadFiles from "../components/UploadFiles_tem";
import {ref} from 'vue'
export default {
    
    name: 'ReportHomepage',
    components: {Sidebar, TopNavigationBar,UploadFiles},
    setup(){
      const employees = ref ([])
      const error = ref (null)

      const load = async () =>{
          try{
              let data = await fetch ('http://127.0.0.1:8000/employee')
              console.log(data)
              if (!data.ok){
                  throw Error('no data available')

              }
              employees.value = await data.json()
              console.log(employees.value[0])
          }
              catch (err){
                  error.value = err.message
                  console.log (error.value)
              }
          }
      load()
      // const {employees, error, load} = getEmployeeList()
      // load()
      console.log('value is', employees)
      return{employees, error}
    }
}
</script>

<style>

.container_file  {
  background-color: rgba(82, 184, 175, 0.75);
	border-radius: 45px;
	width: 400px;
	height: 300px;
	margin: auto;
	position: absolute;
	width: 98%;
    left: 19%;
    top: 10%;}

.container0_file  {
  background-color: rgba(31, 146, 161, 0.75);
	border-radius: 45px;
	width: 400px;
	height: 300px;
	margin: auto;
	position: absolute;
	width: 98%;
    left: 57%;
    top: 10%;}

.container1_file  {
  background-color: rgba(184, 230, 233, 0.75);
	border-radius: 45px;
	width: 400px;
	height: 1800px;
	margin: auto;
	position: absolute;
	width: 98%;
    height: 100%;
    left: 77%;
    top: 10%;}

.top-left-survey1_file {
    background-color: rgba(164, 216, 216, 0.75);
    border-radius: 45px;
    width: 400px;
    height: 1000px;
    margin: auto;
    position: absolute;
    width: 78%;
    left: 19%;
    top: 48%;
    
}

.container2_file {
    white-space: pre-wrap;
    background-color: rgba(164, 216, 216, 0.75);
    border-radius: 45px;
    width: 400px;
    height: 900px;
    margin: auto;
    position: absolute;
    width: 78%;
    left: 19%;
    top: 88%;
}
</style>