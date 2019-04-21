<template>
  <div id="app">
    <main-template></main-template>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
    mainTemplate: () => import('@/templates/Main.vue')
  }
}
</script>

<style>
.bold {
  font-weight: bold;
}
</style>
