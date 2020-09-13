<template>
  <div>
    <b-navbar>
      <template slot="brand">
        <b-navbar-item>
          <h1>Selenium Login Test</h1>
        </b-navbar-item>
      </template>
      <template slot="end" v-if="authState === 'signedin'">
        <b-navbar-item tag="div">{{ user.username }}</b-navbar-item>
        <amplify-sign-out></amplify-sign-out>
      </template>
    </b-navbar>
    <section class="section" v-if="!signedIn">
      <div class="container authenticator">
        <amplify-authenticator>
          <amplify-sign-up
            slot="sign-up"
            :form-fields.prop="formFields"
          ></amplify-sign-up>
        </amplify-authenticator>
      </div>
    </section>
    <section class="section" v-else>
      <div class="container">
        <h1 class="title is-1">Hello, {{ user.username }}</h1>
        <div class="content getButton" v-if="!loading && !display">
          <b-button @click="getInfo">Get My Info</b-button>
        </div>
        <div class="content progressBar" v-else-if="loading && !display">
          <progress
            class="progress is-small is-primary"
            max="100"
          >30%</progress>
        </div>
        <div class="content resultTable" v-else>
          <table class="table mt-2">
            <thead>
              <tr>
                <th>属性</th>
                <th>値</th>
              </tr>
            </thead>
            <tbody>
              <tr class="username">
                <td>ユーザー名</td>
                <td>{{ user.username }}</td>
              </tr>
              <tr class="email">
                <td>メールアドレス</td>
                <td>{{ user.attributes.email }}</td>
              </tr>
              <tr class="email-verified">
                <td>メールアドレス確認</td>
                <td>{{ user.attributes.email_verified | emailVefired }}</td>
              </tr>
              <tr class="user-id">
                <td>ユーザーID</td>
                <td>{{ user.attributes.sub }}</td>
              </tr>
            </tbody>
          </table>
          <b-button @click="close" v-if="display">Close</b-button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { onAuthUIStateChange } from '@aws-amplify/ui-components'

export default {
  name: 'App',
  data () {
    return {
      user: undefined,
      authState: undefined,
      loading: false,
      display: false,
      formFields: [
        {
          type: 'username',
          required: true,
        },
        {
          type: 'email',
          required: true,
        },
        {
          type: 'password',
          required: true,
        },
      ]
    }
  },
  created () {
    onAuthUIStateChange((authState, authData) => {
      console.log(authData)
      this.authState = authState
      this.user = authData
      this.loading = false
      this.display = false
    })
  },
  filters: {
    emailVefired (val) {
      return val ? "メール確認済" : "未確認"
    },
  },
  methods: {
    getInfo () {
      this.loading = true
      setTimeout(function () {
        this.loading = false
        this.display = true
      }.bind(this), 3000)
    },
    close () {
      this.loading = false
      this.display = false
    },
  },
  computed: {
    signedIn () {
      return this.authState === 'signedin' && this.user
    },
  },
  beforeDestroy () {
    return onAuthUIStateChange
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.mt-2 {
  margin-top: 2em;
}
.container.authenticator {
  display: flex;
  justify-content: center;
}
</style>
