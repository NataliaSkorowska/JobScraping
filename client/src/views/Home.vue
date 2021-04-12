<template>
  <div class="home">
    <HomePage msg="Welcome to JobScraper"/>
    <!-- <b-container class="bv-example-row">
    <b-col>1of2
    <b-col v-for="(job_title, index) in job_titles" :key="index">
      <b-row>{{job_title}}</b-row>
    </b-col>
    </b-col>
    <b-col>2of2
    <b-col v-for="(job_detail, index) in job_details" :key="index">
      <b-row>{{job_detail}}</b-row>
    </b-col>
    </b-col>
</b-container> -->
<b-container class="bv-example-row">
  <b-row>
    <b-col>Tytuł
      <b-row v-for="(job_title, index) in job_titles" :key="index">{{job_title}}</b-row>
    </b-col>
    <b-col>Lokalizacja
      <b-row v-for="(job_detail, index) in job_details" :key="index">{{job_detail}}</b-row>
    </b-col>
  </b-row>
</b-container>
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
          this.job_details = res.data.job_details;
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
