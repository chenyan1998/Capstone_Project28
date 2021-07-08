import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import installElementPlus from './plugins/element'
import 'chartjs-adapter-moment';
import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'
import ECharts from 'vue-echarts'
import { use } from "echarts/core"

// import ECharts modules manually to reduce bundle size
const app = createApp(App)
installElementPlus(app)

// register globally (or you can do it locally)
app.component('v-chart', ECharts)
app.mount()
app.use(router).mount('#app')
app.use(VueChartkick)