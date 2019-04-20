<template>
  <section>
    <router-link class="link" v-for="(item, index) in links" :key="index" tag="div" :to="item.link">
      <i :class="item.icon" class="icon" />
      <span v-show="toShow">{{ item.label }}</span>
    </router-link>
  </section>
</template>

<script>
export default {
  props: {
    toShow: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {}
  },
  computed: {
    links () {
      return [
        {
          label: this.$t('page.label.home'),
          link: '/',
          icon: 'fa fa-home'
        },
        {
          label: this.$tc('page.label.form', 2),
          link: 'form',
          icon: 'fab fa-wpforms'
        }
      ]
    }
  }
}
</script>

<style scoped>
section {
  margin-top: 0;
}
.icon {
  margin-right: 1rem;
}
.link {
  height: 3rem;
  padding-left: 15px;
  display: flex;
  align-items: center;
  cursor: pointer;
}
.link:hover {
  background-color: #145987;
}
</style>
