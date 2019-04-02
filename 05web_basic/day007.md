### html标签：form之三 ###

	重点学习标签：
		input标签：输入框
			checkbox类型
			radio类型：结合name属性
			email类型
			tel类型
			url类型
			placeholder属性


	<form action="">
        <label for="">苹果
            <!-- checkbox：复选框 -->
            <!-- checked：复选框的参数，默认选中 -->
            <input type="checkbox" value="" checked>
        </label>
        <label for="">香蕉
            <input type="checkbox">
        </label>
        <label for="">橙子
            <input type="checkbox">
        </label>
    </form>
    <form action="">
        <label for="">奥迪A8
            <!-- radio: 单选按钮 -->
            <input type="radio" name="car">
        </label>
        <label for="">宝马
            <input type="radio" name="car">
        </label>
        <label for="">法拉利
            <input type="radio" name="car">
        </label>
    </form>
    <form action="">
        <label for="">邮箱
            <!-- placeholder: 输入框提示信息 -->
            <!-- pattern： 正则表达式 -->
            <!-- required：必填项 -->
            <input type="email" placeholder="username@abc.com" pattern=".*@abc.com" required>
        </label>
        <label for="">电话
            <input type="tel" placeholder="138-1111-2222">
        </label>
        <label for="">网址
            <input type="url" placeholder="http://www.baidu.com">
        </label>
        <button type="submit">提交</button>
    </form>