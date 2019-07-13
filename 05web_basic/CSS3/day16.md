### 案例：动画猫 ###

[HTML文件](../CSS_demo/animation-cat.html)：

	<div class="draw-box">
        <div class="head"></div>
        <div class="ear ear-left"></div>
        <div class="ear ear-right"></div>
        <div class="eye eye-left"></div>
        <div class="eye eye-right"></div>

        <div class="beard one"></div>
        <div class="beard two"></div>
        <div class="beard three"></div>
        <div class="beard four"></div>
        <div class="beard five"></div>
        <div class="beard six"></div>

        <div class="nose"></div>
        <div class="tongue"></div>
    </div>

[CSS文件](../CSS_demo/style/animation-cat.css)：

	.draw-box {
	    position: relative;
	    margin: 0 auto;
	    margin-top: 2%;
	    width: 600px;
	    height: 420px;
	    /* border: 1px solid red; */
	}
	
	.head {
	    /* 绝对跟着相对走 */
	    position: absolute;
	    top: 16.5%;
	    left: 18%;
	    width: 65%;
	    height: 65%;
	    background: #fc9;
    	/* 椭圆 */
	    border-radius: 50%;
	}
	
	.ear {
	    position: absolute;
	    top: 20%;
	    width: 0;
	    height: 0;
    	/* 三角形 */
	    border-left: 30px solid transparent;
	    border-right: 30px solid transparent;
	    border-top: 50px solid #f93;
	}
	
	.ear-left {
	    left: 17%;
	    transform: rotate(135deg);
	}

	.tongue {
	    position: absolute;
	    top: 68%;
	    left: 46%;
	    width: 36px;
	    background-color: #c62323;
	    /* 半圆形 */
	    border-bottom-left-radius: 25px;
	    border-bottom-right-radius: 25px;
	    animation: tongue infinite 0.5s;
	}
	
	@keyframes tongue {
	    0% {
	        height: 0;
	    }
	
	    100% {
	        height: 5%;
	    }
	}