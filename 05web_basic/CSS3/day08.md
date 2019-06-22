### 布局之grid网格系统 ###

目前未全面普及，处于适用状态。

网格布局，其简单、灵活、强大的工具。

[拔萝卜游戏](https://cssgridgarden.com/#zh-cn)

- 第24关的参考答案

		#garden{
			display: grid;
			grid-template-columns: 50px 1fr 1fr 1fr 50px;
			grid-template-rows: 20% 20% 20% 20% 20%;
		}
		
		#water{
			grid-area: 1 / 1 / 6 / 2;
		}
		
		#poison{
			grid-area: 1 / 5 / 6 / 6;
		}

- 第26关的参考答案

		#garden{
			display: grid;
			grid-template-columns: 20% 20% 20% 20% 20%;
			grid-template-rows: repeat(4, 12.5px) 1fr;
		}
		
		#water{
			grid-column: 1 / 6;
			grid-row: 5 / 6;
		}
		
属性介绍：

grid-column-start: 3;

	描述网格中从左起第三列边界。

grid-column-end:4;

	若仅使用grid-column-start，网格默认只占一列。然而，你可以使用grid-column-end属性将网格拓展到多列。

	注1：end值大于start值时， end值不包括末尾。
	注2：end值可以小于start值。
	注3：end值可以为负数，例如-1来指定为右边的第一列。

grid-column-end:span 2;

	span关键字用来指定所要跨越的宽度。可与grid-column-end、grid-column-start、grid-column一起使用。

grid-column: 2 / 4;

	设置网格项从第二列开始，到第四列结束。

	注1：不包括尾部。
	注2：grid-column-start和grid-column-end两个属性的组合体。

grid-row-start

	其中一件事情使CSS网格布局和Flex盒布局不同的是，你可以很轻松的在二维的空间里定位一个网格项: 行和列。

	grid-row-start就像grid-column-start一样，只不过是在垂直方向指定起始位置。

grid-row

	grid-row同grid-column。

grid-area: 1 / 1 / 3 / 6;

	grid-area属性接受4个由'/'分开的值：grid-row-start, grid-column-start, grid-row-end, 最后是grid-column-end。

	注：grid-area是grid-row和grid-column的结合体。

order：5；

	order属性可重写网格项的顺序，这也是网格布局优于表格布局的好处之一。

	默认情况下，所有的网格项的order都是0，但是顺序也可以被任意设置为正数或者负数，就像z-index一样。

grid-template-columns: 20% 20% 20% 20% 20%;

grid-template-rows: 20% 20% 20% 20% 20%;

	实现了设置每一条规则都有5个值，代表创建了5个列，每一列设置为花园宽度的20%。

	注：grid-template-columns不仅仅只接受百分比的值，也接受像像素或em这样的长度单位。你甚至可以将不同的长度单位混合使用。例如grid-template-columns: 100px 3em 40%;

repeat函数

	grid-template-columns: 20% 20% 20% 20% 20%;属性定义了5列，每列占20%。这可以被简写为：grid-template-columns: repeat(5, 20%);

分数fr

	每一个fr单元分配一个可用的空间。

	比如说，grid-template-columns: 1fr 3fr; 表示空间就会被平均分配为4份；第一个元素占据1/4，第二个元素占据3/4。

	当列的宽度采用像素，百分比或者em的单位的时候，其他使用fr单位设置的列将会平分剩下的空间。

grid-template: 50% 50% / 200px;

	创建一个具有两行的网格，每一行占据50%，以及一个200像素宽的列。

	注：grid-template是grid-template-rows和grid-template-columns的缩写形式。