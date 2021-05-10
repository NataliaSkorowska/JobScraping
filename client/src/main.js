import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import JwPagination from 'jw-vue-pagination';
import App from './App.vue';
import router from './router';
// eslint-disable-line import/no-extraneous-dependencies
Vue.component('jw-pagination', JwPagination);
Vue.use(BootstrapVue);
Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
