### [自定义指令](vue-learn/05-component.html) ###
通过在

	Vue.directive('名字', {
		钩子函数
	})

注册自定义指令，来对某些元素进行自定义操作。

使用时，用v-名字，放到元素上，类似v-model。