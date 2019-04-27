### KV编程论：盒模型 ###
- CSS渲染规则
	- 从上到下依次渲染

- 盒模型		box
	- margin	外边距（ma妈妈：大权总揽）
		- border	边框
			- padding	内边距（pa爸爸：管核心）
				- 内容

### 选择器 ###
1. 类选择器
	1. HTML文件中，使用class属性。
	2. CSS文件中，使用点。
	3. HTML文件快速书写方式: div.class_demo

			HTML文件：
				<div class="class_demo">类型选择器中使用class，CSS文件用点</div>
			
			CSS文件：
				.class_demo {
				    /* 字体颜色 */
				    color: green;
				}

2. id选择器
	1. HTML文件中，使用id属性，且一个文件中，id必须唯一。
	2. CSS文件中，使用井号。
	3. HTML文件快速书写方式: div#id_demo

			HTML文件：
				<div id="id_demo">id选择器：在HTML文件中，使用id，在CSS文件中，使用井号</div>

			CSS文件：
				#id_demo {
				    /* 删除线 */
				    text-decoration: line-through;
				}

3. 元素选择器
	1. HTML文件中，正常书写操作标签内容。
	2. CSS文件中，使用标签方式。
	3. 注：全部同一标签都生效。

			HTML文件：
				<p>元素选择器</p>
    			<p>作用于全部同一标签</p>

			CSS文件：
				p {
				    /* 字体加粗 */
				    font-weight: bold;
				}

4. 通用选择器（不建议使用）
	1. HTML文件中，正常书写操作标签内容。
	2. CSS文件中，使用正则表达式方式影响标签内容。
	3. 注：对大型网页使用，有影响。

			CSS文件：
				* {
				    /* 背景色 */
				    background: red;
				}