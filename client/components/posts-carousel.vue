<template>
  <v-carousel v-model="model"
              class="w-100"
              height="400"
              v-if="shouldShow ? shouldShow : true">
    <v-carousel-item
      v-for="image in images"
      :key="image.title"
      height="400">
      <v-img
        :src="image.image"
        max-width="100%"
        height="400">
        <template v-slot:placeholder>
          <v-row
            class="fill-height ma-0"
            align="center"
            justify="center">
            <v-progress-circular
              indeterminate
              color="grey lighten-5"
            ></v-progress-circular>
          </v-row>
        </template>
      </v-img>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data: function() {
    return {
      model: 0,
      images: [],
      shouldShow: false
    }
  },
  props: {
    page_type: {
      type: String
    }
  },
  async mounted() {
    await this.load();
  },
  watch: {
    async page_type() {
      await this.load();
    }
  },
  methods: {
    async load() {
      const data = await this.$axios.get(`/api/carousel?page_type=`+encodeURIComponent(this.page_type));
      this.images = data.data.data.result;

      if(this.images && this.images.length) {
        this.shouldShow = true;
      }
    },
  }
}
</script>
