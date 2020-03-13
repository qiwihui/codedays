<template>
  <div v-if="display">
    <div class="sample-questions">
      <header>编程问题示例</header>
      <div class="question">
        <div class="question-container">
          <div class="question-content">
            <p v-html="question"></p>
          </div>
        </div>
      </div>
    </div>
    <div class="sample-questions">
      <header>解答</header>
      <div class="question">
        <div class="question-container">
          <div class="question-content">
            <p v-html="solution"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SampleQA",
  data() {
    return {
      question: "",
      solution: "",
      display: true
    };
  },
  mounted() {
    this.getSampleQuestionSolution();
  },
  methods: {
    getSampleQuestionSolution() {
      this.$http
        .get("/api/v1/sample_problem")
        .then(response => {
          if (response.status == 200 && response.data.error == false) {
            this.question = response.data.question
            this.solution = response.data.solution
          } else {
            this.display = false
          }
        })
        .catch(() => {
          this.display = false
        })
    }
  }
};
</script>

<style>
.sample-questions {
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
}

.sample-questions > header {
  font-size: 24px;
  text-align: center;
  margin-bottom: 48px;
}

.sample-questions > .question {
  margin-bottom: 24px;
}

.sample-questions > .question > .question-container {
  padding: 24px;
  border-radius: 4px;
  background: #fbfbfb;
  border: 2px solid #f1f1f1;
}

.sample-questions > .question > .question-container > .question-content {
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  font-family: "Computer Modern Serif";
  font-size: 19px;
  line-height: 30px;
  margin: 0 0 24px;
  text-align: left;
}

pre {
  font-size: 16px;
  white-space: pre-wrap;
  overflow-x: scroll;
}

</style>