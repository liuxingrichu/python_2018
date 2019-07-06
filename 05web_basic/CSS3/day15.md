### 案例：明信片开发：正面/反面 ###
- 需求分析
	- 通过CSS配置实现明信片背面开发


[HTML文件](../CSS_demo/postcard.html)：

	<figure>
        <figcaption>正面</figcaption>
        <!-- class有两个属性值，分别为origin，css-front -->
        <img src="./images/wa.jpg" alt="正面" class="origin css-front">
    </figure>


[CSS文件](../CSS_demo/style/postcard.css)：

	/* class属性值为box5，操作的是：其下面的p标签 */
	.box5 p {
	    font-size: 10px;
	    color: #bbb;
	    /* margin值：上，左和右，下 */
	    margin: 0 10px 10px;
	}


	注意：
		CSS文件中，两个配置内容写在一起的方式为
		.box1, .box2{
		
		}


	/* 调整明信片反面显示位置，使其与正面位置同行 */
	.css-post {
	    position: relative;
	    top: -295px;
	}