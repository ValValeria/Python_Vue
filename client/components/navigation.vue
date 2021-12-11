<template>
  <ComponentSection>
    <div class="w-100">
      <v-breadcrumbs
        class="text--white"
        :items="items"
        large
      />
    </div>
  </ComponentSection>
</template>

<script>
import ComponentSection from "../simple_layouts/component-section";

export default {
  props: {
    items: {
      type: Array
    }
  },
  components: {
    ComponentSection
  }
}
</script>

<style lang="scss">
.v-breadcrumbs__item{
  color: white !important;
}
</style>
