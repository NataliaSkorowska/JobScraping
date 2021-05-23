<template>
  <div>
    <HomePage/>
    <p class="text">Filtruj oferty po pracodawcy, stanowisku lub lokalizacji: </p>
    <div class="search-bar">
      <b-icon-search variant="danger" font-scale="1.5"></b-icon-search>
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
      :fields="fields"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      responsive="sm"
      :per-page="perPage"
      :current-page="currentPage"
      :filter="filter"
      bordered
      class="table">
       <template template v-slot:cell(Stanowisko)="data" class="Stanowisko">
        <b-link v-bind:href="data.item.Link">{{ data.item.Stanowisko}}</b-link>
      </template>
      </b-table>
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
.text{
  text-align: center;
  margin-top: 30px;
  color: red;
  font-weight: bold;
}
.table{
  width: 1000px !important;
  margin: auto;
}
.search-bar{
   width: 190px !important;
  margin: auto;
  margin-top: 20px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.footer{
  background-color: #cc0000;
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
      sortBy: 'Pracodawca',
      sortDesc: false,
      fields: [{ key: 'Pracodawca', sortable: true },
        { key: 'Stanowisko', sortable: false },
        { key: 'Lokalizacja', sortable: true }],
      offers: [],
      perPage: 30,
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
