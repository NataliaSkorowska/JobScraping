<template>
  <div class="home">
    <HomePage msg="Welcome to JobScraper"/>
    <p>{{job_titles}}</p>
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
