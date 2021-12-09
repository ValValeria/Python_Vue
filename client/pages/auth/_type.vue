<template>
  <simple-section title="Authenticate">
    <v-layout justify-center align-center>
      <v-flex xs10 md7>
        <v-card>
          <v-card-text>
            <v-layout column>
              <v-flex xs12 md12>
                <v-tabs centered
                        class="w-100"
                        v-model="tab">
                  <v-tab>Login</v-tab>
                  <v-tab>Sign up</v-tab>
                </v-tabs>
                <v-tabs-items v-model="tab">
                  <v-tab-item v-for="n in 2" :key="n">
                    <AuthForm :tab="tab"/>
                  </v-tab-item>
                </v-tabs-items>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </simple-section>
</template>

<script>
import SimpleSection from "../../simple_layouts/simple-section";
import {mapMutations} from "vuex";
import {LOGIN_MUTATION} from "../../store";
import AuthForm from "../../components/auth-form";

export default {
  data: function(){
    return {
      tab: null
    };
  },
  components: {AuthForm, SimpleSection}
}
</script>

<style scoped lang="scss">
@media all and (min-width: 800px) {
}
</style>

