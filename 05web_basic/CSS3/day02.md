### KV编程论：盒模型 ###
- CSS渲染规则
	- 从上到下依次渲染

- 盒模型		box
	- margin	外边距（ma妈妈：大权总揽）
		- border	边框
			- padding	内边距（pa爸爸：管核心）
				- 内容

### 选择器 ###
1. 类选择器（推荐使用）
	1. HTML文件中，使用class属性。
	2. CSS文件中，使用点。
	3. HTML文件快速书写方式: div.class_demo

			HTML文件：
				<div class="class_demo">类型选择器中使用class，CSS文件用点</div>

				<!-- class有两个属性值，分别为origin，css-front -->
		        <img src="./images/wa.jpg" alt="正面" class="origin css-front">
			
			CSS文件：
				.class_demo {
				    /* 字体颜色 */
				    color: green;
				}

				/* 选中同时有origin和css-front的class属性值的元素 */
				.origin.css-front{
			
				}

				/* CSS文件中，两个配置内容写在一起的方式。注： 任何一个出现书写错误，都不生效 */
				.box1, .box2{
				
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

5. [属性选择器](../CSS_demo/attribute.html)

		常用书写形式:
		
			E[foo]
			E[foo="bar"]		精准匹配
			E[foo~="bar"]		
			E[foo^="bar"]		模糊匹配：以“bar”开头的
			E[foo$="bar"]
			E[foo*="bar"]
		
		HTML文件：
		
		    <input type="text">
		    <br>
		    <input type="text" disabled>
		    <br>
		    <a href="">spring</a>
		    <a href="#">summer</a>
		    <a href="http://www.baidu.com" target="_blank" rel="noopener noreferrer">autumn</a>
		    <a href="#test">winter</a>
		
		CSS文件：
		
		    input[disabled] {
		        cursor: not-allowed;
		    }
		
		    a[href^="#"]{
		        background-color: blue;
		        color: white;
		    }

6. [上下文选择器](../CSS_demo/context.html)

	- 上下文选择器的表达式
		1. e1 e2
			- 选择e1中的后代元素e2	
			- 第一步：取出所有匹配e1表达式的所有元素
			- 第二步：找到e1的所有后代元素
			- 第三步：在e1的所有后代元素中，找出匹配e2表达式的所有元素
		2. e1>e2
			- 选择e1中的子元素e2，是“e1 e2”的特殊情况。
		3. e1~e2
			- 选择e1的后续兄弟元素e2
			- 需要具备的两个条件：
				1. e1与e2，必须是兄弟元素。
				2. e1，e2，有一个先后关系，一定是e1在前面，e2在后面。
		4. e1+e2
			- 选择e1的后续的紧邻兄弟元素e2
			- 需要具备的三个条件：
				1. e1与e2，必须是兄弟元素。
				2. e1，e2，有一个先后关系，一定是e1在前面，e2在后面。
				3. e2是e1是紧邻的关系。
	
		5. 通配符*
			- 匹配任意一个元素
			- 有时，可以起到层次站位的作用。


	注：e1,e2可以是类型选择器、id选择器、class选择器，甚至可能是一个简单的属性选择器。


	HTML文件：
	
	    <ul id="outer">
	        <li>姓名</li>
	        <input type="text">
	        <li>年龄</li>
	        <input type="text" disabled>
	        <li>性别</li>
	        <ul>
	            <li class="inside">男</li>
	            <li class="inside">女</li>
	        </ul>
	        <li>Do you love me?</li>
	        <ul>
	            <li>True</li>
	            <li>False</li>
	        </ul>
	        <li>Which do you like best?</li>
	        <input type="text" disabled>
	    </ul>

	CSS文件：

        /* 选中id为outer的ul元素，其下面的所有li，但不包含里面的ul元素 */
        ul#outer li {
            background-color: blue;
        }

        /* 选中id为outer的ul元素，其下面第一层的所有li，但不包含ul元素里面的li元素 */
        ul#outer>li {
            color: white;
        }

		/* 等效于.inside{} */
        *.inside {
            /* 标签标记不显示 */
            list-style-type: none;
        }

        /* 等效于[disabled]{} */
        *[disabled] {
            cursor: not-allowed;
        }

		/* 要选择ul#outer中，包含的后代元素li，但其包括ul#outer子元素，
        等价于选择其第二代后代元素、第三代后代元素......中的li元素。
        此时，通配符*，起到了层次站位的作用。 */
        ul#outer>* li {
            color: red;
        }

7. [伪类选择器](../CSS_demo/pseudo-class.html)


	第一种：结构化的伪类选择器

		e:first-child		第一个元素
		e:last-child		最后一个元素
		e:nth-child(n)		第n个元素
		
	第二种：UI伪类选择器

		a:visited		已访问的a标签
		a:link			未访问的a标签
		e:hover			被鼠标选中时，生效
		e:focus			元素获得焦点，即在上面操作
		e:checked		一般，用到单选、复选框上。被选中时，选中。
		e:active		元素被激活：鼠标点击到被释放，即中间的一个过程
		e:target		当e元素是通过一个文档类链接导航到的时候，选择e元素


	HTML文件：

		<caption>问卷清单</caption>
	    <ul id="outer">
	        <li>姓名</li>
	        <li>年龄</li>
	        <li>性别
	            <ul>
	                <li>Female</li>
	                <li>Male</li>
	            </ul>
	        </li>
	    </ul>
	    <table border="1">
	        <caption id="score">考试成绩单</caption>
	        <thead>
	            <th>科目</th>
	            <th>姓名</th>
	            <th>成绩</th>
	        </thead>
	        <tbody>
	            ......
	        </tbody>
			<tfoot>
	            <td colspan="2">阅卷人</td>
	            <td>David</td>
	        </tfoot>
	    </table>
	    <a href="#score">查询成绩</a>

	CSS文件：
	
		/* 选择id为outer的ul元素，下面的li子元素中的第一个li元素 */
	    ul#outer>li:first-child {
	        color: red;
	    }
	
	    /* 选择id为outer的ul元素，下面的li子元素中的最后一个li元素 */
	    ul#outer>li:last-child {
	        color: #999;
	    }
	
	    /* 选择id为outer的ul元素，下面的li子元素中的第二个li元素 */
	    ul#outer>li:nth-child(2) {
	        color: green;
	    }
	
	    /* 表格主体部分，奇数行不同颜色显示 */
	    table tbody tr:nth-child(2n+1) {
	        background: #ccc;
	    }
	
	    /* 被鼠标选中 */
	    a:hover {
	        background-color: blue;
	        color: #fff;
	    }
	
	    /* 通过一个文档类链接导航到的时候 */
	    table caption:target {
	        background-color: gold;
	    }

8. [伪元素选择器](../CSS_demo/pseudo-element.html)

	常用伪元素表达式
	
		e::first-letter		第一字符
		e::first-line		首行
		e::before			在文本前
		e::after			在文本后

	CSS文件：

        /* 在文本前添加--，并为红色 */
        h3::before {
            content: "-->";
            color: red;
        }

        /* p标签的首个字符 */
        p::first-letter {
            font-weight: bold;
        }