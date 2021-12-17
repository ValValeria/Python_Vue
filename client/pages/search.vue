<template>
  <div class="search w-100">
    <SimpleSection title="Search">
      <v-layout column
                justify-center>
        <v-flex xs12
                md12
                class="w-100"
                align-self-center>
          <SearchForm/>
        </v-flex>
        <v-flex v-if="!posts.length && !noPosts"
                align-self-center>
          <v-progress-circular
            :size="50"
            color="amber"
            indeterminate
          ></v-progress-circular>
        </v-flex>
        <v-flex v-if="!posts.length && noPosts"
                align-self-center>
          <NoResults/>
        </v-flex>
        <v-flex xs12 md12 v-for="post in posts" :key="post.id" class="w-100">
          <PostCard
            :title="post.title"
            :image="post.image"
            :content="post.content"
            :category="post.category"
            :id="post.id"
          />
        </v-flex>
        <v-flex xs12 md4 v-if="all_pages > 1 && posts.length"
                class="mt-6"
                align-self-center>
          <v-btn @click="nextPage()" outlined>More posts</v-btn>
        </v-flex>
      </v-layout>
    </SimpleSection>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
import {searchAction$, showSnackbar$} from "../subjects";
import SearchForm from "../components/search-form";
import NoResults from "../components/no-results";

export default {
  components: {NoResults, SearchForm, SimpleSection},
  data: function(){
    return {
      searchQuery: '',
      per_page: 10,
      page: 1,
      all_pages: 1,
      posts: [],
      isFirstChange: true,
      noPosts: false
    };
  },
  mounted() {
    searchAction$.subscribe(v => {
      this.searchQuery = v;

      this.posts = [];
      this.all_pages = 1;
      this.per_page = 10;
      this.page = 1;

      this.loadPosts();
    });

    this.loadPosts();
  },
  methods: {
    async loadPosts() {
      const encodedSearch = encodeURIComponent(this.searchQuery || '');
      const url = `/api/search?page=${this.page || 1}&per_page=${this.per_page || 10}&search=${encodedSearch}`;
      const response = await this.$axios.$get(url);
      const data = response.data;
      const posts = data?.result || [];
      const info = data?.info;

      if (posts.length) {
         this.posts = posts;
         this.all_pages = info.all_pages;
         this.noPosts = false;
      } else {
         this.noPosts = true;
      }
    },
    async nextPage() {
      this.page += 1;
      await this.loadPosts();
    }
  }
}
</script>
