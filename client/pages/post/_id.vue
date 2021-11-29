<template>
  <div class="post w-100">
    <SimpleSection :title="post.title" v-if="post.title">
      <div class="w-100" v-if="post.title">
        <div class="post__elements" hidden>
          <p ref="paragraph"></p>
          <h3 ref="title text--h2"></h3>
          <ul ref="code">
            <li hidden></li>
          </ul>
        </div>
        <div class="post__container w-100">
          <div class="post__main-content">
            <v-layout column>
              <v-flex xs12 md12>
                <h3 class="text--white">{{post.title}}</h3>
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
                <div class="post__content" ref="container"></div>
              </v-flex>
            </v-layout>
          </div>
        </div>
      </div>
      <v-layout class="w-100 mt-3" justify-center align-center v-else>
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
  async fetch(context){
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
          await this.$router.push('/');
        });
    }
  },
  methods: {
    loadContent(){
      const elements = {
        container: this.$refs.container,
        paragraph: this.$refs.paragraph,
        code: this.$refs.code,
        title: this.refs.title
      };

      const content = `<root>${this.post.content}</root>`;
      const xmlDoc = new DOMParser().parseFromString(content, 'text/xml');
      const children = Array.from(xmlDoc.childNodes);

      for(let childNode of children){
        let nodeName = childNode.nodeName.toLowerCase();
        let element;

        if(childNode.nodeType === 2){
          element = elements.paragraph.cloneNode(true);
          element.textContent = childNode;
        } else if(nodeName === "code"){
          element = elements.code.cloneNode(true);

          const lines = childNode.textContent.split("\n");

          lines.forEach(v => {
            const lineElement = element.querySelector('li').cloneNode(true);
            lineElement.hidden = false;
            lineElement.textContent = v;

            element.append(lineElement);
          });
        } else if(nodeName === "title"){
          element = elements.title.cloneNode(true);
          element.textContent = childNode.textContent;
        }

        if(element instanceof Node){
          elements.container.append(element);
        }
      }
    }
  }
}
</script>
