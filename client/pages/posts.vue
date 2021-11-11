<template></template>

<script>
export default {
  data(){
    return {page: 1, per_page: 10};
  },
  async asyncData(context){
    try{
      const url = `/api/posts?page=${this.page}&per_page=${this.per_page}`;
      const response = await context.app.$http.$get(url);
      const posts = response.data.result;

      return {posts};
    }catch(e){
      console.err(e.message);
    }
  },
  methods:{
    nextPage(){
      this.page++;

      this.$nuxt.refresh();
    },
    prevPage(){
      this.page--;

      this.$nuxt.refresh();
    }
  }
}
</script>
