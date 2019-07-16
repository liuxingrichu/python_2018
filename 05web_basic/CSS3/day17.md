### 案例：备忘录 ###
[HTML文件](../CSS_demo/memorandum.html)

	<div class="container">
        <header>
            <nav>
				<ul>
                    <li><a href="#">首页</a></li>
                    <li><a href="#">关于</a></li>
                    <li><a href="#">帮助</a></li>
                </ul>
			</nav>
			<div class="info">
                <button>登录</button>
                <button>注册</button>
            </div>
		</header>
        <div class="wrapper">
            <aside class="sidebar">
				<div class="done">...</div>
				<div class="similar">...</div>
			</aside>
            <section class="main">
                <div class="today-list">...</div>
				<div class="add">...</div>
			</section>
        </div>
        <footer>
            <h3>页脚部分</h3>
            <p>备忘录v0.11</p>
        </footer>
    </div>

[CSS文件](../CSS_demo/style/memorandum.css)

	* {
	    margin: 0;
	    padding: 0;
	    /* 任何盒模型以我指定的为准，任何框大小自己定 */
	    box-sizing: border-box;
	}
	
	a {
	    /* 去除a标签的默认样式 */
	    color: inherit;
	    text-decoration: none;
	}
	
	.container {
	    margin: 0 auto;
	    display: flex;
	    flex-direction: column;
	    background: #fff;
	    /* 内容占100%，使其页脚在页面的最下面 */
	    min-height: 100vh;
	}

	.container a:hover {
		/* 光标变成小手 */
	    cursor: pointer;
	    background-color: blue;
	    color: #fff;
	}

	header {
	    color: #888;
	    padding: 20px;
	    margin-bottom: 10px;
	    border-bottom: 2px solid #456ccc;
	    display: flex;
	    /* 通过空格，分为两部分 */
	    justify-content: space-between;
	}
	
	header nav ul {
	    display: flex;
	    align-items: baseline;
	    /* 除去ul的默认样式 */
	    list-style-type: none;
	}
	
	input[type=checkbox] {
	    /* 放大显示框 */
	    zoom: 180%;
	}