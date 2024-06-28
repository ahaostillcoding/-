<template>
	<view class="content">
		<view @click.capture="lock()">
			<image src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/解锁.png"  />
			<button type="primary">解锁车辆</button>
			
		</view>
		<view @click.capture="open()">
			<image click="open" src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/酒精检测.png" />
			<button @click="open" type="primary">血液酒精含量测试</button>
			<uni-popup ref="popup" type="dialog">
				<uni-popup-dialog mode="base" title="血液酒精含量测试" type="success" content="请在酒精测试仪上进行酒精浓度测试" message="成功消息" :duration="2000" :before-close="true" @close="close" @confirm="confirm"></uni-popup-dialog>
			</uni-popup>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			title: '解锁车辆'
		};
	},
	onLoad() {
		uni.startSoterAuthentication({
			requestAuthModes: ['fingerPrint'],
			challenge: '123456',
			authContent: '请用指纹解锁',
			success(res) {
				console.log(res);
			},
			fail(err) {
				console.log(err);
			},
			complete(res) {
				console.log(res);
			}
		})
	},
	methods: {
		lock: function () {
			var self = this;
			uni.chooseVideo({
				sourceType: ['camera'],
				camera: 'front',
				success: function (res) {
					self.src = res.tempFilePath;
				},
				fail: (err) => {
					// #ifdef MP
					uni.getSetting({
						success: (res) => {
							let authStatus = false;
								authStatus = res.authSetting['scope.camera'];
							if (!authStatus) {
								uni.showModal({
									title: '授权失败',
									content: '解锁车辆需要调用手机摄像头进行人脸识别认证，请在设置界面打开相关权限',
									success: (res) => {
										if (res.confirm) {
											uni.openSetting()
										}
									}
								})
							}
						}
					})
					// #endif
				}
			});
		},
		
		//打开血液酒精含量测试 弹窗提示
		open() {
			this.$refs.popup.open()
			initBt()
		},
			/**
			 * 点击取消按钮触发
			 * @param {Object} done
			 */
		close() {
			// TODO 做一些其他的事情，before-close 为true的情况下，手动执行 close 才会关闭对话框			// ...
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
				
		//刷新
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
		
	//蓝牙连接
	
		// 1. 初始化蓝牙设备 | | 提醒用户打开蓝牙设备
		initBt() {
				var that = this;
				uni.openBluetoothAdapter({ //调用微信小程序api 打开蓝牙适配器接口
					success: function(res) {
						// console.log(res)
						uni.showToast({
							title: '初始化成功',
							icon: 'success',
							duration: 800
						})
						that.findBlue(); //2.0
					},
					fail: function(res) { //如果手机上的蓝牙没有打开，可以提醒用户
						uni.showToast({
							title: '请打开蓝牙',
							type: 'error',
							icon: 'none'
						});
					}
				})
		},
		
		// 2. 搜索周边设备
		findBt() {
			var that = this
			uni.startBluetoothDevicesDiscovery({
				allowDuplicatesKey: false,
				interval: 0,
				success: function(res) {
					uni.showLoading({
					title: '正在搜索设备',
				})
				that.getBlue() //3.0
				}
			})
		},
		
		// 3. 获取搜索到的设备信息
		getBt() {
			var that = this
			//uni.getBluetoothDevices获取在蓝牙模块生效期间所有已发现的蓝牙设备。包括已经和本机处于连接状态的设备
			uni.getBluetoothDevices({
				success: function(res) {
					uni.hideLoading();
					// console.log(res)
					that.BluetoothList = res.devices
					//将BluetoothList遍历给用户，当用户点击连接某个蓝牙时调用4.0
				},
				fail: function() {
					console.log("搜索蓝牙设备失败")
				}
			})
		},
		
		// 4. 当用户点击某个设备时将deviceId进行蓝牙连接
		connetBt(deviceId) {
			// console.log(deviceId)
			var that = this;
			uni.createBLEConnection({
				// 这里的 deviceId 需要已经通过 createBLEConnection 与对应设备建立链接
				deviceId: deviceId, //设备id
				success: function(res) {
					uni.showToast({
					title: '连接成功',
					icon: 'fails',
					duration: 800
				})
				console.log("连接蓝牙成功!-->11111")
				uni.stopBluetoothDevicesDiscovery({
					success: function(res) {
						console.log('连接蓝牙成功之后关闭蓝牙搜索');
					}
				})
				that.deviceId = deviceId;
				that.getServiceId() //5.0
				}
			})
		},
		
		// 5. 连接上需要的蓝牙设备之后，获取这个蓝牙设备的服务uuid
		getServiceId() {
			var that = this
			uni.getBLEDeviceServices({
				// 这里的 deviceId 需要已经通过 createBLEConnection 与对应设备建立链接
				deviceId: that.deviceId,
				success: function(res) {
					console.log(res)
					//需要什么服务就用对应的services 
					that.readyservices = res.services[0].uuid	//因设备而议：该特征值只支持读
					that.services = res.services[1].uuid		//因设备而议：该特征值支持write和notfy服务
					that.getCharacteId() //6.0
				}
			})
		},
		
		// 6. 查看当前蓝牙设备的特征值
		getCharacteId() {
			var that = this
			uni.getBLEDeviceCharacteristics({
				// 这里的 deviceId 需要已经通过 createBLEConnection 与对应设备建立链接
				deviceId: that.deviceId,
				// 这里的 serviceId 需要在上面的 getBLEDeviceServices 接口中获取
				serviceId: that.services,
				success: function(res) {
					console.log(res)
					for (var i = 0; i < res.characteristics.length; i++) { //2个值
						var model = res.characteristics[i]
						if (model.properties.write) {
							//model.uuid:用来写入的uuid值
							//this.sendMy()给设备写入
							that.sendMy(model.uuid)
						}
						if (model.properties.notify) {
							//model.uuid:用来notify的uuid值
							that.notifyUuid = model.uuid
						}
					}
				}
			})
		},
		
		// 7. 启用 notify 功能 接收蓝牙数据
		startNotice() {
			var that = this;
			uni.notifyBLECharacteristicValueChange({
				state: true, // 启用 notify 功能
				// 这里的 deviceId 需要已经通过 createBLEConnection 与对应设备建立链接 
				deviceId: that.deviceId,
				// 这里的 serviceId 需要在上面的 getBLEDeviceServices 接口中获取
				serviceId: that.services,
				// 这里的 characteristicId 需要在上面的 getBLEDeviceCharacteristics 接口中获取
				characteristicId: that.notifyUuid, //第一步 开启监听 notityid  第二步发送指令 write
				success(res) {
					//接收蓝牙返回消息
					uni.onBLECharacteristicValueChange((sjRes)=>{
						// 此时可以拿到蓝牙设备返回来的数据是一个ArrayBuffer类型数据，
						//所以需要通过一个方法转换成字符串
						var nonceId = that.ab2hex(sjRes.value)//10.0
						console.log(sjRes)
						console.log('194行'+nonceId)
					})
				},
				fail(err) {
					console.log(err)
				}
			})
		},
		
		// 8. 将获取的ArrayBuffer数据转换成字符串
		ab2hex(buffer) {
			const hexArr = Array.prototype.map.call(
				new Uint8Array(buffer),
				function (bit) {
					return ('00' + bit.toString(16)).slice(-2)
				}
			)
			return hexArr.join('')
		},





		
	}
};
</script>

<style>
	.content {
		text-align: center;
		margin-top: 100upx;
	}

	button {
		margin:20rpx 100rpx 50rpx 100rpx;
	}
	
	image {
		width: 180px;
		height: 180px;
		mode: aspectFit;
		margin-top: 50rpx;
	}
</style>
