<template>
  <section class="container-fluid">
    <div class="row header">
      <div class="col-md-6 col-lg-6 h1">
        <Label>{{ $tc('page.header.purchase') }}</Label>
      </div>
      <div class="col-md-6 col-lg-6 text-right">
        <button @click="save" class="btn btn-link btn-lg far fa-save"></button>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 col-lg-6 text-left">
        <label>{{ $tc('page.label.date') }}:</label>
        <br />
        <date-picker id="DatePicker" v-model="compra.date" :language="_i18n.locale" />
      </div>
    </div>
    <label>{{ $tc("page.label.product", 2) }}:</label>
    <div class="row" v-for="(p, count) in compra.produtos" :key="count">
      <div class="col-md-4 col-lg-4">
        <label>{{ $tc("page.label.name") }}:</label>
        <input type="text" class="form-control" v-model="p.name" />
      </div>
      <div class="col-md-4 col-lg-4">
        <label>{{ $tc("page.label.price") }}:</label>
        <input type="number" class="form-control" v-model="p.price" />
      </div>
      <div class="col-md-1 col-lg-1">
        <label for=""><span style="visibility: hidden;">.</span></label>
        <button @click="compra.produtos.splice(count, 1)" type="button" class="form-control btn btn-md btn-link">
          <i class="far fa-trash-alt"></i>
        </button>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4 col-lg-4">
        <label>{{ $tc("page.label.name") }}:</label>
        <input type="text" class="form-control" v-model="produto.name" />
      </div>
      <div class="col-md-4 col-lg-4">
        <label>{{ $tc("page.label.price") }}:</label>
        <input type="number" class="form-control" v-model="produto.price" />
      </div>
      <div class="col-md-1 col-lg-1">
        <label for=""><span style="visibility: hidden;">.</span></label>
        <button @click="addProduct" type="button" class="form-control btn btn-md btn-link">
          <i class="far fa-plus-square"></i>
        </button>
      </div>
    </div>
    <pre>{{ produto }}</pre>
    <!--  -->
    <transition name="fade">
      <div v-if="showAlert" class="alert alert-warning" role="alert">
        {{ alertText }}
      </div>
    </transition>
    <!--  -->
  </section>
</template>

<script>
export default {
  components: {
    datePicker: () => import('@/components/TouchDatePicker.vue')
  },
  watch: {
    showAlert () {
      let _ = this
      if (this.showAlert) {
        setTimeout(() => {
          _.showAlert = false
        }, 2000)
      }
    }
  },
  data () {
    return {
      alertText: '',
      showAlert: false,
      compra: {
        date: '',
        produtos: []
      },
      produto: {
        name: '',
        price: 0.00
      },
      selectedDate: ''
    }
  },
  created () {
    this.compra.date = `${new Date().getFullYear()}-${new Date().getMonth() + 1}-${new Date().getDate()}`
  },
  methods: {
    addProduct () {
      if (!this.produto.name) {
        this.showAlert = true
        this.alertText = this.$t('page.alerts.name')
        return
      } else if (!this.produto.price) {
        this.showAlert = true
        this.alertText = this.$t('page.alerts.price')
        return
      }
      this.compra.produtos.push(this.produto)
      this.produto = {name: '', price: 0.0}
      this.$forceUpdate()
    },
    format (date) {
      if (!date) {
        return ''
      }
      let splitDate = date.split('-')
      return `${splitDate[2]}/${splitDate[1]}/${splitDate[0]}`
    },
    save () {
      this.axios.post('http://127.0.0.1:5000/api/compras', this.compra).then(
        result => {
          this.$router.replace('/')
          console.log(result)
        }
      ).catch(
        err => {
          console.error(err)
        }
      )
    },
    populate () {
      let filter = this.selectedDate !== '' ? `date=${this.requestFormat(this.selectedDate)}` : 'getAll=true'
      this.axios.get(`http://127.0.0.1:5000/api/compras?${filter}`).then(
        result => {
          this.dados = result.data
        }
      )
    }
  }
}
</script>

<style scoped>
.header {
  border-bottom: solid lightgray thin;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active em versões anteriores a 2.1.8 */ {
  opacity: 0;
}
</style>
