### 编写规则 ###

[编写规则](http://www.shejidaren.com/css-written-specifications.html)

- 顺序
	1. 位置属性(position, top, right, z-index, display, float等)
	2. 大小(width, height, padding, margin)
	3. 文字系列(font, line-height, letter-spacing, color- text-align等)
	4. 背景(background, border等)
	5. 其他(animation, transition等)
- 可以缩写的，比如padding,margin,font等等，这样精简代码同时又能提高用户的阅读体验。
- 去掉小数点前的“0”
- 简写命名：nav,bg,pwd,
- 16进制颜色代码缩写: #666 (和666666一样)，#abc（aabbcc）
- 规范命名，用a-b的形式，不要a_b
	- 输入的时候少按一个shift键；
	- 浏览器兼容问题 （比如使用_tips的选择器命名，在IE6是无效的）
	- 能良好区分JavaScript变量命名（JS变量命名是用“_”）
- id名称唯一，尽量优先用class
- 为选择器加前缀，随业务和具体组件名称来定


### 从设计到开发的流程 ###

需求-设计-审核-开发-测试（循环）

设计-【标注】-开发

- 微型设计专用工具Dorado



