<template>
  <div>
    <SimpleSection title="Error">
      <v-layout align-center justify-center column>
        <v-flex xs12 md5>
          <p class="text--accent-1 text-lg-body-1">
            Sorry, but an error has occurred. Try a little bit later. :(
          </p>
        </v-flex>
        <v-flex xs10 md3 class="mt-3">
          <v-btn @click="navigateBack()">Back</v-btn>
        </v-flex>
      </v-layout>
    </SimpleSection>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";

export default {
  components: {SimpleSection},
  props: ['error'],
  layout: 'error',
  methods: {
    navigateBack() {
      if (this.$router.currentRoute.redirectedFrom === undefined) {
          this.$router.push('/')
      } else {
          this.$router.back();
      }
    }
  }
}
</script>
