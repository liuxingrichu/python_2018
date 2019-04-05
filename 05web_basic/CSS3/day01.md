### CSS简介 ###
1. CSS名称
	1. 层叠样式表
	2. Cascading Style Sheets
2. 目前流行版本：CSS3
3. 原理：当浏览器显示文档时，必须将文档的内容与其样式信息结合。
	1. 浏览器将HTML和CSS转化成DOM（文档对象模型）。DOM在计算机内存中表示文档。DOM将文档内容和其样式结合在一起。
	2. 浏览器显示DOM的内容。
4. 作用：给页面增光添彩。

### 谷歌浏览器样式使用技巧 ###
1. 查看样式
	1. F12
	2. 浏览器空白地方-》右键-》检查（Ctrl + Shift + I）
2. 在网页中，添加临时样式
	1. 在Elements标签页中，可查看源代码
	2. 在下方的Styles标签页中，可手动添加样式，例如color:red;该方式可以立即在网页中查看修改效果，但刷新后失效。
	3. 取消样式前的勾选，样式失效。
	4. 点击样式后的颜色前的显示框，可以选择颜色，也可以从页面上取用颜色样式。
3. 拷贝修改样式，保存到相应文件中
	1. 在Elements标签页中，找到要拷贝内容—>右键-》Copy—》Copy Element
	2. 到相应文件中，粘贴即可。
4. 页面刷新
	1. F5
	2. Ctrl + r
	3. 点击“刷新图标”

### CSS三种使用方式 ###
1. 外部样式表（推荐使用）
	1. 支持多文件公用

			举例：
				在html文件目录下，创建style目录，并在目录下创建color_style.css文件。

			color_style.css文件：
				#outside {
				    color: green;
				}

			HTML文件：
				<head>
				    <meta charset="UTF-8">
				    <meta name="viewport" content="width=device-width, initial-scale=1.0">
				    <meta http-equiv="X-UA-Compatible" content="ie=edge">
				    <title>CSS三种使用方式</title>
				    <link rel="stylesheet" href="style/color_style.css">
				</head>
				
				<body>
				    <h3 id="outside">外部文件：常用：外部样式表</h3>
				</body>

2. 内部样式表
	1. 使用范围：仅能在一个文件内使用
	2. 使用场景：文件内部测试

			举例：
				<head>
				    <meta charset="UTF-8">
				    <meta name="viewport" content="width=device-width, initial-scale=1.0">
				    <meta http-equiv="X-UA-Compatible" content="ie=edge">
				    <title>CSS三种使用方式</title>
				    <style>
				        #inside {
				            color: gold;
				        }
				    </style>
				</head>
				
				<body>
				    <h3 id="inside">头部style：单个文件测试：内部样式表</h3>
				</body>

3. 内部样式
	1. 使用范围：仅对一个标签生效
	2. 使用场景：测试，常用于浏览器中
	
			举例：
				<h3 style="color: #F44336;">使用浏览器：单个元素测试：CSS内联样式</h3>