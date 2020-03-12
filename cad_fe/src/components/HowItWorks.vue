<template>
  <div class="how-it-works">
    <header>如何操作？</header>
    <div class="steps-container">
      <div class="step">
        <header>
          <span class="number">1</span>我们出题
        </header>
        <p>从各大公司和技术论坛获取量身定制的问题。</p>
      </div>
      <div class="step">
        <header>
          <span class="number">2</span>你解决问题
        </header>
        <p>在第二天早上收到解决方法之前，你都需要自己解决问题。</p>
      </div>
      <div class="step">
        <header>
          <span class="number">3</span>我们给你发送答案
          <a class="badge">
            <span>VIP</span>
          </a>
        </header>
        <p>验证你的答案，并获得相关问题的背景知识。</p>
      </div>
      <div class="step">
        <header>
          <span class="number">4</span>我们提供技术支持
          <a class="badge">
            <span>VIP</span>
          </a>
        </header>
        <p>提供视频讲解，在线支持，协助你更好地掌握编程技能。</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.how-it-works {
  padding: 48px 24px 24px;
  background: #fff;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  margin-bottom: 24px;
}
.how-it-works > header {
  font-size: 24px;
  text-align: center;
  margin-bottom: 48px;
}

.how-it-works > .steps-container {
  width: 85%;
  margin-bottom: 24px;
}

@media (max-width: 600px) {
  .how-it-works > .steps-container {
    width: 100%;
  }
}

.how-it-works > .steps-container > .step {
  margin-bottom: 48px;
}

.how-it-works > .steps-container > .step > header {
  font-size: 24px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
    "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif !important;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  letter-spacing: 0.5px;
}

.how-it-works > .steps-container > .step > header > span.number {
  color: #555555;
  margin-right: 12px;
  font-weight: 500;
  font-size: 12px;
  border: 2px solid #ccc;
  border-radius: 50%;
  padding: 3px 0 0 0;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  text-align: center;
  width: 24px;
  height: 24px;
  display: inline-block;
}

.how-it-works > .steps-container > .step > p {
  font-size: 19px;
  color: #555555;
  line-height: 30px;
  padding: 12px 0 0 37px;
}

.how-it-works .badge {
  margin-top: -4px;
  margin-left: 8px;
  position: relative;
  top: 1px;
}

.how-it-works .badge > span {
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  background: #ffce4f;
  border: 2px solid #ffce38;
  border-radius: 5px;
  padding: 2px;
}
</style>