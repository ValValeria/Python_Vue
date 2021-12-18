<template>
<div class="about">
  <SimpleSection title="About me">
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>
            Valeria Di
          </v-card-title>
          <v-card-subtitle>
            Programmer/ UI Designer
          </v-card-subtitle>
          <v-card-text>
            Hi, I'm Valeria, a passionate self-taught Full Stack web developer and a freelance software engineer from Ukraine. My passion for software lies with dreaming up ideas and making them come true with elegant interfaces. I take great care in the experience, architecture, and code quality of the things I build. I am also an open-source enthusiast and maintainer. I learned a lot from the open-source community and I love how collaboration and knowledge sharing happened through open-source.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card>
            <v-card-actions>
              <v-btn color="orange" outlined rounded @click="navToGithub()">Visit my github profile</v-btn>
              <v-btn color="orange" outlined rounded @click="navToContactPage()">Contact me</v-btn>
              <v-btn color="orange" outlined rounded @click="mailMe()">Mail me</v-btn>
            </v-card-actions>
          </v-card>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-parallax
          dark
          src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
        >
          <v-row
            align="center"
            justify="center"
          >
            <v-col
              class="text-center"
              cols="12"
            >
              <h1 class="text-h4 font-weight-thin mb-4">
                Dev Prog
              </h1>
              <h4 class="text-lg-body-1">
                Build your application today!
              </h4>
            </v-col>
          </v-row>
        </v-parallax>
      </v-col>
    </v-row>
  </SimpleSection>
</div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
export default {
  name: "about",
  components: {SimpleSection},
  methods: {
    navToGithub() {
      if (process.client) {
        window.open('https://github.com/ValValeria')
      }
    },
    navToContactPage() {
      this.$router.push('/contacts')
    },
    mailMe() {
      if (process.client) {
        window.open('mailto:led2017l@gmail.com')
      }
    }
  }
}
</script>

<style scoped>

</style>
