// 块级作用域之let
function f5(){
    let n = 5;
    // let n = 1;
    if (true){
        let n = 10;
        console.log(n);
    }
    console.log(n);
}

f5();

function f10(){
    var n = 5;
    var n = 8;
    if (true){
        var n = 10;
        console.log(n);
    }
    console.log(n);
}

f10();

// 块级作用域之const

const name = 'Rex';
// name = 'Dog';
const obj = {};
// obj = [];
obj.name = 'Lily';
obj;

function foo() {
    const a = 1;
    // a = 3;

    function bar() {
        const a = 2;
        console.log(a);
    }
    bar();

    console.log(a);
}

foo();