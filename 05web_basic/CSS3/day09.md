### 布局之grid实践 ###

[Demo](../CSS_demo/grid.html)

	HTML文件：

		<div class="container">
	        <header>HEADER</header>
	        <div class="menu">menu</div>
	        <div class="content">content</div>
	        <div class="side">side</div>
	        <footer>FOOTER</footer>
	    </div>


	CSS文件：

		.container {
		    display: grid;
		    /* 经典分布为12列 */
		    grid-template-columns: repeat(12, 1fr);
		    grid-template-rows: 60px 300px 100px;
		    grid-gap: 5px;
		    /* 分布布局，点代表空白站位 */
		    grid-template-areas:
		        "h h h h h h h h h h h h"
		        ". m m c c c c c c s s ."
		        "f f f f f f f f f f f f";
		}
		
		header {
		    background: rgb(24, 88, 151);
		    color: white;
		    text-align: center;
		    grid-area: h;
		}
		
		footer {
		    background-color: rgb(134, 73, 73);
		    grid-area: f;
		    text-align: center;
		}
		
		div {
		    border: 3px solid rgb(187, 255, 0);
		    margin: 5px;
		    padding: 5px;
		    background-color: rgb(136, 187, 16);
		}
		
		.menu {
		    grid-area: m;
		    background-color: #456;
		}
		
		.content {
		    grid-area: c;
		    background-color: #4ac;
		}
		
		.side {
		    grid-area: s;
		    background-color: #abc;
		}