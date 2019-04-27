### 颜色 ###
- 颜色表示法
	- 十六进制
		- 以井号开头，三组16进制的红绿蓝颜色双位数值，对光源进行设置的最低值可以是 0（十六进制 00），最高值是 255（十六进制 FF），例如#0fab01。
		- 若两个相同，可简写，例如#aabbcc可简写为#abc。
	- RGB
		- rgb(red, green, blue)。
		- 每个参数 (red、green 以及 blue) 定义颜色的强度，可以是介于 0与255之间的整数，或者是百分比值（从 0% 到 100%），rgb(0,0,255) 和 rgb(0%,0%,100%)。
	- RGBA
		- RGB 颜色值的扩展，带有一个 alpha 通道。它规定了对象的不透明度，alpha 参数是介于 0.0（完全透明）与 1.0（完全不透明）的数字。例如rgba(255,0,0,0.5)
	- 英文单词
		- 使用英语单词，表示颜色，例如red。
	- [配色转换](https://rgbcolorcode.com/)
	- 快捷书写方法
		- w100等效于width: 100px;
		- h200等效于height: 200px;
		- 0.8px等效于.8px
		- font-family 从左向右依次使用，前一个字体不存在考虑下一个字体。
		- 一般规律：单词首字母，从提示中选择。


- 用途
	- border 边框
		- [边框轮廓](https://html-css-js.com/css/generator/border-outline/)
		- [边框弧度](https://html-css-js.com/css/generator/border-radius/)
		- [边框阴影](https://html-css-js.com/css/generator/box-shadow/)
		- -webkit-box-shadow，表示对于内核为webkit的谷歌浏览器类的配置，考虑兼容性。
		- -moz，表示火狐浏览器的配置
		- margin	border	padding参数设置顺序
			- 1个值：上下左右
			- 2个值：上和下，左和右
			- 3个值：上，左和右，下
			- 4个值：上，右，下，左（顺时针）
			- 注：可通过按F12键查看设置情况

					HTML文件：
						<div class="my-border">内外边距</div>
					
					CSS文件：
						.my-border {
						    width: 100px;
						    height: 100px;
						    margin: 10px 20px;
						    border: 1px solid red;
						    padding: 10px 20px 30px;
						}

					HTML文件：
					    <div class="border-image">用图片做边框</div>
					CSS文件：
						.border-image {
						    width: 200px;
						    height: 200px;
						    border: 60px solid gold;
						    /* 边框图片地址 */
						    border-image-source:url(https://mdn.mozillademos.org/files/13060/border-image.png);
						    /* 九宫格：将空间分成九宫格，参数可写数字、百分比 */
						    border-image-slice: 40;
						    /* 重复方式: round 平滑方式 */
						    border-image-repeat: round;
						}

	- 背景
		- [背景生成](https://html-css-js.com/css/generator/background/)
		- [背景渐变](https://html-css-js.com/css/generator/gradient/)

				HTML文件：
					<div class="bg-image">背景色</div>
				    <div class="bg-image-big">背景大图</div>
		
				CSS文件
					.bg-image {
					    width: 300px;
					    height: 200px;
					    /* 背景设置 */
					    background: #DCF51E url(https://html-css-js.com/images/smiley.png) repeat-y scroll 9px 13px;
					    /* 透明度 */
					    opacity: .5;
					}
					
					.bg-image-big {
					    width: 800px;
					    height: 9600px;
					}
					
					body {
					    background: #abc url("https://images.unsplash.com/photo-1533263272401-a58fc34341c2?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max&ixid=eyJhcHBfaWQiOjF9&s=a1bf1441aa5e3d0127583edc12d59880") no-repeat;
					    /* 设置背景图像是否固定或者随着页面的其余部分滚动 */
					    background-attachment: fixed;
					}

	- 文字

