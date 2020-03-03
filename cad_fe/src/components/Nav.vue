<template>
  <div class="nav">
    <div class="nav-container">
      <div class="logo">
        <a href="/" class="icon">
          <img
            src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgdmVyc2lvbj0iMS4wIgogICB3aWR0aD0iMjVwdCIKICAgaGVpZ2h0PSI0M3B0IgogICB2aWV3Qm94PSIwIDAgMjYxLjM3NzY2IDQzMS4yMjk2OCIKICAgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQgbWVldCIKICAgaWQ9InN2ZzE2Ij4KICA8ZGVmcwogICAgIGlkPSJkZWZzMjAiIC8+CiAgPG1ldGFkYXRhCiAgICAgaWQ9Im1ldGFkYXRhMiI+CiAgICA8cmRmOlJERj4KICAgICAgPGNjOldvcmsKICAgICAgICAgcmRmOmFib3V0PSIiPgogICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2Uvc3ZnK3htbDwvZGM6Zm9ybWF0PgogICAgICAgIDxkYzp0eXBlCiAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vcHVybC5vcmcvZGMvZGNtaXR5cGUvU3RpbGxJbWFnZSIgLz4KICAgICAgPC9jYzpXb3JrPgogICAgPC9yZGY6UkRGPgogIDwvbWV0YWRhdGE+CiAgPGcKICAgICB0cmFuc2Zvcm09Im1hdHJpeCgwLjEsMCwwLC0wLjEsLTQ4Ni40NjIzNSw2MDguMDEzODYpIgogICAgIGlkPSJnMTQiCiAgICAgc3R5bGU9ImZpbGw6IzAzYTlmNDtzdHJva2U6bm9uZSI+CiAgICA8cGF0aAogICAgICAgZD0ibSA2MDIwLDYxMzQgYyAtMjY0LC0zNCAtNDYzLC0xMDQgLTY1NCwtMjMxIC0yNDIsLTE2MSAtNDEyLC0zOTYgLTQ3OCwtNjU5IC0zMSwtMTI0IC0zMSwtMzMyIC0xLC00NTQgMjcsLTEwNSA3NywtMjI2IDEyNywtMzA0IDM1LC01NCA1NCwtMTIzIDI1NCwtODkwIGwgMjE3LC04MzEgNjg3LC0zIDY4NywtMiAxMCwzNyBjIDUsMjEgMzUsMTM3IDY2LDI1OCAzMTEsMTIxMyAzNDUsMTM0MCAzNzksMTM5NSAyMjIsMzYzIDIxOSw3NTkgLTgsMTExMCAtNjMsOTYgLTIwNywyNDQgLTMxNCwzMjAgLTE1NSwxMTAgLTM3MiwyMDAgLTU2OSwyMzYgLTg3LDE1IC0zMzUsMjYgLTQwMywxOCB6IgogICAgICAgaWQ9InBhdGg0IiAvPgogICAgPHBhdGgKICAgICAgIGQ9Im0gNTU0NCwyNjgwIGMgLTMyLC0xMyAtNjQsLTU5IC02NCwtOTEgMCwtMTggMTEsLTQxIDI5LC02MSBsIDI5LC0zMyBoIDYzNiA2MzYgbCAyNywyNyBjIDM4LDM5IDM4LDk3IDAsMTM2IGwgLTI3LDI3IC02MjMsMiBjIC0zNDIsMSAtNjMyLC0yIC02NDMsLTcgeiIKICAgICAgIGlkPSJwYXRoNiIgLz4KICAgIDxwYXRoCiAgICAgICBkPSJtIDU1MzEsMjQwNiBjIC01NiwtMzEgLTY3LC0xMDIgLTIyLC0xNDcgbCAyOSwtMjkgaCA2MzIgYyA0MTQsMCA2MzgsNCA2NTEsMTAgMjksMTYgNTEsNjcgNDQsMTAwIC00LDE2IC0yMCw0MSAtMzcsNTUgbCAtMzAsMjUgaCAtNjIxIGMgLTQ5NywtMSAtNjI3LC0zIC02NDYsLTE0IHoiCiAgICAgICBpZD0icGF0aDgiIC8+CiAgICA8cGF0aAogICAgICAgZD0ibSA1NTk3LDIxMjIgYyAtMzgsLTQwIC0zNywtOTMgMiwtMTMzIGwgMjksLTI5IGggNTQ1IDU0NSBsIDMwLDI1IGMgMTcsMTQgMzMsMzkgMzcsNTUgNywzMyAtMTUsODQgLTQ0LDEwMCAtMTMsNiAtMjExLDEwIC01NjgsMTAgaCAtNTQ5IHoiCiAgICAgICBpZD0icGF0aDEwIiAvPgogICAgPHBhdGgKICAgICAgIGQ9Im0gNTg2NCwxODYzIGMgNTIsLTEwMSAyMjcsLTE2OCAzNzUsLTE0NCAxMDgsMTggMjA1LDczIDI0NCwxNDAgbCAxOCwzMSBoIC0zMjYgLTMyNiB6IgogICAgICAgaWQ9InBhdGgxMiIgLz4KICA8L2c+Cjwvc3ZnPgo="
          />
        </a>
        <a href="/">
          <div class="text">每日一题</div>
        </a>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "navi"
}
</script>

<style>
.nav {
  margin-left: calc(-50vw + 50%);
  width: 100vw;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  padding: 24px;
  background: #fff;
  border-bottom: 2px solid #f1f1f1;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  margin-bottom: 50px;
}
.nav > .nav-container {
    max-width: 960px;
}
.nav>.nav-container, .nav>.nav-container>.logo {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-flex: 1;
    -ms-flex-positive: 1;
    flex-grow: 1;
}

.nav>.nav-container>.logo {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}
.nav>.nav-container>ul.links {
    list-style-type: none;
    padding: 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}

.nav>.nav-container>.logo a {
    text-decoration: none;
}

.nav>.nav-container>.logo .text {
    margin-left: 12px;
    font-size: 24px;
    color: #555;
}

.nav>.nav-container>.logo .icon {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    width: 58px;
    height: 58px;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    justify-content: center;
}
</style>