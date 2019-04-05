### html标签：form之一 ###

	重点学习标签：
		form标签：表单
		label标签：输入框提示信息
		button标签：按钮
		input标签：输入框
			text属性
			password属性
			

	<!-- action参数：提交地址 -->
    <!-- method参数：提交方式 -->
    <!-- enctype="multipart/form-data"：提交文件 -->
    <form action="" method="GET" enctype="multipart/form-data">
        用户名：<input type="text">
        <br>
        <!-- autocomplete="off"：自动完成，默认开启 -->
        <!-- 输入框文字说明：推荐使用label方式 -->
        <!-- lable的for参数值与input的id参数值一致 -->
        <label for="username">用户名：
            <input type="text" autocomplete="off" id="username">
        </label>
        <button>提交</button>
        <hr>
        <!-- autofocus: 自动聚焦，默认True -->
        <input type="text" autofocus>
        <hr>
        <!-- disabled: 禁止表单 -->
        <input type="text" disabled>
        <!-- 分组显示 -->
        <fieldset>
            <legend>分组</legend>
            <label for="">用户名：
                <input type="text">
            </label>
            <br>
            <label for="">密码：
                <!-- 密码类型 -->
                <input type="password">
            </label>
        </fieldset>
        <button type="reset">重置</button>
    </form>