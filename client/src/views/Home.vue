<template>
  <div>
    <HomePage/>
    <div class="search-bar">
      <input type="text"
         placeholder="Szukaj"
         v-model="filter" />

    </div>
    <b-table  id="my-table"
      :items="offers"
      :per-page="perPage"
      :current-page="currentPage"
      :filter="filter"
      bordered
      fixed
      class="table"></b-table>
      <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
      class="customPagination"
    ></b-pagination>
    <div>
      <footer class="footer">
         <div class="text-center p-3">
   Projekt stworzony przez: Aleksandra Okrój, Natalia Skórowska, Mateusz Sałata
  </div>
      </footer>
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
  margin-bottom: 20px;
}
.footer{
  background-color: #800000;
  width:100%;
  height: 65px;
  bottom:0;
  margin-bottom: 0px;
  margin-top: 20px;
  color: white;
}
#myInput {
  background-image: url('/css/searchicon.png'); /* Add a search icon to input */
  background-position: 10px 12px; /* Position the search icon */
  background-repeat: no-repeat; /* Do not repeat the icon image */
  width: 100%; /* Full-width */
  font-size: 16px; /* Increase font-size */
  padding: 12px 20px 12px 40px; /* Add some padding */
  border: 1px solid #ddd; /* Add a grey border */
  margin-bottom: 12px; /* Add some space below the input */
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
      perPage: 8,
      currentPage: 1,
      filter: '',
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
  sortBy(sortKey) {
    this.reverse = (this.sortKey === sortKey) ? !this.reverse : false;
    this.sortKey = sortKey;
  },
};
</script>
