<template>
  <div class="home">
    <HomePage msg="Welcome to JobScraper"/>
    <table class="table">
       <thead>
            <tr>
              <th scope="col">Job titles</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(job_title, index) in job_titles" :key="index">
              <td>{{job_title}}</td>
            </tr>
          </tbody>
    </table>
  </div>
</template>

<script>
// @ is an alias to /src
import HomePage from '@/components/HomePage.vue';
import axios from 'axios';

export default {
  name: 'Home',
  components: {
    HomePage,
  },
  data() {
    return {
      job_titles: [],
    };
  },
  methods: {
    getJob() {
      const path = 'http://localhost:5000';
      axios.get(path)
        .then((res) => {
          this.job_titles = res.data.job_titles;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getJob();
  },
};
</script>
