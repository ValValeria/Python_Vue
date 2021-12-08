<template>
  <simple-section title="Authenticate">
    <v-card>
      <v-card-text>
        <v-layout column justify-center align-center>
          <v-flex xs12>
            <v-tabs center-active class="w-100">
              <v-tab>Login</v-tab>
              <v-tab>Sign up</v-tab>
            </v-tabs>
          </v-flex>
          <v-flex xs12>
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
                  <v-flex xs12 md12>
                    <v-text-field
                      v-model="email"
                      :rules="rules"
                      :counter="10"
                      label="Email"
                      required></v-text-field>
                  </v-flex>
                  <v-flex xs12 md12>
                    <v-text-field
                      v-model="password"
                      :rules="rules"
                      :counter="10"
                      label="Password"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
              </v-form>
            </div>
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
  </simple-section>
</template>

<script>
import SimpleSection from "../../simple_layouts/simple-section";
import {mapMutations} from "vuex";
import {LOGIN_MUTATION} from "../../store";

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

<style scoped lang="scss">
@media all and (min-width: 800px) {
  .section__form{
    min-width: 500px;
  }
}
</style>

