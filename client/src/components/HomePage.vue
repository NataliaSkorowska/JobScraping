<template>
<div>
  <b-navbar class="navbar" toggleable="lg">
    <b-navbar-brand>
      <h1 class="title"><a href="http://localhost:8080/">JOB SCRAPING</a></h1></b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <h1 class="statystyki"><a href="http://localhost:8080/stats">Statystyki</a></h1>
  </b-navbar>
</div>
</template>

<style scoped>
.statystyki{
  font-size: 40px;
}
 a, a:hover, a:focus, a:active {
      text-decoration: none;
      color: inherit;
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
  padding-left: 10%;
}
</style>
