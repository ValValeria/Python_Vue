<template>
<div class="posts w-100">
  <SimpleSection title="Posts">
       <v-layout column
                 class="w-100"
                 justify-center>
         <v-flex xs12 md12 class="mb-6 w-100">
           <PostsCarousel page_type="posts"/>
         </v-flex>
         <template v-if="posts.length && !$fetchState.pending">
           <v-flex xs12 md12 v-for="post in posts" :key="getRandom()" class="w-100">
             <PostCard
               :title="post.title"
               :image="post.image"
               :content="post.content"
               :category="post.category"
               :id="post.id"
             />
           </v-flex>
           <v-flex xs12 md4 v-if="all_pages > 1" class="mt-6" align-self-center>
             <v-btn @click="nextPage()" outlined>More posts</v-btn>
           </v-flex>
         </template>
         <v-flex xs12 md4
                 v-else-if="$fetchState.pending || $fetchState.error"
                 align-self-center>
           <v-progress-circular
             :size="50"
             color="amber"
             indeterminate
           ></v-progress-circular>
         </v-flex>
         <v-flex xs12 md4 v-if="!$fetchState.pending && !posts.length && !$fetchState.error">
           <NoResults/>
         </v-flex>
       </v-layout>
  </SimpleSection>
</div>
</template>

<script>
import SimpleSection from '../simple_layouts/simple-section';
import PostCard from "../components/post-card";
import PostsCarousel from "../components/posts-carousel";
import NoResults from "../components/no-results";

export default {
  data(){
    return {
      page: 1,
      per_page: 10,
      posts: [],
      all_pages: 1
    };
  },
  async fetch(){
    const json = await this.$axios.get(`/api/posts?page=${this.page}&per_page=${this.per_page}`);
    const posts = json.data.data.result;
    this.all_pages = json.data.data.info.all_pages;
    this.posts.push(...posts);
  },
  methods:{
    nextPage() {
      this.page++;
      this.$nuxt.refresh();
    },
    getRandom() {
      return Math.random() ;
    }
  },
  components:{
    NoResults,
    PostsCarousel,
    PostCard,
    SimpleSection
  }
}
</script>
