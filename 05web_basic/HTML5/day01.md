### html标签 ###
- html标签分类（占位）
	1. 块级标签：block
	2. 行内标签：inline
- html标签分类（闭合方式）
	1. 手动闭合标签（多数）
		1. a
		2. span
		3. div
	2. 自闭合标签
		1. img

##### 文本元素 

	重点学习标签：
		a标签：超链接
		span标签：行内空白
		br标签：换行
		img标签：图片
		video标签：视频
		source标签：兼容性
		

	<a href="#">超链接：在本页中，跳转</a>
	<a href="https://codepen.io/pen/">超链接：跳转指定链接，并在当前页面打开</a>
	<a href="https://codepen.io/pen/" target="_blank">超链接：跳转指定链接，并用新标签打开链接</a>

	<img src="图片来源" alt="无法显示照片时，提示信息">
	<img src="web2.0.jpg" alt="无法显示照片时，提示信息">

	<!-- autoplay:  视频在就绪后马上播放-->
	<!-- controls：向用户显示控件，比如播放按钮 -->
	<!-- muted：规定视频的音频输出应该被静音 -->
	<!-- preload：视频在页面加载时进行加载，并预备播放 -->
	<!-- 规定视频下载时显示的图像，或者在用户点击播放按钮前显示的图像。 -->
	<video src="第7讲 字符串.webm" width="360" height="240" controls autoplay muted preload="metadata" poster="web2.0.jpg">视频</video>

	<!-- 兼容性问题 -->
	<h2>添加多个视频源</h2>
	<!-- type：视频格式 -->
	<video width="360" height="240" controls preload="metadata" poster="images/poster.png">
	    <source src="images/timessquare.webm" type="video/webm">    
	    <source src="images/timessquare.ogv" type="video/ogv">    
	    <source src="images/timessquare.mp4" type="video/mp4">    
	</video>

	<b>关键字</b>
	<!-- 换行 -->
	<br>
	<em>强调</em>
	<i>外文词汇或科学相关术语</i>
	<strong>表示重要内容</strong>
	<sup>表示上标文字</sup>
	<sub>表示下标文字</sub>
	<span>行内空白标签</span>
	<ruby>拼音</ruby>
	<del>删除</del>
	<u>下划线</u>
	<mark>加标记</mark>

##### 分组元素 

	重点学习标签：
		div标签：块级空白
		p标签：段落
		ol、li标签：有序列表
		ul、li标签：有序列表
		figure标签：图片
		hr标签：段落级别的分割线
		

	<blockquote>引用</blockquote>
	<!-- 说明列表 -->
	<dl>
	    <dt>计算机</dt>
	    <dd>用来计算的仪器 ... ...</dd>
	    <dt>显示器</dt>
	    <dd>以视觉方式显示信息的装置 ... ...</dd>
	</dl>
	<div>块级空白标签，与span对应</div>
	<!-- 图片 -->
	<figure>
	    <figcaption>1-2 图片标题</figcaption>
	</figure>
	<code>代码</code>
	<!-- 段落级别的分割线 -->
	<hr>
	<!-- 有序列表 -->
	<ol>
	    <li>首先，...</li>
	    <li>其次，...</li>
	    <li>最后，...</li>
	</ol>
	<ul>
	    <li>first</li>
	    <li>second</li>
	    <li>last</li>
	</ul>
	<p>表示段落</p>