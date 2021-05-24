<template>
<div>
  <b-navbar class="navbar" toggleable="lg">
    <b-navbar-brand><h1 class="title"><a href="http://localhost:8080/">JOB SCRAPING</a></h1></b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  </b-navbar>
        <br>
        <div>
          <span>Miejsca, w których znaleźliśmy najwięcej ofert pracy</span>
          <column-chart class="column-chart" :data="miasta" :colors="['#cc0000']"></column-chart>
        </div>
        <br>
        <div>
          <span>Forma zatrudnienia</span>
          <pie-chart :data="umowy" :colors="['#cc0000', '#3D0000',
          '#7A0000','#FF8585','#FF3333']"></pie-chart>
        </div>
        <br>
        <div>
          <span>Poszukiwany wymiar pracy</span>
          <bar-chart class="bar-chart"
           :data="etaty" :colors="['#cc0000', '#3D0000','#7A0000']"></bar-chart>
        </div>
        <br>
        <div>
          <span>Poziom stanowiska</span>
          <pie-chart :donut=true :data="pozycje" :colors="['#cc0000', '#3D0000',
          '#7A0000','#FF8585','#FF3333']"></pie-chart>
        </div>
  <footer class="footer">
         <div class="text-center p-3">
   Projekt stworzony przez: Aleksandra Okrój, Natalia Skórowska, Mateusz Sałata
  </div>
      </footer>
</div>
</template>

<style scoped>
div{
  text-align: center;
}
span{
  font-size: 25px;
}
.column-chart{
  padding-left: 2%;
  padding-right: 2%;
}
.bar-chart{
  padding-left: 20%;
  padding-right: 30%;
}
.navbar{
  background-color:#cc0000;
  height: 120px;
}
h1{
  color:white;
}
.title{
  font-size: 80px;
  text-align: center;
}
 a, a:hover, a:focus, a:active {
      text-decoration: none;
      color: inherit;
 }
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      miasta: [],
      umowy: [],
      etaty: [],
      pozycje: [],
    };
  },
  methods: {
    getMiasto() {
      const path = 'http://localhost:5000/miasto';
      axios.get(path)
        .then((res) => {
          this.miasta = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getUmowa() {
      const path = 'http://localhost:5000/umowa';
      axios.get(path)
        .then((res) => {
          this.umowy = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getEtat() {
      const path = 'http://localhost:5000/etat';
      axios.get(path)
        .then((res) => {
          this.etaty = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getPozycja() {
      const path = 'http://localhost:5000/pozycja';
      axios.get(path)
        .then((res) => {
          this.pozycje = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMiasto();
    this.getUmowa();
    this.getEtat();
    this.getPozycja();
  },
};
</script>
