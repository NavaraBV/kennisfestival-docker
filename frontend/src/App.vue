<template>
  <h1>Tasks</h1>
  <div id="content">
    <task-form @added-task="taskAdded"></task-form>
    <task-list :tasks="tasks" :isLoading="isLoading"></task-list>
    <base-button @click="getTasks()">Fetch list</base-button>
  </div>
</template>

<script>
import axios from "axios";
import TaskList from "@/components/tasks/TaskList.vue";
import TaskForm from "@/components/tasks/TaskForm.vue";
import BaseButton from "@/components/UI/BaseButton.vue";

export default {
  components: {
    TaskList,
    TaskForm,
    BaseButton,
  },
  data() {
    return {
      tasks: [],
      isLoading: false,
    };
  },
  methods: {
    getTasks() {
      this.isLoading = true;
      this.error = null;

      axios
        .get(`${import.meta.env.VITE_ROOT_API}/tasks`)
        .then((response) => {
          this.tasks = response.data;
          this.isLoading = false;
        })
        .catch((error) => {
          console.log(error);
          this.error = "Failed to fetch data - please try again later.";
          this.isLoading = false;
        });
    },

    taskAdded(task) {
      this.tasks.push(task);
    },
  },
  mounted() {
    this.getTasks();
  },
};
</script>

<style>
@import "@/assets/base.css";

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
}
</style>
