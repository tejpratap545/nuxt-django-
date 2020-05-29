import RSVP from 'rsvp'
export default async function({ store, from }) {
  const isInitialPageLoad = !from
  if (isInitialPageLoad) {
    await RSVP.all([
      store.dispatch('videos/loadAllVideos'),

      store.dispatch('videos/loadAllTags')
    ])
  }
}
