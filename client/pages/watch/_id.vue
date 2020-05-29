<template>
  <v-app>
    <VideoWatch :video="video" />
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
      const id = parseInt(this.$route.params.id)

      return this.videos.find((v) => v.id === id)
    }
  },

  components: { VideoWatch },
  methods: {}
}
</script>

<style></style>
