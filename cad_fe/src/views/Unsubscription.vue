<template>
  <div>
    <div class="page">
      <h1>感谢您的订阅！</h1>
      <p v-if="message != ''">{{ message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "",
      unsubscribe_key: ""
    }
  },
  mounted() {
    this.verify()
  },
  methods: {
    verify() {
      this.$http
        .post("/api/v1/unsubscribe", { unsubscribe_key: this.$route.query.unsubscribe_key })
        .then(response => {
          if (response.status == 200) {
            this.message = response.data.message
          } else {
            this.message = response.data.message
          }
        })
        .catch(error => {
          console.log(error)
          if (error.response.status == 429) {
            this.message = error.response.data.message
          }
        })
    }
  }
};
</script>

<style>
.page{
  min-height: calc(100vh - ((108px + 24px) + (calc(86px + 24px))));
  text-align: center;
}
</style>