<template>
	<view class="login-container">
		<view class="avatar-container">
			<image class="avatar" src="https://typoranote-picture.oss-cn-guangzhou.aliyuncs.com/typora图片/智安行.jpg">
			</image>
		</view>
		<view class="form-container">
			<uni-forms ref="form" :modelValue="formData" :rules="rules">
				<uni-forms-item label="用户名" name="name">
					<uni-easyinput type="text" v-model="formData.name" placeholder="请输入用户名" />
				</uni-forms-item>
				<uni-forms-item label="密码" name="password">
					<uni-easyinput type="password" v-model="formData.password" placeholder="请输入密码" />
				</uni-forms-item>
			</uni-forms>
			<view class="button-container">
				<button type="primary" class="login-button" @click="submit">登录</button>
			</view>
		</view>
		<view class="link-container">
			<view class="link-item" @click="registered">
				<text class="register-link">还没有账号？点击注册</text>
			</view>
		</view>
	</view>
</template>


<script>
export default {
  data() {
    return {
      formData: {
        name: '',
        password: '',
      },
      rules: {
        name: {
          rules: [
            { required: true, errorMessage: '请输入账号' },
            { minLength: 3, maxLength: 5, errorMessage: '姓名长度在 {minLength} 到 {maxLength} 个字符' },
          ],
        },
        password: {
          rules: [{ required: true, errorMessage: '请输入密码' }],
        },
      },
    };
  },
  onLoad: function (option) {
    if (option.data != null) {
      var result = JSON.parse(option.data);
      console.log('传送数值', result);
      this.formData.name = result;
    }
  },
  methods: {
    submit() {
      this.$refs.form.validate()
        .then(res => {
          console.log('表单数据信息：', res);
		  uni.reLaunch({
		  	url: '/pages/tabbar/tabbar-1/tabbar-1',
		  });
        })
        .catch(err => {
          console.log('表单错误信息：', err);
        });
    },
    registered() {
      uni.navigateTo({
        url: '/pages/registered/registered',
        events: {
          acceptDataFromOpenedPage: function (data) {
            console.log(data);
          },
          someEvent: function (data) {
            console.log(data);
          },
        },
        success: function (res) {
          res.eventChannel.emit('acceptDataFromOpenerPage', { data: 'data from starter page' });
        },
      });
    },
  },
};
</script>

<style scoped>
	.login-container {
		margin-top: 50px;
		display: flex;
		flex-direction: column;
		align-items: center;
		/* justify-content: center; */
		height: 100vh;
	}

	.avatar-container {
		margin-bottom: 10px;
	}

	.avatar {
		width: 80px;
		height: 80px;
		border-radius: 50%;
	}

	.form-container {
		background-color: #fff;
		padding: 30rpx;
		width: 300px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.button-container {
		display: flex;
		justify-content: center;
		margin-top: 30px;
	}

	.login-button {
		width: 50%;
		height: 40px;
		border-radius: 20px;
		font-size: 16px;
	}

	.link-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin-top: 20px;
	}

	.link-item {
		margin-bottom: 10px;
	}

</style>