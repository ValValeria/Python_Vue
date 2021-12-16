<template>
  <div class="section__form w-100">
    <v-form v-model="valid">
      <v-layout column>
        <v-flex xs12 md12>
          <v-text-field
            v-model="username"
            :rules="rules"
            label="Username"
            required
          ></v-text-field>
        </v-flex>
        <v-flex xs12 md12  v-if="tab !== 0">
          <v-text-field
            v-model="email"
            :rules="rules"
            label="Email"
            type="email"
            required></v-text-field>
        </v-flex>
        <v-flex xs12 md12>
          <v-text-field
            v-model="password"
            :rules="rules"
            type="password"
            label="Password"
            required></v-text-field>
        </v-flex>
        <v-flex md5 xs5 align-self-center>
          <v-btn @click.prevent="submit">Submit</v-btn>
        </v-flex>
      </v-layout>
    </v-form>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
import { mapMutations } from 'vuex'
import {LOGIN_MUTATION} from "../store";
import {showSnackbar$} from "../subjects";

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
    async submit() {
      const urlParams = new URLSearchParams();
      urlParams.append("username", this.username);
      urlParams.append("password", this.password);

      let url = "/api/login"

      if(this.tab === 1) {
         urlParams.append("email", this.email);
         url = "/api/signup"
      }

      const response = await fetch(url, {
        method: 'POST',
        body: urlParams.toString(),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      });

      if(response.ok) {
        const data = await response.json();

        if(data.status === "ok") {
          showSnackbar$.next("You have authenticated successfully");
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
