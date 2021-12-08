<template>
<div class="category">
  <SimpleSection title="Category">
    <v-layout></v-layout>
  </SimpleSection>
</div>
</template>

<script>
import SimpleSection from "../../simple_layouts/simple-section";
export default {
  data: function() {
    return {
      posts: []
    };
  },
  components: {SimpleSection},
  async asyncData(context) {

  }
}
</script>
