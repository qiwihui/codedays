<template>
  <div id="app" class="app">
    <div class="app-container">
      <div id="nav">
        <navi />
      </div>
      <div class="lander">
        <router-view></router-view>
      </div>
      <footer class="footer">
        <div class="copyright">
          <ul>
            <li>
              <a href="/" class="copyright">© 每日一题 2020</a>
            </li>
          </ul>
        </div>
      </footer>
    </div>
  </div>
</template>

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
footer.footer {
    margin-top: 48px;
    margin-left: calc(-50vw + 50%);
    flex-direction: column;
    background: #fff;
    width: 100vw;
    bottom: 0;
    z-index: 2;
    left: 0;
    right: 0;
    border-top: 2px solid #f1f1f1;
    justify-content: center;
    align-items: center;
}
footer.footer>.copyright {
    padding: 24px;
    border-top: 2px solid #f1f1f1;
    color: #555;
    width: 100%;
}
footer.footer>.copyright>ul {
    flex-direction: row;
    justify-content: center;
}
footer.footer>.copyright>ul {
    list-style-type: none;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 0;
    line-height: 36px;
}
footer.footer>.copyright>ul>li {
    margin-right: 24px;
}
footer.footer>.copyright>ul>li>a {
    color: #555;
    text-decoration: none;
}
</style>

<script>
import Navi from "@/components/Nav.vue";
export default {
  components: {
    Navi
  }
};
</script>