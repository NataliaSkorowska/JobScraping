<template>
  <div>
    <HomePage msg="Welcome to JobScraper"/>
    <div class="search-bar">
      <input type="text"
         placeholder="Szukaj"
         v-model="filter" />
    </div>
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
      class="customPagination"
    ></b-pagination>
    <b-table  id="my-table"
      :items="offers"
      :per-page="perPage"
      :current-page="currentPage"
      bordered
      fixed></b-table>
    <div class="footer-copyright text-center py-3">
      <mdb-container fluid>
      </mdb-container>
    </div>

  </div>
</template>

<style>
.page-link{
  color: red !important;
  margin-top: 20px;
}
.page-item.active .page-link{
  background-color: lightgray !important;
}
.pagination{
  align-items: center;
  justify-content: center;
}
.table{
  width: 50% !important;
  margin: auto;
  ;
}
.search-bar{
   width: 190px !important;
  margin: auto;
  margin-top: 20px;
}
.footer-copyright{
  background-color: #800000;
}
</style>

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
      offers: [],
      perPage: 10,
      currentPage: 1,
    };
  },
  computed: {
    rows() {
      return this.offers.length;
    },
  },
  methods: {
    getJob() {
      const path = 'http://localhost:5000';
      axios.get(path)
        .then((res) => {
          this.offers = res.data.offers;
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
  onChangePage(pageOfItems) {
    // update page of items
    this.pageOfItems = pageOfItems;
  },
};
</script>
