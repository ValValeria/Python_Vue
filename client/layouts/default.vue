<template>
  <v-app>
    <Header/>
    <NavigationDrawer/>
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
      <CustomFooter/>
    </v-main>
  </v-app>
</template>

<script>
import CustomFooter from "../components/custom-footer";
import Header from "../components/custom-header";
import Banner from "../components/banner";
import '../assets/styles.scss';
import NavigationDrawer from "../components/navigation-drawer";

export default {
  data: function(){
    return {
      text: '',
      snackbar: false,
      show: false
    }
  },
  components:{
    NavigationDrawer,
    CustomFooter,
    Header,
    Banner
  }
}
</script>
