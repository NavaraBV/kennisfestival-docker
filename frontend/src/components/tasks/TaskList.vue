<template>
  <p v-if="isLoading">Loading...</p>
  <p v-else-if="!isLoading && (!tasks || tasks.length === 0)">
    <base-card> No tasks found. Start adding some tasks first. </base-card>
  </p>
  <ul v-else>
    <task-item
      v-for="task in tasks"
      :key="task.id"
      :task="task.task"
      :assignee="task.assignee"
      :status="task.status"
    >
    </task-item>
  </ul>
</template>

<script>
import TaskItem from "./TaskItem.vue";

export default {
  components: {
    TaskItem,
  },
  props: ["tasks", "isLoading"],
};
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
</style>
