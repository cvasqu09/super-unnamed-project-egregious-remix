<template>
  <b-navbar>
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <h1>Super</h1>
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item :to="{ path: '/' }">
        Home
      </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ name: 'posts' }">
        Posts
      </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ name: 'books'}">
        Books
      </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ name: 'users'}">
        Users
      </b-navbar-item>
      <b-navbar-item tag="router-link" :to="{ name: 'journal-list'}">
        Journals
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
export default {
  name: 'TheHeader',
};
</script>

<style scoped>

</style>
