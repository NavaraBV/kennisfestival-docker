<template>
  <div>
    <slot></slot>
  </div>
</template>

<style scoped>
@import "@/assets/base.css";
div {
  background-color: var(--vt-c-white);
  color: var(--vt-c-black-soft);
  margin: 2rem auto;
  padding: 1rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
}
</style>
