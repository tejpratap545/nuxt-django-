export const state = () => ({
  videos: [],
  tags: []
})
export const mutations = {
  SET_VIDEOS(state, videos) {
    state.videos = videos
  },
  SET_TAGS(state, tags) {
    state.tags = tags
  }
}
export const actions = {
  async loadAllVideos({ commit }) {
    const videos = await getData('/video', this.$axios)

    commit('SET_VIDEOS', videos)
  },

  async loadAllTags({ commit }) {
    const tags = await getData('/tag', this.$axios)

    commit('SET_TAGS', tags)
  }
}

export const getters = {}

async function getData(route, $axios) {
  const response = await $axios.get(route)
  return response.data
}
