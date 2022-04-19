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
                                    <bk-radio :label="'会员'" value="0" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'客服'" value="1" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'管理员'" value="2">
                                    </bk-radio>
                                </bk-radio-group>
                            </bk-form-item>
                            <bk-form-item>
                                <bk-button style="margin-right: 3px;" theme="primary" title="登录" @click="loginAccount">登录</bk-button>
                                <bk-button ext-cls="mr5" theme="default" title="取消" @click="cancelLogin">取消</bk-button>
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
                                    <bk-radio :label="'会员'" value="0" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'客服'" value="1" class="mr20">
                                    </bk-radio>
                                    <bk-radio :label="'管理员'" value="2">
                                    </bk-radio>
                                </bk-radio-group>
                            </bk-form-item>
                            <bk-form-item>
                                <bk-button style="margin-right: 3px;" theme="primary" title="注册" @click="registerAccount">注册</bk-button>
                                <bk-button ext-cls="mr5" theme="default" @click="cancelRegister" title="取消">取消</bk-button>
                            </bk-form-item>
                        </bk-form>
                    </div>
                </bk-tab-panel>
            </bk-tab>
        </div>
    </div>
</template>

<script>
import axios from '../../assets/js/axios'

export default {
    name: 'login',
    data () {
        return {
            msg: '欢迎来到企业在线客服管理系统！',
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
            customDesc: ' ',
            member_id: '',
            customer_id: ''
        }
    },
    create: {
    },
    methods: {
        submitData () {
            alert(JSON.stringify(this.formData))
        },
        changeDate (oldDay, newDay) {
            this.formData.date = newDay
        },
        loginAccount () {
            console.log('loginForm', this.loginForm)
            if (this.loginForm.username === '') {
                this.$bkMessage({
                    message: '用户名不能为空，请重新登录！',
                    theme: 'warning'
                })
            } else if (this.loginForm.password === '') {
                this.$bkMessage({
                    message: '密码不能为空，请重新输入！',
                    theme: 'warning'
                })
            } else if (this.loginForm.identity === '') {
                this.$bkMessage({
                    message: '请选择你的身份！',
                    theme: 'warning'
                })
            }
            else {
                //调用登录接口
                this.$axios.post('project/login_authentication/', this.loginForm).then(res => {
                    if(res.data.id){
                        var id = res.data.id
                        console.log('ididididid:', id)
                    }
                    console.log(res);
                    if (res.data.result === true) {
                        this.$bkMessage({
                            message: '登录成功！',
                            theme: 'success'
                        })
                        if (this.loginForm.identity == '0') {
                            this.member_id = id
                            console.log('member_id', id)
                            setTimeout(() => {
                                this.$router.push({
                                    name: 'member',
                                    params: {
                                        id: this.member_id
                                    }
                                })
                            }, 100)
                        } else if (this.loginForm.identity == '1') {
                            this.customer_id = id
                            console.log('customer_id', this.customer_id)
                            setTimeout(() => {
                                this.$router.push({
                                    name: 'customer',
                                    params: {
                                        id: this.customer_id
                                    }
                                })
                            }, 100)
                        } else {
                            setTimeout(() => {
                                this.$router.push({
                                    name: 'manager'
                                })
                            }, 100)
                        }
                    } else {
                        this.$bkMessage({
                            message: '用户名或密码错误，请重新登录！',
                            theme: 'error'
                        })
                    }
                }).catch(error => {
                    this.$bkMessage({
                        message: error,
                        theme: 'error'
                    })
                });
            }

        },
        cancelLogin () {
            this.loginForm.username = ''
            this.loginForm.password = ''
            this.loginForm.identity = ''
            this.$bkMessage({
                message: '您已取消登录！',
                theme: 'primary'
            })
        },
        registerAccount () {
            console.log('reginsterForm', this.registerForm)
            if (this.registerForm.username === '') {
                this.$bkMessage({
                    message: '用户名不能为空，请重新输入！',
                    theme: 'error'
                })
            }
            else if (this.registerForm.password === '') {
                this.$bkMessage({
                    message: '密码不能为空，请重新输入！',
                    theme: 'warning'
                })
            }
            else if (this.registerForm.confirm === '') {
                this.$bkMessage({
                    message: '确认密码不能为空，请重新输入！',
                    theme: 'warning'
                })
            } else if (this.registerForm.identity === '') {
                this.$bkMessage({
                    message: '请选择你要注册的身份！',
                    theme: 'warning'
                })
            } else if (this.registerForm.password !== this.registerForm.confirm) {
                this.$bkMessage({
                    message: '两次密码不一致，请重新输入！',
                    theme: 'error'
                })
            } else {
                //调用注册接口
                this.$axios.post('project/register/', this.registerForm).then(res => {
                    console.log(res);
                    if (res.data.result === true) {
                        this.$bkMessage({
                            message: '注册成功！',
                            theme: 'success'
                        })
                    } else {
                        this.$bkMessage({
                            message: '注册失败',
                            theme: 'error'
                        })
                    }
                }).catch(error => {
                    this.$bkMessage({
                        message: error,
                        theme: 'error'
                    })
                });

            }

        },
        cancelRegister () {
            this.registerForm.username = ''
            this.registerForm.password = ''
            this.registerForm.confirm = ''
            this.registerForm.identity = ''
            this.$bkMessage({
                message: '您已取消注册操作！',
                theme: 'primary'
            })
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
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
