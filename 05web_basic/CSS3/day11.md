### 转换 ###

转换效果，一般采用工具完成，非自己手写。

- [辅助网址](https://html-css-js.com/css/generator/transform)

举例：

	#demo {
	    /* 火狐浏览器 */
	    -moz-transform: scale(1.1) rotate(76deg) translate(5px, 21px) skew(36deg, 1deg);
	    /* 谷歌浏览器 */
	    -webkit-transform: scale(1.1) rotate(76deg) translate(5px, 21px) skew(36deg, 1deg);
	    /* opera浏览器 */
	    -o-transform: scale(1.1) rotate(76deg) translate(5px, 21px) skew(36deg, 1deg);
	    /* IE浏览器 */
	    -ms-transform: scale(1.1) rotate(76deg) translate(5px, 21px) skew(36deg, 1deg);
	    transform: scale(1.1) rotate(76deg) translate(5px, 21px) skew(36deg, 1deg);
	}

### 过渡 ###

- [第三方效果文件](https://ianlunn.github.io/Hover/)
- 使用方法：
	- 下载并解压Hover-master.zip文件
	- 拷贝hover.css文件，至css文件配置目录
	- 在网页上找到，需要的效果
	- 在hover.css文件中，找到其对应的名称，将其名称，放置到class属性配置中。

html文件举例：

	<link rel="stylesheet" href="style/hover.css">
    <style>
        .btn{
            /* 改为块级标签 */
            display: block;
            /* 兼顾行内标签和块级标签的特性 */
            /* display: inline-block; */
            width: 100px;
            height: 200px;
            background: #567;
        }
    </style>

	<button class="hvr-pulse ">按钮</button>
    <!-- 配置多个属性 -->
    <a class="btn hvr-radial-out hvr-pulse ">a标签的按钮</a>
