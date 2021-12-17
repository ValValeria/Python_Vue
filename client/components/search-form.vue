<template>
  <v-layout class="w-100 mb-3"
            justify-center>
    <v-flex md10 xs12 align-self-center>
      <v-text-field
        v-model="search"
        :counter="20"
        label="Search"
        ref="searchField"
        @keyup.enter="submit"
      ></v-text-field>
    </v-flex>
    <v-flex md2 xs12 align-self-center class="ml-2">
      <v-btn @click="submit" class="w-100">Search</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import {searchAction$, showSnackbar$} from "../subjects";

export default {
  data: function() {
    return {
      search: ''
    }
  },
  methods: {
    submit() {
      if(this.search.length < 20) {
        searchAction$.next(this.search);
      } else {
        showSnackbar$.next("The search query must be less than 20 characters.")
      }
    }
  }
}
</script>
