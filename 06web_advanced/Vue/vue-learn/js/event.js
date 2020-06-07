var app = new Vue({
    el:'#app',
    data : {
        counter: 100,
        message: 'hello',
    },
    methods:{
        greet: function (event){
            alert("Welcome!");
            if (event){
                alert(event.target.tagName);
            }
        },
        say: function(msg){
            alert(msg);
        },
        submit: function(data){
            alert(data);
        }
    }
})