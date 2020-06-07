### [使用component组件化开发](vue-learn/05-component.html) ###
- 组件简介
	- 组件是可复用的Vue实例，有名字
	- 可以复用
	- data必须是一个函数，需要return
	- 需要先注册后使用

			Vue.component('my-component-name', {
			// ... options ...
			})
- 几个重要属性
	- data		在子组件必须是一个函数，需要return
	- template	html页面模板
	- props		一个自定义特性列表，接收传值，作为属性
	- methods	包含多个自定义函数的对象
	- watch		侦听属性，响应数据变动
	- computed	计算属性，响应数据变动，优先采用
	- created	创建组件时，初始化数据
- 父子组件的通信
- 使用vue-cli进行工程化
	- Vue CLI是一个基于Vue.js进行快速开发的完整系统，提供：
		- 通过@vue/cli搭建交互式的项目脚手架。
		- 通过@vue/cli + @vue/cli-service-global快速开始零配置原型开发。
		- 一个运行时依赖（@vue/cli-service），该依赖：
			- 可升级；
			- 基于webpack构建，并带有合理的默认配置；
			- 可以通过项目内的配置文件进行配置；
			- 可以通过插件进行扩展。
		- 一个丰富的官方插件集合，集成了前端生态中最好的工具。
		- 一套完全图形化的构建和管理Vue.js项目的用户界面。
		- https：//cli.vuejs.org/zh/guide/

- 安装最新版cli工具
	- 安装准备：需要安装node.js、npm、webpack
	- 安装：npm install -g @vue/cli
	- 查询： vue --version
	- 创建： vue create vue-blog
	- 在工程目录下，运行： vue run serve