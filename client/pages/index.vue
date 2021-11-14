<template>
 <div class="home w-100">
   <div class="home__banner w-100">
     <SimpleSection>
       <div class="home__content">
         <v-layout column justify-center align-center>
           <v-flex xs12 md12>
             <h1 class="text-h1 text-uppercase text--white text-center mb-6">
               Create your own app from scratch
             </h1>
           </v-flex>
           <v-flex xs12 md8>
             <p class="text-sm-body-1 text-center text--white mb-4">
               Discover languages that gives you the freedom to create, design,
               manage and develop your apps exactly the way you want.
             </p>
           </v-flex>
           <v-flex md3 xs3>
             <v-btn outlined id="btn" block @click="navigateToPosts()">
               Learn more
             </v-btn>
           </v-flex>
         </v-layout>
       </div>
     </SimpleSection>
   </div>
 </div>
</template>

<script>
import SimpleSection from '../simple_layouts/simple-section';

export default {
  components:{
    SimpleSection
  },
  methods:{
    navigateToPosts(){
      this.$router.push('/posts');
    }
  }
}
</script>

<style lang="scss" scoped>
p{
  max-width: 600px;
}

@media(min-width: 1000px){
  .home__banner{
    background-image: url("/background.svg");
    background-size: contain;
  }
}
</style>
