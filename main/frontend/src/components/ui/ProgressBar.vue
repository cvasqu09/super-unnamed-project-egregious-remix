<template>
  <Progress :value="progress" :radius="50" :strokeWidth="10">
    <template v-slot:footer>
      <b>{{description}}</b>
    </template>
  </Progress>
</template>

<script>
import Progress from 'easy-circular-progress';

export default {
  name: 'ProgressBar',
  components: {
    Progress,
  },
  props: {
    progress: {
      default: 0,
    },
    description: {
      type: String,
      default: 'Total Progress',
    },
  },
};
</script>

<style scoped>

</style>
