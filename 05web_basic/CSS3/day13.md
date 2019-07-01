### CSS继承与优先级 ###
1. 继承与非继承
	1. 当元素的一个继承属性（inherited property ）没有指定值时，则取父元素的同属性的计算值。
	2. 当元素的一个非继承属性(在Mozilla code 里有时称之为 reset property )没有指定值时，则取属性的初始值。
	3. 每个属性，定义时候有标注是否可继承

2. 下面列表中，选择器类型的优先级是递增的：
	1. 类型选择器（type selectors）（例如, h1）和 伪元素（pseudo-elements）（例如,
::before）
	2. 类选择器（class selectors） (例如 .example)，属性选择器（attributes selectors）（例如 [type="radio"]），伪类（pseudo-classes）（例如 :hover）
	3. ID选择器（例如 #example），元素外部使用css时，优先级最高！
	4. 给元素添加的内联样式 (例如, style="font-weight:bold") 总会覆盖外部样式表的任何样式，因此可看作是具有最高的优先级。

- 注意：
	- 为目标元素直接添加样式，永远比继承样式的优先级高，无视优先级的遗传规则。
	- 优先级是基于选择器的形式进行计算的。
	- 使用 !important 是一个坏习惯，应该尽量避免。


[举例](../CSS_demo/css-tips.html)：

	<style>
        /* ID选择器：id */
        #parent {
            color: green;
        }

        #parent1 {
            color: green;
        }

        #id-h1 {
            color: orange;
        }

        /* 类选择器：class */
        .title {
            color: red;
        }

        /* 类型选择器：元素 */
        h1 {
            color: purple;
        }

        /* ID选择器 */
        * #foo {
            color: green;
        }

        /* 属性选择器 */
        *[id="foo"] {
            color: purple;
        }
    </style>


	<!-- 继承 -->
    <div id="parent1">
        <p>parent</p>
    </div>
    <!-- 优先级 -->
    <div id="parent">
        <h1 class="title" id="id-h1">Here is a title!</h1>
    </div>
    <p id="foo">I am a sample text.</p>


