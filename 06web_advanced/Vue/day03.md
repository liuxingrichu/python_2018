### [Vue的事件处理](vue-learn/04-event.html) ###
- 监听DOM，运行js代码，v-on:click="js代码"
- 使用methods对象，添加复杂逻辑，封装函数
	- 无参数		v-on:click="函数名"
	- 有参数		v-on:click="函数名(参数)"
- 事件修饰符
	- stop		停止事件冒泡传播
	- prevent	阻止默认行为
- 按键修饰符
	- v-on:keyup.enter="submit"
	- @keyup.enter="submit"
	- @keyup.on.page-down="onPageDown"

- 好处
	1. 扫一眼HTML模板，便能轻松定位在JavaScript代码里对应的方法。
	2. 因为你无须在JavaScript里手动绑定事件，你的ViewModel代码可以是非常纯粹的逻辑，和DOM完全解耦，更易于测试。
	3. 当一个ViewModel被销毁时，所有的事件处理器都会自动被删除。无须担心，如何清理它们。