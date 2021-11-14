<template>
  <v-app>
    <Header/>
    <v-main>
       <Nuxt/>
    </v-main>
    <Footer/>
  </v-app>
</template>

<script>
import footer from "../components/footer";
import header from "../components/header";
import banner from "../components/banner";

export default {
  components:{
    Footer: footer,
    Header: header,
    Banner: banner
  }
}
</script>
