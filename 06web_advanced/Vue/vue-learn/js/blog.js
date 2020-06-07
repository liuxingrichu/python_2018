Vue.component('blog-post', {
    props: ['title', 'content'],
    template: `
    <div>
        <h3>{{ title }}</h3>
        <p>{{ content_short}}</p>
    </div>
    `,
    computed: {
        content_short: function(){
            return this.content.slice(0, 10);
        }
    }
})

Vue.component('blog-header', {
    props: ['title'],
    template: `
    <div>
        <h3>{{ title }}</h3>
    </div>
    `
})

// 自定义指令
Vue.directive('icolor', function(el){
    el.style.color = 'grey';
})

var app = new Vue({
    el: '#blog',
    data: {
        title: 'New Blog One',
        posts: [],
    }, 
    created: function(){
        let that = this;
        // get data throught api
        that.posts = [
            {id:1, title: 'learn Vue', content: 'v-if v-for v-on v-bind component'},
            {id:2, title: 'learn Pyhon', content: 'class def if for else'},
        ]
    }
   
})