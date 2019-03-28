### 实体字符或特殊字符 ###

	<h3>人民币：元 ￥ &yen; &#165;</h3>
	<h6>大于 &gt;</h6>
	<h5>小于 &lt;</h5>
	<hr>
	<h2>版本 &copy;</h2>

### 表格 ###
	重点学习标签：
		table标签：表格
		caption标签：表格标题
		th标签：行头
		tr标签：行
		td标签：列
			rowspan属性：合并列单元格
			colspan属性：合并行单元格
		thead标签：表头
		tbody标签：表体		
		tfoot标签：表尾


	<!-- 表格属性border:边框  -->
    <table border="1">
        <!-- 表格标题（位置可开始或结束，其效果一致）：caption -->
        <caption>1-8 课程表</caption>
        <!-- 表格行：tr -->
        <thead>
            <!-- 表格头: th -->
            <th>班级名称</th>
            <th>上课地点</th>
            <th>课程名称</th>
        </thead>
        <tbody>
            <tr>
                <!-- 表格列：td -->
                <td>计科1801</td>
                <td>信工楼6012</td>
                <td>前端开发技术</td>
            </tr>
            <tr>
                <td>计科1802</td>
                <!-- 合并列单元格：rowspan -->
                <td rowspan="2">办公楼5016</td>
                <td rowspan="2">数据分析</td>
            </tr>
            <tr>
                <td>计科1803</td>
            </tr>
        </tbody>
        <tfoot>
            <!-- 合并行单元格： colspan -->
            <td colspan="2">制表人</td>
            <td>春花秋月</td>
        </tfoot>
    </table>