<template>
  <div class="subscribe">
    <header>增加你的面试成功率！</header>
    <p class="slogan">通过每天解决一个编程问题，提高你的编程能力：</p>
    <p class='warning'><span v-if="message != ''">{{ message }}</span></p>
    <div class="container">
      <form>
        <input
          type="email"
          name="email"
          v-model="email"
          class="email"
          placeholder="你的邮箱"
          autofocus="autofocus"
          required
        />
        <button @click.prevent="subscribe" type="submit" class="submit">
          <span v-if='loading==false'>订阅每日一题邮件</span>
          <span v-else><beat-loader :loading="loading" :color='color' :size='size'></beat-loader></span>
        </button>
      </form>
      <div class="disclaimer">没有广告，随时取消</div>
    </div>
  </div>
</template>

<style lang="css">
.subscribe {
  background: rgb(3, 169, 244);
  padding: 48px 24px;
  color: #fff;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.subscribe > header {
  font-size: 48px;
}
.subscribe > .slogan {
  margin-bottom: 10px;
  font-size: 24px;
  font-weight: 300;
  margin: 24px 0 0;
  line-height: 36px;
}
.subscribe > .container {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.email {
  width: 100%;
  text-align: center;
}
.submit {
  width: 100%;
  margin: 0;
  cursor:pointer; 
}

.disclaimer {
  margin: 12px 0 0;
  text-align: center;
  font-size: 0.8em;
}
.warning {
  color: black;
}
form {
  display: block;
  margin-top: 0em;
  width: 40%;
}

@media (max-width: 600px) {
  form {
    width: 100%;
  }
}

button {
  background: none;
  padding: 15px 24px;
  border: none;
  outline: none;
  background: #ffce4f;
  color: #6e5817;
  font-weight: 600;
  font-size: 18px;
  box-shadow: 0 3px 0 0 #6e5817;
}
input {
  border: none;
  outline: none;
  color: #fff;
  height: 50px;
  /* border-radius: 4px; */
  -webkit-transition: all .15s ease;
  transition: all .15s ease;
  font-size: 18px;
  color: #111;
  padding: 0 24px;
}
</style>

<script>
import BeatLoader from 'vue-spinner/src/BeatLoader.vue'
export default {
  name: "subscribe",
  data() {
    return {
      email: "",
      message: "",
      loading: false,
      color: '#000',
      size: '11px'
    }
  },
  methods: {
    subscribe() {
      if (this.email == '') {
        this.message = "请输入邮箱"
        return true
      }
      this.loading=true
      this.$http
        .post("/subscribe", { email: this.email })
        .then(response => {
          this.loading=false
          if (response.status == 201) {
            this.message = response.data.message
          } else {
            this.message = response.data.message
          }
        })
        .catch((error) => {
          this.loading=false
          console.log(error)
          if (error.response.status == 429) {
            this.message = error.response.data.message
          }
        })
    },
    checkForm: function (e) {
      this.errors = [];
      if (!this.email) {
        this.errors.push('Email required.')
      } else if (!this.validEmail(this.email)) {
        this.errors.push('Valid email required.')
      }

      if (!this.errors.length) {
        return true
      }

      e.preventDefault();
    },
    validEmail: function (email) {
      var re = /^(([^<>()[]\.,;:\s@"]+(\.[^<>()[]\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
      return re.test(email)
    }
  },
  components: {
    BeatLoader
  },
}
</script>
