<template>
  <div class="contacts">
    <SimpleSection title="Contacts">
      <v-layout justify-center class="w-100">
        <v-flex xs12 md6>
          <v-form
            ref="form"
            v-model="valid"
            lazy-validation
          >
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>

            <v-text-field
              v-model="message"
              :counter="10"
              :rules="messageRule"
              label="Name"
              required
            ></v-text-field>

            <v-btn
              color="error"
              class="mr-4"
              @click="reset"
            >
              Reset Form
            </v-btn>

            <v-btn
              color="warning"
              @click="submit"
            >
              Submit
            </v-btn>
          </v-form>
        </v-flex>
      </v-layout>
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
    reset () {
      this.$refs.form.reset()
    }
  }
}
</script>

<style scoped>

</style>
