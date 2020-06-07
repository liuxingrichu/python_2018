var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue! Nice to meet you!',
    name: 'Tom' + 'aaabbbccc',
    todo: 'learn Vue',
    isBusy: false,
    myhtml: "<p style='color:red'>This is pure html</p>",
    
    isShow: false,
    username: 'Jim',

    todolist: [
      {date:'1.1', thing: "New Year's Day"},
      {date:'5.1', thing: "International Labour Day"},
      {date:'6.1', thing: "Children's Day"},
      {date:'8.1', thing: "Army Day"},
    ],
    user: {
      username: 'Tom',
      password: '123',
      age: 18,
      city: 'New York'
    },

    test1: {
      active: true,
    },
    test2: {
      active: false,
      error: true
    },
    activeClass: 'active',
    errorClass: 'error',

    log: '焦点移开显示',
    num: '字符转数字',
    trimstr: '去两端空白'
  }
})

app.todolist.push({date:'10.1', thing: "National Day"})

// find  from March to Auguest
d = new Date()
app.todolist = app.todolist.filter(item => { 
  return d.setDate(item.date) >= d.setDate('3.1') && d.setDate(item.date) < d.setDate('9.1')
})