// this 关键字
var obj_this = {name: 'Tom'}
obj_this.doSomeThing = function() {
    console.log(this);
    var that = this;
    function test(){
        // 使用that来指向obj_this对象
        console.log(this);
        console.log(that);
    }
    test();
}

obj_this.doSomeThing();


function hello(){
    console.log(this);
    obj = {};
    obj.f = function test(){
        console.log(this);
    }
    obj.f();
}

hello();
