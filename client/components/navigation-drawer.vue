<template>
  <v-navigation-drawer v-model="show"
                       app>
    <v-list link>
      <v-subheader class="text-md-h6 text-center w-100">Menu</v-subheader>
      <v-list-item v-for="item in links"
                   :key="item.title"
                   @click="navigate(item.path)">
        <v-list-item-title class="text-md-body-1">
          {{item.title}}
        </v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import {showMenu$, showSnackbar$} from "../subjects";

export default {
  name: "navigation-drawer",
  data: function() {
    return {
      show: false,
      links: [
        {path: "/", title: "Home"},
        {path: "/posts", title: "Posts"},
        {path: "/categories", title: "Categories"},
        {path: "/contacts", title: "Contacts"},
        {path: "/about", title: "About me"},
      ]
    }
  },
  mounted(){
    showSnackbar$.subscribe(v => {
      this.snackbar = true;
      this.text = v;
    });

    showMenu$.subscribe(v => {
      this.show = v;
    });
  },
  methods: {
    navigate(path) {
      this.$router.push(path);
    }
  }
}
</script>

<style scoped>

</style>
