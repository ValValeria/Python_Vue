<template>
  <div class="contacts">
    <SimpleSection title="Contacts">
      <div class="w-100 center">
        <div class="contacts__info">
          <v-card flat class="w-100 center">
            <v-card-text>
              <v-form
                class="contacts__form"
                ref="form"
                v-model="valid"
                lazy-validation
              >
                <v-layout justify-center column class="w-100">
                  <v-flex xs10 md6>
                    <v-text-field
                      v-model="username"
                      label="Username"
                      required
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs10 md6>
                    <v-text-field
                      v-model="email"
                      :rules="emailRules"
                      label="E-mail"
                      required
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs10 md6>
                    <v-textarea
                      v-model="message"
                      :rows="5"
                      label="Message"
                      required
                    ></v-textarea>
                  </v-flex>
                  <v-flex  xs10 md4 align-self-center class="mb-2 mt-4">
                    <v-btn
                      color="error"
                      @click="reset"
                      width="150"
                    >
                      Reset
                    </v-btn>
                  </v-flex>
                  <v-flex  xs10 md4  align-self-center>
                    <v-btn
                      @click="submit"
                      width="150"
                    >
                      Submit
                    </v-btn>
                  </v-flex>
                </v-layout>
              </v-form>
            </v-card-text>
          </v-card>
        </div>
      </div>
    </SimpleSection>
  </div>
</template>

<script>
import SimpleSection from "../simple_layouts/simple-section";
import {showSnackbar$} from "../subjects";
export default {
  name: "contacts",
  data: function() {
    return {
      valid: true,
      message: '',
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      username: ""
    }
  },
  components: {SimpleSection},
  mounted() {
    const state = this.$store.state;

    if(state.isAuth && state.user.username){
       this.username = state.user.username;
    }
  },
  methods: {
    reset() {
      this.$refs.form.reset()
    },
    async submit() {
      let message;

      if(this.message.length > 10 && this.message.length < 200) {
        const formData = new FormData();
        formData.append("username", this.username);
        formData.append("email", this.email);
        formData.append("message", this.message);

        const response = await fetch('/api/letter', {
          method: 'POST',
          body: formData
        });

        let message;

        if(response.ok) {
          message = "The letter is delivered to our admin";
        } else {
          message = "Internal error"
        }
      } else {
        message = "The size of message must be between 10 and 200 characters";
      }

      showSnackbar$.next(message);
    }
  }
}
</script>

<style scoped>
.contacts__form, .contacts__info{
  max-width: 600px;
  width: 100%;
}
</style>
