// 默认参数，放到形参最后
function learnJS(
    func, 
    other, 
    version='ES6'){
        console.log('learn', func, other);
        console.log('当前版本', version);
}

// learnJS('新建, 运行', 'other', version='ES9')
// 本应传参数的，若没有传参，会显示undefined
learnJS()

// rest参数，参数数量不确定
// 原来方式
// function sumAll(a, b){
//     console.log(arguments);
//     return a+b;
// }

// sumAll(1 ,2)

// 新方式
function sumAll(...all){
    console.log(all);
    return all[0] + all[1];
}

sumAll(1 ,2, 1, 2)

// 函数的属性和方法
var otherSum = sumAll;
otherSum(4, 5, 7);
console.log(otherSum.name);
// 仅计算位置参数，不计算默认参数和参数组(...all)
console.log(otherSum.length);
console.log(learnJS.length);

console.log(learnJS.toString());

