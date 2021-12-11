<template>
  <div class="section__form w-100">
    <v-form v-model="valid">
      <v-layout column>
        <v-flex xs12 md12>
          <v-text-field
            v-model="username"
            :rules="rules"
            :counter="10"
            label="Username"
            required
          ></v-text-field>
        </v-flex>
        <v-flex xs12 md12  v-if="tab === 0">
          <v-text-field
            v-model="email"
            :rules="rules"
            :counter="10"
            label="Email"
            type="email"
            required></v-text-field>
        </v-flex>
        <v-flex xs12 md12>
          <v-text-field
            v-model="password"
            :rules="rules"
            :counter="10"
            type="password"
            label="Password"
            required></v-text-field>
        </v-flex>
        <v-flex md5 xs5 align-self-center>
          <v-btn>Submit</v-btn>
        </v-flex>
      </v-layout>
    </v-form>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
import { mapMutations } from 'vuex'
import {LOGIN_MUTATION} from "../store";

export default {
  data: function() {
    return {
      valid: false,
      email: '',
      password: '',
      username: '',
      rules: [
        v => v.trim().length > 10 && v.trim().length < 30
      ],
    }
  },
  name: "auth-form",
  props: {
    tab: {
      required: true,
      type: Number
    }
  },
  components: {
    SimpleSection,
    ...mapMutations([
      LOGIN_MUTATION
    ])
  },
  methods:{
  }
}
</script>

<style scoped>

</style>
