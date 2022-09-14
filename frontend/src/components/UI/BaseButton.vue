<template>
  <button :class="mode">
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: ["mode"],
};
</script>

<style scoped>
button {
  padding: 0.75rem 1.5rem;
  font-family: inherit;
  background-color: var(--vt-c-orange);
  border: 1px solid var(--vt-c-orange);
  color: white;
  cursor: pointer;
}

button:hover,
button:active {
  background-color: var(--vt-c-orange-dark);
  border-color: var(--vt-c-orange-dark);
}

.flat {
  background-color: transparent;
  color: var(--vt-c-orange);
  border: none;
}

.flat:hover,
.flat:active {
  background-color: var(--vt-c-orange-soft);
}
</style>
