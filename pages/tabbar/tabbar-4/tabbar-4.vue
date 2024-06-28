<template>
	<view class="content">
		我的消息
		<view class="list">
			<uni-list>
				<uni-list-item title="2023/12/8 10:45 解锁车辆失败" link @click="open()" ></uni-list-item>
				<uni-list-item title="2023/12/7 20:33 成功解锁车辆" link @click="open()" ></uni-list-item>
				<uni-popup ref="popup" type="dialog">
					<uni-popup-dialog mode="base" title="血液酒精含量" type="error" content="您的血液酒精含量为25mg/100ml,属于酒后驾驶" message="成功消息" :duration="2000" :before-close="true" @close="close" @confirm="confirm"></uni-popup-dialog>
				</uni-popup>
			</uni-list>
		</view>
		
	</view>
</template>

<script>
	export default {
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {
			setTimeout(() => {
				uni.setTabBarBadge({
					index: 1,
					text: '2'  //设置消息小红点显示消息数量
				});
				uni.showTabBarRedDot({
					index: 3
				});
			}, 1000);
		},
		methods: {
			onClick() {
				console.log("按钮点击")
			},
			function (options) {
					setTimeout(function () {
						console.log('start pulldown');
					}, 1000);
					uni.startPullDownRefresh();
				},
			onPullDownRefresh() {
				console.log('refresh');
				setTimeout(function () {
					uni.stopPullDownRefresh();
				}, 1000);
			},
			open() {
						this.$refs.popup.open()
					},
					/**
					 * 点击取消按钮触发
					 * @param {Object} done
					 */
			close() {
				// TODO 做一些其他的事情，before-close 为true的情况下，手动执行 close 才会关闭对话框
				// ...
				this.$refs.popup.close()
			},
			/**
			 * 点击确认按钮触发
			 * @param {Object} done
			 * @param {Object} value
			 */
			confirm(value) {
				// 输入框的值
				console.log(value)
				// TODO 做一些其他的事情，手动执行 close 才会关闭对话框
				// ...
				this.$refs.popup.close()
			},
		}
	}
</script>

<style>
	.content {
		text-align: center;
		height: 100upx;
		margin-top: 100upx;
	}
	.list {
		text-align: left;
		height: 400upx;
		margin-top: 100upx;
	}
</style>
