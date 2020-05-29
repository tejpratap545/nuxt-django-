<template>
  <videolist :videos="videos" :tags="tags"></videolist>
</template>

<script>
import { mapState } from 'vuex'
import videolist from '../components/videolist'
export default {
  components: {
    videolist
  },
  computed: {
    ...mapState({
      videos: (state) => state.videos.videos,
      tags: (state) => state.videos.tags
    })
  }
}
</script>
