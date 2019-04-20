<template>
  <section class="container-fluid">
    <div class="row white">
      <div class="col-md-12 col-lg-12 header no-padding">
        <div class="col-md-4 col-lg-4 text-left">
          <span @click="change" class="far" :class="`fa-${isOpen ? 'minus' : 'plus'}-square`" style="margin-right: 1rem; margin-left: 3px;"></span>
          <span>AGENDA</span>
        </div>
        <div class="col-md-4 col-lg-4 text-center">
          <!-- CODE HERE -->
        </div>
        <div class="col-md-4 col-lg-4 text-right">
          {{ $t('lang') }}
        </div>
      </div>
    </div>
    <div class="row" :style="customStyle">
      <div class="left-bar text-center no-padding container-fluid" :style="leftWidth">
        <left-menu :to-show="isOpen" />
      </div>
      <div class="container-fluid main-screen" :style="rightWidth">
        <router-view />
      </div>
    </div>
  </section>
</template>

<script>
import leftMenu from '@/components/LeftMenu.vue'

export default {
  components: {
    leftMenu
  },
  data () {
    return {
      isOpen: true
    }
  },
  computed: {
    leftWidth () {
      return `width: ${this.isOpen ? 10 : 3}rem !important;`
    },
    rightWidth () {
      return `width: calc(100% - ${this.isOpen ? 10 : 3}rem);`
    },
    customStyle () {
      return `height: calc(${window.innerHeight}px - 3rem) !important;`
    }
  },
  methods: {
    change () {
      this.isOpen = !this.isOpen
      this.$forceUpdate()
    }
  }
}
</script>

<style scoped>
.no-padding {
  padding: 0%;
}
.main-screen {
  border: solid #145987 thin;
  padding-top: 15px;
  background-color: whitesmoke;
}
.header {
  background-color: #145987;
  height: 3rem; /* NÃO ALTEREM! */
  font-weight: bold;
  display: flex;
  align-items: center;
}
.left-bar {
  color: white;
  height: 100%;
  border: solid #145987 thin;
  border-right: none;
  background-color: #00759d;
}
.white {
  color: white;
}
</style>
