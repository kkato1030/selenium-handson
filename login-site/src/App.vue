<template>
  <div>
    <b-navbar>
      <template slot="brand">
        <b-navbar-item>
          <h1>Selenium Login Test</h1>
        </b-navbar-item>
      </template>
      <template slot="end" v-if="signedIn">
        <b-navbar-item tag="div">{{ user.username }}</b-navbar-item>
        <amplify-sign-out></amplify-sign-out>
      </template>
    </b-navbar>
    <section class="section" v-if="!signedIn">
      <div class="container">
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <h1 class="title is-1">Login</h1>
            <form id="login" @submit.prevent="signin">
              <b-field label="Username">
                <b-input v-model="username"></b-input>
              </b-field>
              <b-field label="Password">
                <b-input type="password"
                  v-model="password"
                  password-reveal>
                </b-input>
              </b-field>
              <input
                class="button is-primary"
                :class="{'is-loading': submitting }"
                type="submit"
                value="Login"
                :disabled="!canSignIn"
              >
            </form>
            <div class="message is-danger mt-2" v-if="errMsg">
              <div class="message-body">{{ errMsg }}</div>
            </div>
          </div>
        </div>
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
import { Auth, Hub } from 'aws-amplify'

const getUser = async () => {
  return Auth.currentAuthenticatedUser()
    .then(data => {
      return data
    })
}

export default {
  name: 'App',
  data () {
    return {
      user: undefined,
      submitting: false,
      loading: false,
      display: false,
      username: "",
      password: "",
      errMsg: "",
    }
  },
  async created () {
    try {
      this.user = await getUser()
    } catch (e) {
      console.error(e)
    }
    Hub.listen('auth', function (data) {
      switch (data.payload.event) {
        case 'signIn':
          this.user = data
          break
        case 'signOut':
          this.user = undefined
          break
        default:
          console.log(data)
      }
    }.bind(this))
  },
  filters: {
    emailVefired (val) {
      return val ? "メール確認済" : "未確認"
    },
  },
  methods: {
    async signin () {
      this.submitting = true
      try {
        await Auth.signIn(this.username, this.password)
        this.username = undefined
        this.password = undefined
        this.errMsg = ""
      } catch (err) {
        console.log(err)
        this.errMsg = err.message
      }
      this.submitting = false
    },
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
    canSignIn () {
      return this.username && this.password
    },
    signedIn () {
      return !!this.user
    },
  },
}
</script>

<style>
.mt-2 {
  margin-top: 2em;
}
</style>
