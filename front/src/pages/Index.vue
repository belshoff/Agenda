<template>
  <q-page class="flex flex-left">
    <!-- <img alt="Quasar logo" src="~assets/quasar-logo-full.svg"> -->
    <datepicker v-model="filter.date" />
    <pre>{{ filter }}</pre>
  </q-page>
</template>

<style>
</style>

<script>
import Datepicker from 'components/TouchDatePicker.vue'

export default {
  name: 'PageIndex',
  components: {
    Datepicker
  },
  data () {
    return {
      filter: {
        date: ''
      },
      get: {}
    }
  },
  mounted () {
    this.populate()
  },
  methods: {
    populate () {
      this.$axios({
        url: 'localhost:5000/compras',
        method: 'get',
        data: this.filter
      }).then((response) => {
        console.log(response)
        this.get = response
      }).catch(() => {
        this.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Loading failed',
          icon: 'report_problem'
        })
      })
    }
  }
}
</script>
