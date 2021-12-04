<template>
 <div class="component-section w-100 center">
   <div class="component-section__container w-100">
     <slot></slot>
   </div>
 </div>
</template>

<script>
export default {
  name: "component-section",
}
</script>

<style scoped>
.component-section__container{
   padding: 24px 0;
   width: 90%;
   margin: 0 auto;
   max-width: 900px;
}
</style>
