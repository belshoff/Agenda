<template>
  <div id="app">
    <main-template></main-template>
  </div>
</template>

<script>
const mainTemplate = () => System.import('@/templates/Main.vue')

export default {
  name: 'App',
  components: {
    mainTemplate
  }
}
</script>
