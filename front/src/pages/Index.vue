<template>
  <section class="container-fluid">
    <div class="row">
      <div class="col-md-6 col-lg-6 text-left">
      </div>
      <div class="col-md-5 col-lg-5 text-right">
        <date-picker id="DatePicker" @input="populate" v-model="selectedDate" :language="_i18n.locale"></date-picker>
        <button class="btn" @click="populate">
          <i class="fas fa-search"></i>
        </button>
      </div>
      <div class="col-md-1 col-lg-1 text-center">
        <label>{{ format(selectedDate) }}</label>
      </div>
    </div>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-3 col-lg-3 postit text-center" v-for="linha in dados" :key="linha.id">
          <div class="row">
            <div class="col-md-12 col-lg-12">
              <button class="btn btn-sm btn-warning far fa-edit" />
              <button class="btn btn-sm btn-warning far fa-trash-alt" @click="del(linha.id)" />
            </div>
          </div>
          <label class="bold">
            {{ format(linha.date) }}
          </label>
          <p v-for="produto in linha.produtos" :key="produto.id">
            {{ produto.name }}: {{ produto.price }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  components: {
    datePicker: () => import('@/components/TouchDatePicker.vue')
  },
  data () {
    return {
      selectedDate: '',
      dados: []
    }
  },
  created () {
    this.selectedDate = `${new Date().getFullYear()}-${new Date().getMonth() + 1}-${new Date().getDate()}`
  },
  mounted () {
    this.populate()
  },
  methods: {
    format (date) {
      if (!date) {
        return ''
      }
      let splitDate = date.split('-')
      return `${splitDate[2]}/${splitDate[1]}/${splitDate[0]}`
    },
    requestFormat (date) {
      let splitDate = date.split('-')
      return `${Number(splitDate[0])}-${Number(splitDate[1])}-${Number(splitDate[2])}`
    },
    del (id) {
      this.axios.delete(`http://127.0.0.1:5000/api/compras/${id}`).then(
        result => {
          this.populate()
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
.postit {
  margin: 1rem;
  background-color: #ffc107;
  border-left-width: 10px;
  border-left-style: dotted;
  border-left-color: white;
  border-radius: 0px 1rem 1rem 0px;
}
</style>
