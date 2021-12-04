<template>
  <v-app>
    <Header/>
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
    <v-main>
      <v-snackbar
        v-model="snackbar"
      >
        {{ text }}

        <template v-slot:action="{ attrs }">
          <v-btn
            text
            v-bind="attrs"
            @click="snackbar = false"
          >
            Close
          </v-btn>
        </template>
      </v-snackbar>
      <Nuxt/>
    </v-main>
    <CustomFooter/>
  </v-app>
</template>

<script>
import CustomFooter from "../components/custom-footer";
import Header from "../components/custom-header";
import banner from "../components/banner";
import {showMenu$, showSnackbar$} from "../subjects";
import '../assets/styles.scss';

export default {
  data: function(){
    return {
      text: '',
      snackbar: false,
      links: [
        {path: "/", title: "Home"},
        {path: "/posts", title: "Posts"},
        {path: "/contact", title: "Contacts"}
      ],
      show: false
    }
  },
  components:{
    CustomFooter,
    Header,
    Banner: banner
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
