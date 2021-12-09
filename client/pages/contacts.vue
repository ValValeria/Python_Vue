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
                      v-model="email"
                      :rules="emailRules"
                      label="E-mail"
                      required
                    ></v-text-field>
                  </v-flex>
                  <v-flex xs10 md6>
                    <v-textarea
                      v-model="message"
                      :counter="200"
                      :rows="5"
                      :rules="messageRules"
                      label="Name"
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
      messageRules: [
        v => !!v || 'Message is required',
        v => /\d{10,200}/.test(v) || 'Message length must be between 10 and 200 characters',
      ],
    }
  },
  components: {SimpleSection},
  methods: {
    reset() {
      this.$refs.form.reset()
    },
    submit() {

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
