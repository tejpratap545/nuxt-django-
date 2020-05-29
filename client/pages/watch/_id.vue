<template>
  <v-app>
    <VideoWatch :video="video" />
    {{ video }}
  </v-app>
</template>

<script>
import { mapState } from 'vuex'
import VideoWatch from '../../components/VideoWatch'

export default {
  data() {
    return {
      VideoWatch
    }
  },
  computed: {
    ...mapState({
      videos: (state) => state.videos.videos
    }),
    video() {
      return this.videos.find((v) => v.id === this.$route.params.id)
    }
  },

  components: { VideoWatch },
  methods: {}
}
</script>

<style></style>
