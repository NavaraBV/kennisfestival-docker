<template>
  <li>
    <base-card>
      <header>
        <h3>{{ task }}</h3>
        <nav>
          {{ status }}
        </nav>
      </header>
      <p>Assignee: {{ assignee }}</p>
    </base-card>
  </li>
</template>

<script>
export default {
  props: ["task", "assignee", "status"],
};
</script>

<style scoped>
li {
  margin: auto;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

h3 {
  font-size: 1.25rem;
  margin: 0.5rem 0;
}

p {
  margin: 0.5rem 0;
}

nav {
  text-decoration: none;
  color: var(--vt-c-orange);
}
</style>
