<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-btn icon @click.stop="miniVariant = !miniVariant">
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>

      <v-toolbar-title v-text="title" class=" text-center" />
      <v-spacer />
      <div v-if="this.$auth.loggedIn">
        {{ this.$auth.user.email }}
        <v-btn @click="logout"> logout </v-btn>
      </div>

      <div v-else>
        <nuxt-link to="login"><v-btn>login</v-btn></nuxt-link>

        <nuxt-link to="signup"> <v-btn>sign up</v-btn></nuxt-link>
      </div>
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <v-footer :fixed="fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
      miniVariant: false,
      title: 'Welcome to this nuxt js + django universal app '
    }
  },
  created() {
    try {
      this.$auth.setUser(this.$auth.$storage.getLocalStorage('user'))
    } catch {
      this.$auth.setUser(false)
    }
  },
  methods: {
    async logout() {
      await this.$auth.logout()
      localStorage.removeItem('auth.user')
    }
  }
}
</script>
