<template>
  <div class="post w-100">
    <div class="post__elements" hidden>
      <p id="paragraph" class="text-md-body-1"></p>
      <h4 id="title" class="text--h4"></h4>
      <v-card flat id="code">
        <v-card-actions class="code__container pa-3 flex-column justify-start align-start">
          <div hidden class="code__item text-md-body-1 mb-1"></div>
        </v-card-actions>
      </v-card>
    </div>
    <SimpleSection :title="post.title" v-if="post.title">
      <div class="w-100">
        <div class="post__container w-100">
          <div class="post__main-content">
            <v-layout column>
              <v-flex xs12 md12>
                <h3 class="text--white" @click="navigateToCategories()">Category:
                  <span class="text-lg-subtitle-1"> {{post.category}}</span>
                </h3>
              </v-flex>
              <v-flex xs12 md12>
                <v-img
                  :src="post.image"
                  max-height="300"
                  class="w-100"
                >
                  <template v-slot:placeholder>
                    <v-row
                      class="fill-height ma-0"
                      align="center"
                      justify="center"
                    >
                      <v-progress-circular
                        indeterminate
                        color="grey lighten-5"
                      ></v-progress-circular>
                    </v-row>
                  </template>
                </v-img>
              </v-flex>
              <v-flex xs12 md12>
                <div class="post__content" id="container"></div>
              </v-flex>
            </v-layout>
          </div>
        </div>
      </div>
    </SimpleSection>
    <SimpleSection v-else>
      <v-layout class="w-100 mt-3" justify-center align-center>
        <v-progress-circular
          :size="50"
          color="amber"
          indeterminate></v-progress-circular>
      </v-layout>
    </SimpleSection>
  </div>
</template>

<script>
import SimpleSection from "../../simple_layouts/simple-section";
import {showSnackbar$} from "../../subjects";
import {first, interval} from "rxjs";

export default {
  data: function(){
    return {post: {}}
  },
  components: {SimpleSection},
  async asyncData(context) {
    const id = context.params.id;
    const response = await context.$axios.get(`/api/posts/${id}`);
    const data = response.data.data.result[0];

    if(data){
      return {post: data};
    } else {
      showSnackbar$.next('The post doesn\'t exist');

      interval(500)
        .pipe(first())
        .subscribe(async v => {
          await context.$router.push('/');
        });
    }
  },
  async beforeMount(){
    document.addEventListener("readystatechange", () => {
      if (document.readyState === "complete" && this.post.title){
        this.loadContent(this.post);
      }
    });
  },
  methods: {
    loadContent(post){
      const container = document.getElementById('container');
      const paragraph = document.getElementById('paragraph');
      const code = document.getElementById('code');
      const title = document.getElementById('title');

      const content = `<root>${post.content}</root>`;
      const xmlDoc = new DOMParser().parseFromString(content, 'text/xml');
      const children = Array.from(xmlDoc.firstChild.childNodes);

      for(let childNode of children){
        let tagName = childNode.nodeName.toLowerCase();
        let element;

        if(tagName === "#text") {
          element = paragraph.cloneNode(true);
          element.textContent = childNode.textContent;
        } else if(tagName === "code") {
          element = code.cloneNode(true);

          const lines = childNode.textContent.split("\n");

          lines.forEach(v => {
            const lineElement = element.querySelector('div.code__item').cloneNode(true);
            lineElement.hidden = false;
            lineElement.textContent = v;

            element.querySelector('.code__container').append(lineElement);
          });

        } else if(tagName === "title") {
          element = title.cloneNode(true);
          element.textContent = childNode.textContent;
        }

        if (element != null) {
           container.append(element);
        }
      }
    },
    navigateToCategories() {
      this.$router.push(`/category/` + encodeURIComponent(this.post.category));
    }
  },
}
</script>
