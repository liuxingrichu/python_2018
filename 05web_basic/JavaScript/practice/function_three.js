// 变量解构赋值
// let [a, b, c] = [1, 2, 3];
// a;
// b;
// c;

// let [x,,y] = [1, 2, 3]
// x;
// y;

// let [x, y='b']=['a'];
// x;
// y;

let [x, y='b'] = ['a', undefined];
x;
y;

let {foo, baz} = {foo:'aaa', baz:'bbb'};
foo;
baz;

const [a, b, c, d, e] = 'hello';
a;
b;
c;
d;
e;

let {length:len} = 'hello';
len;

// 得到返回值
function example(){
    return [1,3,5];
}

let [ea, eb, ec] = example();
ea;
eb;
ec;

// 返回对象
function obj() {
    return {
        name:'Jim',
        age: 16
    }
}

let {name, age} = obj();
name;
age;