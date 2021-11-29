<template>
  <div class="post-card mb-4 w-100">
    <v-card
      class="w-100"
      outlined
      flat>
      <v-card-title>{{title}}</v-card-title>
      <v-card-subtitle>Category: {{category}}</v-card-subtitle>
      <v-img height="250" :src="image"/>
      <v-card-text>
        {{content.slice(0, 30)}}
      </v-card-text>
      <v-card-text>
        <v-btn @click="navigate()">Read more</v-btn>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default{
  props: {
    id: {
      type: Number
    },
    image: {
      type: String
    },
    category: {
      type: String
    },
    content: {
      type: String
    },
    title: {
      type: String
    }
  },
  methods: {
    navigate(){
      this.$nextTick(async () => {
        await this.$router.push(`/post/${this.id}`);
      });
    }
  }
}
</script>
