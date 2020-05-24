// 全局作用域
var a =100;
console.log(a);

function num(){
    b = 200;
    var c = 300;
    console.log(a);
}

num();
console.log(b);
// c is not defined.
console.log(c);