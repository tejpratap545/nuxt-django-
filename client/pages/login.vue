<template>
  <v-app>
    <div>
      <v-text-field v-model="login.email" label="email"> </v-text-field>
      <v-text-field v-model="login.password" label="password"> </v-text-field>
      <v-btn @click="userLogin">Login</v-btn>
    </div>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      login: {
        email: 'tejpratapsingh545@gmail.com',
        password: '1234'
      }
    }
  },
  methods: {
    userLogin() {
      //   this.$auth
      //     .loginWith('local', {
      //       data: this.login
      //     })
      this.$auth.loginWith('social').then((response) => {
        this.$auth.$storage.setLocalStorage('user', response.data.user)
        this.$auth.setUser(this.$auth.$storage.getLocalStorage('user'))
      })
    }
  }
}
</script>

<style></style>
