### 模板 ###
- [插值](vue-learn/02-vue-template.html)
	- 使用{{}}，把js中的数据嵌入到html中
	- 文本 {{变量}}
	- js表达式

			{{ number+1 }}
			{{ ok ? 'YES' : 'NO'}}
			{{ message.split('').reverse().join('') }}
			<div v-bind:id="'list-'+id"></div>

- [指令](vue-learn/03-render-bind.html)
	- 指令（Directives）是带有v-前端的特殊特性。
	- 无参数

			v-html="rawHtml"，加载原始html，直接{{}}会当成文本
			v-if
			v-show
			v-for
	- 有参数

			v-bind:href
			v-on:click

- 渲染：条件渲染和列表渲染
	- 条件渲染
	
			v-if="真假（表达式）"
			v-else
			v-else-if
			v-show="真假（表达式）"
	- 列表渲染，使用v-for
		- 数组				v-for="item in items"
		- 获取索引			v-for="(item, index) in items"
		- 对象取值			v-for="value in object"
		- 对象的key与index	v-for="(value, key, index) in object"
		- 用key识别节点		:key="item.di"
		- 数组更新
			- 变异方法（mutation method），改变原始数组，直接用：push，pop，shift，unshift，splice，sort，reverse
			- 非变异（non-mutating method）方法，采用替换旧数组的方式进行：filter(), concat()和slice()

- 绑定：样式绑定和表单绑定
	- 绑定class

			对象：			
				v-bind:class="{ active:isActive }"
				v-bind:class="classObject"
			
			数组：			
				v-bind:class="[activeClass, errorClass]"
				v-bind:class="[{active:isActive}, errorClass]"

	- 绑定style

			对象：
				v-bind:style="{ color:activeColor, fontSize:fontSize+'px'}"
			数组：
				v-bind:style="[baseStyles, overridingStyles]"
	- 表单绑定


			用v-model指令在表单<input><textarea><select>元素上，创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。

			修饰符：lazy、number、trim