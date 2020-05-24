// 闭包
function f1(){
    var n = 999;
    function f2(){
        console.log(n);
    }
    return f2;
}

var result = f1();
result();

function createIncrementor(start){
    return function () {
        return start++;
    };
}

var inc = createIncrementor(5);
console.log(inc());
console.log(inc());
console.log(inc());
console.log(inc());