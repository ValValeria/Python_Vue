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
  data: () => ({
    items: [
      {
        text: 'Home',
        disabled: false,
        href: '/',
      },
      {
        text: 'Posts',
        disabled: false,
        href: '/posts',
      },
      {
        text: 'Sign up',
        disabled: false,
        href: '/auth/signup'
      },
      {
        text: 'Sign in',
        disabled: false,
        href: '/auth/signin'
      }
    ],
  }),
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
