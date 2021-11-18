<template>
  <div class="post w-100">
    <simple-section :title="post.title">
      <div class="post__elements" hidden>
        <p ref="paragraph"></p>
        <h3 ref="title"></h3>
        <ul ref="code">
          <li hidden></li>
        </ul>
      </div>
      <div class="post__content w-100" ref="container"></div>
    </simple-section>
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
  async mounted(){
    const id = this.$route.params.id;
    const response = await this.$axios.get(`/api/posts/${id}`);
    const data = response.data.data.result[0];

    if(data){
      this.post = data;
    } else {
      showSnackbar$.next('The post doesn\'t exist');

      interval(500)
        .pipe(first())
        .subscribe(async v => {
           await this.$router.push('/');
        });
    }
  },
  watch:{
    post(newPost, prevPost){
       const elements = {
         container: this.$refs.container,
         paragraph: this.$refs.paragraph,
         code: this.$refs.code,
         title: this.refs.title
       };

       const content = `<root>${newPost.content}</root>`;
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
