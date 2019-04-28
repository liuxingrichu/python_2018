### 布局之position ###

	HTML文件：
	    <p>位置1</p>
	    <div class="box">
	        <p class="abs">位置2：绝对跟着相对走（绝对像）</p>
	    </div>
	    <p>位置3</p>
	
	CSS文件：
		p {
		    color: red;
		    border: 1px solid yellow;
		    padding: 20px;
		    background-color: 4564ff;
		}
		
		.box {
		    width: 200px;
		    height: 200px;
		    position: relative;
		    top: 100px;
		    left: 100px;
		    border: 2px solid red;
		}
		
		.abs {
		    position: absolute;
		    top: 50px;
		    right: 50px;
		}