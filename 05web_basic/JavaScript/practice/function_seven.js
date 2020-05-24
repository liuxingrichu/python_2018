// var提升变量
function foo(x){
    // var tmp;
    if (x > 100) {
        var tmp = x - 100;
        // tmp = x - 100;
    }
    console.log(tmp);
}

foo(200);

// demo two

var tmp = new Date();

function f(){
    // var tmp;
    console.log(tmp); //undefined
    if (false) {
        var tmp = 'hello';
        // tmp = 'hello';
    }
}

f();

// demo three

var s = 'hello';

for (var i=0; i<s.length; i++){
    console.log(s[i]);
}

console.log(i);

for (let j=0; j<s.length; j++){
    console.log(s[j]);
}

console.log(j); // j is not defined