### html标签：form之二 ###

	重点学习标签：
		input标签：输入框
			submit属性
			reset属性


	<form action="">
        <label for="">
            <!-- minlength：最小长度 -->
            <!-- maxlength：最大长度 -->
            <!-- placeholder：提示信息 -->
            <input type="text" minlength="2" maxlength="10" placeholder="用户名">
        </label>
        <hr>
        <label for="">
            <!-- size：输入框大小 -->
            <input type="text" minlength="2" maxlength="10" size="3" placeholder="提示">
        </label>
        <hr>
        <!-- 单选列表 -->
        <input type="text" list="fruits">
        <hr>
        <input type="text" readonly value="这里只读">
        <input type="password" placeholder="密码提示">
        <!-- type="submit"：提交类型 -->
        <input type="submit">
        <!-- type="reset": 重置 -->
        <input type="reset">
        <input type="button" value="普通按钮">
        <!-- type="number"：数字类型    min: 最小值     value：默认值   step：步长-->
        <input type="number" min="2" max="8" value="3" step="2" name="price">
        <!-- type="range"：滑块 -->
        <input type="range">
    </form>
    <datalist id="fruits">
        <option value="香蕉"></option>
        <option value="苹果"></option>
        <option value="橙子"></option>
    </datalist>

