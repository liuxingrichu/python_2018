### 元素使用原则 ###
1. 元素小写
2. 属性：空格，双引号
3. 嵌套元素，注意格式化，每一段落
4. 别误用元素
5. 实体符合全文统一，名称优先
6. 注释只在最必要时候才加
7. 风格一致，section还是div：看项目历史情况
8. 不确定的内容，都用div或span
9. 结构化思考
10. 属性：KV编程论

### html标签：form之四 ###

	重点学习标签：
		input标签：输入框
			date类型：日期
			image类型：图片
		select标签：下拉框
		textarea标签：写评论
		form标签：表单
			enctype="multipart/form-data：文件上传

	<form action="">
        <label for="">时间类型
            <input type="date">
        </label>
        <br>
        <label for="">颜色类型
            <!-- value属性：默认颜色值，16进制形式 -->
            <input type="color" value="#10f0f0">
        </label>
        <br>
        <label for="">隐藏类型
            <input type="hidden" name="">
        </label>
        <br>
        <label for="">图片类型
            <input type="image" src="web2.0.jpg" alt="web2相关技术" name="picture">
        </label>
        <br>
        <lable for="fruit">单选下拉框
            <select name="fruit" id="fruit">
                <option value="apple">苹果</option>
                <option value="banana">香蕉</option>
                <!-- selected: 默认选择 -->
                <option value="orange" selected>橙子</option>
            </select>
        </lable>
        <br>
        <lable for="fruit">多选下拉框
            <select name="fruit" id="fruits" multiple>
                <option value="apple">苹果</option>
                <option value="banana">香蕉</option>
                <option value="orange">橙子</option>
            </select>
        </lable>
        <br>
        <label for="">多行文本，可用于评论
            <!-- cols: 列， rows：行 -->
            <textarea name="" id="" cols="30" rows="10"></textarea>
        </label>
    </form>


	<form action="" enctype="multipart/form-data">
        <label for="">上传文件
            <input type="file" name="" id="">
        </label>
        <button>上传</button>
    </form>