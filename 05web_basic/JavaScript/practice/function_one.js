// 定义函数
function hi(){
    console.log('hello!');
}

hi()

function hiname(name){
    console.log(`hello ${name}`)
}

hiname('Tom');

// 匿名函数
(function (name){
    console.log('hello, ', name)
})('Lucy')

// 函数赋值给变量，进行操作
var sayHi = function (name){
    console.log('hello, ', name)
}

sayHi('Lily')

// 函数赋值给对象
let user = {}
user.name = 'David'
user.city = 'London'
user;
user.upperName = function(){
    return this.name.toUpperCase();
}


console.log(user.upperName());
user.name = 'Jim'
console.log(user.upperName());

// 函数作为参数
let aList = [1, 2, 3, 5, 1, 8, 9, 7]
let newList = aList.map(function(x){return x*2});
console.log(newList)

// reduce: 多到1
let sum = aList.reduce(function(x, y){return x+y});
console.log(sum);

// 函数作为返回值
function calcArea(w, h) {
    return w*h
}

function rectInfo(w, h) {
    console.log(`w=${w}, h=${h}的面积为：`);
    return calcArea;
}

var w = 4;
var h = 5;
var area = rectInfo(w, h)(w, h);
console.log(area);