<template>
  <div class="category">
    <SimpleSection title="Category">
      <v-layout justify-center
                align-center
                class="mb-4 w-100">
         <v-flex md3 xs12 v-for="category in categories" :key="category.tag" class="ml-2 mb-2 mr-1">
            <v-card>
              <v-card-text class="text-lg-h5 text-center">
                 {{category.title}}
              </v-card-text>
            </v-card>
         </v-flex>
      </v-layout>
      <v-layout class="w-100">
        <v-flex xs12 md12 v-for="post in posts" :key="post.title" class="w-100">
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
      </v-layout>
    </SimpleSection>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
import PostCard from "../components/post-card";

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
      ]
    };
  },
  components: {SimpleSection, PostCard},
  methods: {
    async nextPage() {
      await this.loadContent();
    },
    async loadContent() {
      const tag = this.categories[this.chosenCategory]?.tag;

      if (tag) {
        const data = await this.$axios.$get(`/api/posts/${tag}?page=${this.page}&per_page=${this.per_page}`);
        data.data.result.forEach(v => {
           const post = this.posts.find(v1 => v1.id === v.id);

           if(!post){
             this.posts.push(v)
           }
        });
      }
    }
  },
  mounted() {
    this.loadContent();
  }
}
</script>

<style scoped>

</style>
