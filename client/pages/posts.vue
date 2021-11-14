<template>
<div class="posts w-100">
  <SimpleSection title="Posts">
       <v-layout column class="w-100">
         <v-flex xs12 md12 v-for="post in posts" :key="Math.random()">
           <PostCard
             :title="post.title"
             :image="post.image"
             :content="post.content"
             :category="post.category"
             :id="post.id"
           />
         </v-flex>

         <v-flex xs12 md4 v-if="posts.length" class="mt-6" align-self-center>
            <v-btn @click="nextPage()" outlined>More posts</v-btn>
         </v-flex>
       </v-layout>
  </SimpleSection>
</div>
</template>

<script>
import SimpleSection from '../simple_layouts/simple-section';
import PostCard from "../components/post-card";

export default {
  data(){
    return {page: 1, per_page: 10, posts: []};
  },
  async fetch(){
    const json = await this.$axios.get(`/api/posts?page=${this.page}&per_page=${this.per_page}`);
    const posts = json.data.data.result;
    console.log(json)
    this.posts.push(...posts);
  },
  methods:{
    nextPage(){
      this.page++;

      this.$nuxt.refresh();
    },
  },
  components:{
    PostCard,
    SimpleSection
  }
}
</script>
