import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
// import Modal from "@burhanahmeed/vue-modal-2";


const myApp = createApp(App)
myApp.use(router)
myApp.mount('#app')
