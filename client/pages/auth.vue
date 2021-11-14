<template>
  <simple-section title="Authenticate">
   <v-tabs>
     <v-tab>Login</v-tab>
     <v-tab>Sign up</v-tab>
   </v-tabs>
    <div class="section__form">
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                v-model="username"
                :rules="rules"
                :counter="10"
                label="Username"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                v-model="email"
                :rules="rules"
                :counter="10"
                label="Email"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                v-model="password"
                :rules="rules"
                label="Password"
                required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
  </simple-section>
</template>

<script>
import { mapMutations } from 'vuex';
import {LOGIN_MUTATION} from "../store/";
import SimpleSection from "../simple_layouts/simple-section";

export default {
  data: function(){
    return {
      valid: false,
      email: '',
      password: '',
      username: '',
      rules: [
        v => v.trim().length > 10 && v.trim().length < 30
      ]
    };
  },
  components: {SimpleSection},
  methods:{
    ...mapMutations(LOGIN_MUTATION)
  }
}
</script>
