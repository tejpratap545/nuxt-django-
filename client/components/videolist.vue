<template>
  <v-app>
    <v-container>
      <v-row>
        <v-col
          v-for="video in videos"
          :key="video.id"
          cols="10"
          sm="6"
          md="4"
          lg="3"
        >
          <div>
            <v-card :to="`/watch/${video.id}`" hover class="mx-auto">
              <v-img
                class="white--text align-end"
                height="200px"
                :src="video.image"
              >
                <v-card-title> {{ video.name }} </v-card-title>
              </v-img>

              <v-card-text class="text--primary">
                <div id="des">{{ video.description }}</div>
              </v-card-text>

              <span>
                <v-btn
                  v-for="tag_id in video.tags"
                  :key="tag_id"
                  :to="`/tag/${tag_id}`"
                  class="btn"
                  small
                >
                  {{ gettag(tag_id).tagname }}
                </v-btn>
              </span>
            </v-card>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {}
  },
  methods: {
    gettag(tagid) {
      return this.tags.find((v) => v.id === tagid)
    }
  },
  props: ['videos', 'tags']
}
</script>

<style>
#des {
  height: 100px;
  overflow: scroll;
}
.btn {
  min-width: 0px;
}
</style>
