<template>
  <div>
    <h1>Users</h1>
    <ul>
      <li v-for="user in users" :key="user.id">
        <h1>{{ user.username }}</h1>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserPage',
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    axios.post('/auth/', {
      username: 'test',
      password: 'password',
    })
      .then((res) => {
        this.users = res.data;
      });
  },
};
</script>

<style scoped>

</style>
