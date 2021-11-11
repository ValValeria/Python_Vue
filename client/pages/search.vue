<template></template>

<script>
export default {
  data: function(){
    return {
      searchQuery: ''
    };
  },
  async asyncData({$http}){
    try{
      const encodedSearch = encodeURIComponent(this.searchQuery);
      const url = `/api/search?page=${this.page}&per_page=${this.per_page}&search=${encodedSearch}`;
      const response = await $http.$get(url);
      const posts = response.data.result;

      return {posts};
    }catch(e){
      console.err(e.message);
    }
  },
  methods:{
    search($event) {
      this.searchQuery = $event.target.value;
      this.$nuxt.refresh();
    }
  }
}
</script>
