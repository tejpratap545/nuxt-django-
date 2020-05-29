<template>
  <!-- <div
    class="video-player-box"
    v-video-player:videoPlayer="playerOptions"
  ></div> -->
  <vue-plyr>
    <div class="plyr__video-embed">
      <iframe
        :src="video.video_url"
        allowfullscreen
        allowtransparency
        allow="autoplay"
      >
      </iframe>
    </div>
  </vue-plyr>
</template>

<script>
// import 'video.js/dist/video-js.css'

// import Vue from 'vue'
// if (process.browser) {
//   const VueVideoPlayer = require('videojs-youtube')
//   import { videoPlayer } from 'vue-video-player'

//   Vue.use(VueVideoPlayer)
// }
export default {
  computed: {
    // playerOptions() {
    //   return {
    //     language: 'en',
    //     techOrder: ['youtube'],
    //     playbackRates: [0.7, 1.0, 1.5, 2.0, 2.5, 3.0],
    //     sources: [
    //       {
    //         type: 'video/youtube',
    //         src: 'https://youtu.be/cRF7hIsIO10'
    //       }
    //     ],
    //     poster: this.video.image,
    //     fluid: true
    //   }
    // }
  },
  props: ['video']
}
</script>
