<template>
  <simple-section :title="post.title">

  </simple-section>
</template>

<script>
import SimpleSection from "../../layouts/simple-section";
export default {
  data: function(){
    return {post: {}}
  },
  components: {SimpleSection},
  async asyncData({params, $http}){
    const id = params.id;
    const url = `/api/posts/${id}`;
    const post = await $http.$get(url);

    return {post};
  }
}
</script>
