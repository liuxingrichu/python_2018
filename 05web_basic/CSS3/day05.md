### 布局之float ###

之前float布局用的多，现在有其他更好的方式实现布局。

[Demo](../CSS_demo/float.html)

	HTML文件：
	    
	    <div class="container">
	        <div class="header">HEADER</div>
	        <div class="menu">MENU</div>
	        <div class="content">CONTENT
	            <div>
	                <h3>left</h3>
	                A man was blissfully driving along the highway, when he saw the Easter Bunny hopping1 across the middle
	                of the road. He swerved to avoid hitting the Bunny, but unfortunately the rabbit jumped in front of his
	                car and was hit. The basket of eggs went flying all over the place.
	                <br>
	                The driver, being a sensitive man as well as an animal lover, pulled over to the side of the road, and
	                got out to see what had become of the Bunny carrying the basket. Much to his dismay, the colorful Bunny
	                was dead. The driver felt guilty and began to cry.
	            </div>
	            <div>
	                <h3>right</h3>
	                A woman driving down the same highway saw the man crying on the side of the road and pulled over. She
	                stepped out of her car and asked the man what was wrong.
	                <br>
	                "I feel terrible," he explained, "I accidentally hit the Easter Bunny and killed it. There may not be an
	                Easter because of me. What should I do?"
	                <br>
	                The woman told the man not to worry. She knew exactly what to do. She went to her car trunk, and pulled
	                out a spray can. She walked over to the limp, dead Bunny, and sprayed the entire contents of the can
	                onto the little furry animal.
	            </div>
	        </div>
	        <div class="footer">FOOTER</div>
	    </div>

	
	CSS文件：

		.container {
		    background-color: aqua;
		}
		
		.header {
		    height: 100px;
		    background-color: blue;
		}
		
		.menu {
		    height: 400px;
		    width: 20%;
		    float: left;
		    background-color: aliceblue;
		}
		
		.content {
		    width: 79%;
		    height: 400px;
		    float: right;
		    background-color: blanchedalmond;
		}
		
		.footer {
		    /* 清除高度崩塌 */
		    clear: both;
		    height: 100px;
		    background-color: cadetblue;
		}
		
		/* 伪元素方式查找元素 */
		.content div:nth-child(1) {
		    float: left;
		    width: 49%;
		}
		
		.content div:nth-child(2) {
		    float: right;
		    width: 49%;
		}