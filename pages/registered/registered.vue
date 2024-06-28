<template>
  <view class="registration-container">
    <view class="registration-form">
      <uni-forms ref="form" :modelValue="formData" :rules="rules">
        <uni-forms-item label="账号名" name="name">
          <uni-easyinput type="text" v-model="formData.name" placeholder="请输入账号名" />
        </uni-forms-item>
        <uni-forms-item label="密码" name="password">
          <uni-easyinput type="password" v-model="formData.password" placeholder="请输入密码" />
        </uni-forms-item>
        <uni-forms-item label="确认密码" name="ConfirmPassword">
          <uni-easyinput type="password" v-model="formData.ConfirmPassword" placeholder="请确认密码" />
        </uni-forms-item>
        <button type="primary" class="registration-button" @click="registered">注册</button>
      </uni-forms>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      formData: {},
      rules: {
        name: {
          rules: [
            { required: true, errorMessage: '请输入账号名' },
            { minLength: 3, maxLength: 5, errorMessage: '姓名长度在 {minLength} 到 {maxLength} 个字符' },
          ],
        },
        password: {
          rules: [{ required: true, errorMessage: '请输入密码' }],
        },
        ConfirmPassword: {
          rules: [
            { required: true, errorMessage: '请输入确认密码' },
            { custom: this.validateConfirmPassword, errorMessage: '两次密码不一致' },
          ],
        },
      },
    };
  },
  methods: {
    registered() {
      this.$refs.form.validate().then((res) => {
        console.log('表单数据信息：', res);
        let name = res.name;
        console.log("data", name);
        uni.showToast({
          title: '注册成功',
        });
        setTimeout(() => {
          uni.reLaunch({
            url: '/pages/login/login?data=' + name,
          });
        }, 1000);
      }).catch((err) => {
        console.log('表单错误信息：', err);
      });
    },
    validateConfirmPassword(value, formData) {
      if (value !== formData.password) {
        return {
          valid: false,
          message: '两次密码不一致',
        };
      }
      return {
        valid: true,
      };
    },
  },
};
</script>

<style scoped>
  .registration-container {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    height: 100vh;
  }

  .registration-form {
    background: #fff;
    padding: 50rpx;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 90%; /* 添加一个固定宽度 */
    box-sizing: border-box; /* 将 padding 纳入总宽度 */
  }

  .registration-button {
    width: 100%;
    margin-top: 20px;
  }
</style>

