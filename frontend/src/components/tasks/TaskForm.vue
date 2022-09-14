<template>
  <base-dialog
    v-if="inputIsInvalid"
    title="Invalid Input"
    @close="confirmError"
  >
    <template #default>
      <p>Unfortunately, at least one input value is invalid.</p>
      <p>
        Please check all inputs and make sure you enter at least a few
        characters in each field.
      </p>
    </template>
    <template #actions>
      <base-button @click="confirmError">Okay</base-button>
    </template>
  </base-dialog>
  <base-card>
    <form @submit.prevent="submitData">
      <div class="form-control">
        <label for="title">Task</label>
        <input id="title" name="title" type="text" v-model="enteredTask" />
      </div>
      <div class="form-control">
        <label for="assignee">Assignee</label>
        <input
          id="assignee"
          name="assignee"
          type="text"
          v-model="enteredAssignee"
        />
      </div>
      <div>
        <base-button type="submit">Add Resource</base-button>
      </div>
    </form>
  </base-card>
</template>

<script>
import axios from "axios";

export default {
  emits: ["added-task"],
  data() {
    return {
      inputIsInvalid: false,
      enteredTask: "",
      enteredAssignee: "",
    };
  },
  methods: {
    submitData() {
      if (
        this.enteredTask.trim() === "" ||
        this.enteredAssignee.trim() === ""
      ) {
        this.inputIsInvalid = true;
        return;
      }

      axios
        .post(`${import.meta.env.VITE_ROOT_API}/tasks`, {
          task: this.enteredTask,
          assignee: this.enteredAssignee,
          status: "new",
        })
        .then((response) => {
          this.$emit("added-task", response.data);
          this.enteredTask = "";
          this.enteredAssignee = "";
        });
    },
    confirmError() {
      this.inputIsInvalid = false;
    },
  },
};
</script>

<style scoped>
label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input,
textarea {
  display: block;
  width: 100%;
  font: inherit;
  padding: 0.15rem;
  border: 1px solid #ccc;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: var(--vt-c-orange);
  background-color: var(--vt-c-orange-light);
}

.form-control {
  margin: 1rem 0;
}
</style>
