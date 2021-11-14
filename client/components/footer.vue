<template>
  <v-footer
     v-if="show"
  >
    <v-card
      flat
      width="100%"
      class="text-center"
    >
      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>DEV </strong>Prog
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "footer",
  data: function(){
    return {
      show: true
    };
  },
  watch: {
    $route: (to, from) => {
      this.show = this.$route.path !== '/';
    }
  }
}
</script>

<style scoped>

</style>
