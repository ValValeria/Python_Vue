<template>
  <v-app-bar
    absolute
    elevate-on-scroll
    black
    app
  >
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

    <v-toolbar-title class="text--black"><b>Dev </b>Prog</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn icon>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>

    <v-btn icon>
      <v-icon>mdi-dots-vertical</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
import {showMenu$} from "../subjects";

export default{
  data: function() {
    return {
      show: false
    }
  },
  computed: {
    drawer: {
      get() {
        return this.show;
      },
      set(value) {
        this.show = value;
        showMenu$.next(value);
      }
    }
  }
}
</script>
