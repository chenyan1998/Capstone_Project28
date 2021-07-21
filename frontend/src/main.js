import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import installElementPlus from './plugins/element'
import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'

const app = createApp(App)
installElementPlus(app)

app.mount()
app.use(router).mount('#app')
app.use(VueChartkick)