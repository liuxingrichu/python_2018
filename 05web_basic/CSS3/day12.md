### 动画 ###

- [第三方工具](https://daneden.github.io/animate.css/)
	- 使用方法：
		- 选择相应效果，例如tada；
		- 打开animate.css，找到tada的关键帧；
		- 拷贝代码到自己的配置文件；
		- 配置动画效果。

- [其它动画效果](https://envato.com/blog/pure-css-animation-snippets/)


举例：

	<style>
        .blink {
            /* 参数说明：blink是关键帧的名字，infinite是表示永远循环 */
            animation: blink 0.5s infinite;
        }

        @keyframes blink {
            0% {
                color: black
            }

            50% {
                /* 参数说明：transparent表示透明 */
                color: transparent
            }

            100% {
                color: black
            }

        }

        .jump {
            width: 100px;
            height: 100px;
            background-color: #998855;
            animation: tada 1s infinite;
        }

        @keyframes tada {
            from {
                -webkit-transform: scale3d(1, 1, 1);
                transform: scale3d(1, 1, 1);
            }

            10%,
            20% {
                -webkit-transform: scale3d(0.9, 0.9, 0.9) rotate3d(0, 0, 1, -3deg);
                transform: scale3d(0.9, 0.9, 0.9) rotate3d(0, 0, 1, -3deg);
            }

            30%,
            50%,
            70%,
            90% {
                -webkit-transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, 3deg);
                transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, 3deg);
            }

            40%,
            60%,
            80% {
                -webkit-transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, -3deg);
                transform: scale3d(1.1, 1.1, 1.1) rotate3d(0, 0, 1, -3deg);
            }

            to {
                -webkit-transform: scale3d(1, 1, 1);
                transform: scale3d(1, 1, 1);
            }
        }
    </style>


	<p class="blink">一闪一闪亮晶晶，满天都是小星星</p>
    <p class="jump blink tada">跳啊跳</p>


