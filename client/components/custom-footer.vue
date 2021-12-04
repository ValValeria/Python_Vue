<template>
  <v-footer v-if="show" app>
    <v-card
      flat
      width="100%"
      class="text-center">
      <v-card-text class="white--text">
        {{getTime()}} — <strong>DEV </strong>Prog
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "custom-footer",
  data: function() {
    return {
      show: false
    };
  },
  mounted() {
    this.shouldShow();
  },
  watch: {
    $route(prev, val) {
      this.shouldShow();
    }
  },
  methods: {
    shouldShow() {
      this.show = this.$route.path !== "/";
    },
    getTime() {
      return new Date().getFullYear();
    }
  }
}
</script>

<style scoped>

</style>
