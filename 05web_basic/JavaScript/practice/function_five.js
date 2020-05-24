// 局部作用域
function num(){
    var c = 300;
    console.log(c);
    function test(){
        console.log(c);
        // console.log(d);
    }
    test();
}

// console.log(c);
num();

// 定义时作用域
var a = 1;
var x = function(){
    console.log(a);
};

function f () {
    var a = 2;
    console.log(a);
    x();
}

f()