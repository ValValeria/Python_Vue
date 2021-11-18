<template>
  <v-app>
    <Header/>
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
    <Footer/>
  </v-app>
</template>

<script>
import footer from "../components/footer";
import header from "../components/header";
import banner from "../components/banner";
import {showSnackbar$} from "../subjects";

export default {
  data: function(){
    return {
      text: '',
      snackbar: false
    }
  },
  components:{
    Footer: footer,
    Header: header,
    Banner: banner
  },
  mounted(){
    showSnackbar$.subscribe(v => {
      this.snackbar = true;
      this.text = v;
    })
  }
}
</script>
