<template>
  <footer class="footer">
    <div class="copyright">
      <ul>
        <li>
          <a href="/" class="copyright">© 每日一题 2020</a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style>
footer.footer {
    /* margin-top: 48px; */
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