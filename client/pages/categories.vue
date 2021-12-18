<template>
  <div class="category">
    <SimpleSection title="Category">
      <div class="category__items mb-7 w-100">
         <div v-for="category in categories"
              :key="category.tag"
               class="w-100">
            <v-btn @click="loadByCategory(category)" color="orange" outlined class="w-100">
              <div class="text-lg-h5 text-center">
                 {{category.title}}
              </div>
            </v-btn>
         </div>
      </div>
      <v-layout class="w-100"
                justify-center>
        <v-flex xs12 md12 v-for="post in posts" :key="post.title" class="w-100">
          <PostCard
            :title="post.title"
            :image="post.image"
            :content="post.content"
            :category="post.category"
            :id="post.id"
          />
        </v-flex>
        <v-flex xs1 md1
                v-if="!posts.length && !noPosts"
                align-self-center>
          <v-progress-circular
            :size="50"
            color="amber"
            indeterminate
          ></v-progress-circular>
        </v-flex>
        <v-flex xs12 md12
                v-if="!posts.length && noPosts"
                align-self-center>
          <NoResults/>
        </v-flex>
        <v-flex xs12 md4 v-if="all_pages > 1 && posts.length" class="mt-6" align-self-center>
          <v-btn @click="nextPage()" outlined>More posts</v-btn>
        </v-flex>
      </v-layout>
    </SimpleSection>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
import PostCard from "../components/post-card";
import NoResults from "../components/no-results";

export default {
  name: "categories",
  data: function() {
    return {
      posts: [],
      all_pages: 0,
      page: 1,
      per_page: 10,
      chosenCategory: 0,
      categories: [
        {
          title: "javascript",
          tag: "javascript"
        },
        {
          title: "python",
          tag: "python"
        },
        {
          title: "ml/ds",
          tag: "machine learning"
        },
        {
          title: "android",
          tag: "android development"
        },
        {
          title: "other",
          tag: "other"
        },
        {
          title: "all",
          tag: "all"
        }
      ],
      noPosts: false
    };
  },
  components: {SimpleSection, PostCard, NoResults},
  methods: {
    async nextPage() {
      this.page += 1;

      await this.loadContent();
    },
    async loadContent() {
      const tag = encodeURIComponent(this.categories[this.chosenCategory]?.tag);

      if (tag) {
        const data = await this.$axios.$get(`/api/category/?category=${tag}&page=${this.page}&per_page=${this.per_page}`);

        this.all_pages = data.data.info.all_pages;

        data.data.result.forEach(v => {
           const post = this.posts.find(v1 => v1.id === v.id);

           if(!post){
             this.posts.push(v)
           }
        });

        if(!this.posts.length) {
          this.noPosts = true;
        }
      }
    },
    loadByCategory(category) {
      this.chosenCategory = this.categories.indexOf(category);

      this.page = 1;
      this.posts = [];
      this.all_pages = 1;
      this.noPosts = false;

      this.loadContent();
    }
  },
  mounted() {
    this.loadContent();
  }
}
</script>

<style scoped lang="scss">
.category__items {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: auto;
  grid-gap: 0.5rem;
}
</style>
