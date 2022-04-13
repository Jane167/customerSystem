<template>
    <div class="wrapper">

        <h2 class="title">
            <bk-icon type="dialogue" />
            {{msg}}
        </h2>
        <div class="tabBox">
            <bk-tab :active.sync="active" type="unborder-card">
                <bk-tab-panel v-for="(panel, index) in panels" v-bind="panel" :key="index">
                    <div v-if="panel.name === 'login' " class="loginBox">
                        <bk-form :label-width="100" :model="loginForm">
                            <bk-form-item label="用户名：" :required="true" :property="'username'" :desc="customDesc">
                                <bk-input v-model="loginForm.username" placeholder="请输入用户名"></bk-input>
                            </bk-form-item>
                            <bk-form-item label="密  码：" :required="true" :property="'password'" :desc="customDesc">
                                <bk-input type="password" v-model="loginForm.password" placeholder="请输入密码"></bk-input>
                            </bk-form-item>

                            <bk-form-item label="身  份：" :required="true">
                                <bk-radio-group v-model="loginForm.identity">
                                    <bk-radio :label="'会员'" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'客服'" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'管理员'">
                                    </bk-radio>
                                </bk-radio-group>
                            </bk-form-item>
                            <bk-form-item>
                                <bk-button style="margin-right: 3px;" theme="primary" title="登录" @click.stop.prevent="submitData">登录</bk-button>
                                <bk-button ext-cls="mr5" theme="default" title="取消">取消</bk-button>
                            </bk-form-item>
                        </bk-form>
                    </div>
                    <div v-else-if="panel.name === 'register'" class="registerBox">
                        <bk-form :label-width="100" :model="registerForm">
                            <bk-form-item label="用户名：" :required="true" :property="'username'" :desc="customDesc">
                                <bk-input v-model="registerForm.username" placeholder="请输入用户名"></bk-input>
                            </bk-form-item>
                            <bk-form-item label="密  码：" :required="true" :property="'password'" :desc="customDesc">
                                <bk-input v-model="registerForm.password" type="password" placeholder="请输入密码"></bk-input>
                            </bk-form-item>
                            <bk-form-item label="确认密码：" :required="true" :property="'confirm'" :desc="customDesc">
                                <bk-input v-model="registerForm.confirm" type="password" placeholder="请再次输入密码"></bk-input>
                            </bk-form-item>

                            <bk-form-item label="身  份：" :required="true">
                                <bk-radio-group v-model="registerForm.identity">
                                    <bk-radio :label="'会员'" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'客服'" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'管理员'">
                                    </bk-radio>
                                </bk-radio-group>
                            </bk-form-item>
                            <bk-form-item>
                                <bk-button style="margin-right: 3px;" theme="primary" title="注册" @click="registerAccount">注册</bk-button>
                                <bk-button ext-cls="mr5" theme="default" title="取消">取消</bk-button>
                            </bk-form-item>
                        </bk-form>
                    </div>
                </bk-tab-panel>
            </bk-tab>
        </div>
    </div>
</template>

<script>
export default {
    name: 'login',
    data () {
        return {
            msg: 'welcome to Online customer service management system',
            panels: [
                { name: 'login', label: '登录', count: 10 },
                { name: 'register', label: '注册', count: 20 }
            ],
            active: 'mission',
            loginForm: {
                username: '',
                password: '',
                identity: '',
            },
            registerForm: {
                username: '',
                password: '',
                confirm: '',
                identity: '',
            },
            customDesc: 'hello world'
        }
    },
    method: {
        submitData () {
            alert(JSON.stringify(this.formData))
        },
        changeDate (oldDay, newDay) {
            this.formData.date = newDay
        },
        registerAccount () {
            console.log('reginsterForm', this.registerForm)
            this.$http.get('project/reginster', registerForm).then((res) => {
                console.log(res.data)
            })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
    /* background-image: url('../../images/homepage.jpg'); */
    background: #f56c6c;
    height: 100%;
    overflow: hidden;
    margin: 0;
    padding: 0;
}
.title {
    margin: 0 auto;
    margin-top: 5%;
}
.tabBox {
    width: 30%;
    margin: 0 auto;
    margin-top: 5%;
}
.loginBox {
    margin: 0 auto;
}
.registerBox {
    max-width: 0 auto;
}
</style>
