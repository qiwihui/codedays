<template>
  <div id="app" class="app">
    <div class="app-container">
      <Navi />
      <div class="lander">
        <router-view></router-view>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
import Navi from "@/components/Navi.vue"
import Footer from "@/components/Footer.vue"
export default {
  components: {
    Navi,
    Footer
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  outline: none;
}

body {
  color: #000;
  margin: 0;
  padding: 0;
}

.app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  display: flex;
  justify-content: center;
  position: relative;
  min-height: 100%;
}

.app>.app-container {
  max-width: 960px;
  min-height: calc(100vh - 242px);
  height: calc(100% - 350px);
}

.lander {
  flex-direction: column;
  padding: 0;
}
</style>