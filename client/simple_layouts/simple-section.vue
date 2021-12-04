<template>
  <section class="section w-100 center">
      <div class="section__container center w-100">
        <div class="section__title text-h2 text-center mb-6 pb-3 text--white" v-if="title && title.length">
          {{title}}
        </div>
        <div class="section__content w-100">
          <slot></slot>
        </div>
      </div>
  </section>
</template>

<script>
export default{
  props:{
    title: String,
    required: false,
    default: ''
  }
}
</script>

<style lang="scss">
.section{
  min-height:93vh;
}

.section__container{
  padding: 48px 0;
  width: 90%;
  margin: 0 auto;
  max-width: 900px;
}
</style>
