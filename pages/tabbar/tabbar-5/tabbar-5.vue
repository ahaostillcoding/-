<template>
	<view class="content" >
		
		<view class="login" @click.capture="ToLogin">
			<image src="../../../static/img/login.png"></image>
			<div>登录</div>
		</view>
		
			<uni-list class="list">
				<uni-list-item :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'circle-filled'}" :variable="zhiwen_flag" title="指纹登录"  :show-switch="true"  @switchChange="zhiwen" ></uni-list-item>
				<uni-list-item :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'loop'}" title="检查更新" showArrow clickable  @click="onClick" ></uni-list-item>
				<uni-list-item :show-extra-icon="true" showArrow :extra-icon="{color: '',size: '22',type: 'gear'}" title="设置" link to="/pages/login/login"></uni-list-item>
			</uni-list>

	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				zhiwen_flag: -1,
			}
		},
		onLoad: function(option) {
		  const eventChannel = this.getOpenerEventChannel();
		  eventChannel.emit('acceptDataFromOpenedPage', {data: 'data from test page'});
		  eventChannel.emit('someEvent', {data: 'data from test page for someEvent'});
		  // 监听acceptDataFromOpenerPage事件，获取上一页面通过eventChannel传送到当前页面的数据
		  eventChannel.on('acceptDataFromOpenerPage', function(data) {
		    console.log(data)
		  })
		},
		methods: {
			zhiwen() {
				this.zhiwen_flag = -this.zhiwen_flag;
				console.log(this.zhiwen_flag)
			},
			onClick(e) 
			{
				console.log('执行click事件', e.data)
				uni.showToast({
					title: '已经是最新版本'
				});
			},			
			ToLogin() {
				uni.navigateTo({
					url: '/pages/login/login',
					events: {
					    // 为指定事件添加一个监听器，获取被打开页面传送到当前页面的数据
					    acceptDataFromOpenedPage: function(data) {
					      console.log(data)
					    },
					    someEvent: function(data) {
					      console.log(data)
					    }
					  },
					  success: function(res) {
					    // 通过eventChannel向被打开页面传送数据
					    res.eventChannel.emit('acceptDataFromOpenerPage', { data: 'data from starter page' })
					  }
				});
			}
		}
	}
</script>

<style>
	.content {
		text-align: center;
		height: 100upx;
		margin-top: 50upx;
	}
	.list{
		text-align: left;
		height: 400upx;
		margin-top: 150upx;
	}

	.center {
		flex: 1;
		flex-direction: column;
		background-color: #f8f8f8;
	}
	image {
		width: 150rpx;
		height: 150rpx;
	}
	.login {
		text-align: center;
		height: 100upx;
		margi: 50upx;
	}
</style>
