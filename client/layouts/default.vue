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
import Footer from "../components/custom-footer";
import Header from "../components/custom-header";
import banner from "../components/banner";
import {showSnackbar$} from "../subjects";
import '../assets/styles.scss';

export default {
  data: function(){
    return {
      text: '',
      snackbar: false
    }
  },
  components:{
    Footer,
    Header,
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
