<template>
  <section class="section">
      <section class="section__container">
        <section class="section__title">
          {{title}}
        </section>
        <section class="section__content">
          <slot></slot>
        </section>
      </section>
  </section>
</template>

<script>
export default{
  props:{
    title: String
  }
}
</script>
