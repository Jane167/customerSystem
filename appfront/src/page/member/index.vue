<template>
    <div class="wrapper">
        <div>
            <h1 style="float: left; margin: 20px">
                <bk-icon style="margin: 20px" type="dialogue" />{{msg}}
            </h1>
            <bk-tag theme="info" style="margin-top: 30px" radius="5px">{{identity}}</bk-tag>
            <bk-fixed-navbar v-if="showNav" style="background: #ebebeb" :position="position" :nav-items="navItems"></bk-fixed-navbar>
        </div>
        <div style="margin-top: 50px">
            <bk-tab :active.sync="active" :type="currentType" style="margin-top: 20px; width: 90%; margin: 0 auto" tab-position="left">
                <bk-tab-panel v-for="(panel, index) in panels" v-bind="panel" :key="index">
                    <div v-if="panel.name==='personCenter'">
                        <div class="card-demo">
                            <bk-card title="我的个人资料" :is-collapse="true" :collapse-icons="icons" :show-foot="true" :show-head="true">
                                <bk-form :label-width="100" :model="personInfo">
                                    <bk-form-item label="昵称:" :property="'nickname'" :desc="customDesc">
                                        <p>{{personInfo.nickname}}</p>
                                    </bk-form-item>
                                    <bk-form-item label="用户名:" :property="'username'" :desc="customDesc">
                                        <p>{{personInfo.username}}</p>
                                    </bk-form-item>
                                    <bk-form-item label="密码:" :property="'password'" :desc="customDesc">
                                        <p>{{personInfo.password}}</p>
                                    </bk-form-item>
                                    <bk-form-item label="个人介绍:" :property="'introduction'" :desc="customDesc">
                                        <p>{{personInfo.introduction}}</p>
                                    </bk-form-item>
                                    <bk-form-item label="创建时间:" :property="'create_time'" :desc="customDesc">
                                        <p>{{personInfo.create_time}}</p>
                                    </bk-form-item>
                                    <bk-form-item label="更新时间:" :property="'update_time'" :desc="customDesc">
                                        <p>{{personInfo.update_time}}</p>
                                    </bk-form-item>
                                </bk-form>
                                <div slot="footer" class="foot-main">
                                    <bk-button theme="primary" title="新增" icon="cog" style="margin-top: 10px" @click='openEditPersonDialog' class="mr10">编辑个人资料</bk-button>
                                </div>
                            </bk-card>
                        </div>
                    </div>
                    <div v-else-if="panel.name==='contactCustomer'">
                        联系客服
                    </div>
                </bk-tab-panel>
            </bk-tab>
        </div>
        <!-- 编辑客服信息dialog -->
        <bk-dialog v-model="editPersonInfo.primary.visible" @confirm="submitEditPersonData" theme="primary" :mask-close="false" :header-position="editPersonInfo.primary.headerPosition" title="编辑个人资料">
            <bk-form :label-width="100" :model="personInfo">
                <bk-form-item label="昵称" :property="'nickname'" :desc="customDesc">
                    <bk-input v-model="personInfo.nickname" placeholder="请输入昵称"></bk-input>
                </bk-form-item>
                <bk-form-item label="用户名" :required="true" :property="'username'" :desc="customDesc">
                    <bk-input v-model="personInfo.username" placeholder="请输入用户名"></bk-input>
                </bk-form-item>
                <bk-form-item label="密码" :required="true" :property="'password'" :desc="customDesc">
                    <bk-input type='password' v-model="personInfo.password" placeholder="请输入密码"></bk-input>
                </bk-form-item>
                <bk-form-item label="个人介绍" :property="'introduction'" :desc="customDesc">
                    <bk-input v-model="personInfo.introduction" placeholder="请输入个人介绍"></bk-input>
                </bk-form-item>
            </bk-form>
        </bk-dialog>
    </div>
</template>

<script>
export default {
    name: 'manager',
    data () {
        return {
            icons: ['icon-right-shape', 'icon-down-shape'],
            status: false,
            msg: 'Welcome to Online customer service management system !',
            identity: '会员',
            panels: [
                { name: 'personCenter', label: '个人中心', count: 10 },
                { name: 'contactCustomer', label: '联系客服', count: 20 },

            ],
            active: 'mission',
            currentType: 'card',
            position: 'middle',
            navItems: [
                {
                    icon: 'icon-dialogue />',
                    text: '退出登录',
                    tooltip: '点击退出登录',
                    action: () => {
                        this.exit()
                        // window.open('http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzgwMDgwMjAwMV80NDMwOTZfODAwODAyMDAxXzJf')
                    }
                },
                {
                    icon: 'icon-star />',
                    text: '评分',
                    tooltip: '点击给客服打分',
                    action: () => {
                        this.exit()
                        // window.open('http://wpa.b.qq.com/cgi/wpa.php?ln=1&key=XzgwMDgwMjAwMV80NDMwOTZfODAwODAyMDAxXzJf')
                    }

                }
            ],
            showNav: true,
            customDesc: ' ',
            personInfo: {
                id: '',
                nickname: '',
                username: '',
                password: '',
                introduction: '',
                create_time: '',
                update_time: ''
            },
            id: '',
            editPersonInfo: {
                primary: {
                    visible: false,
                    headerPosition: 'left'
                }
            },
        }
    },
    created () {
        this.getParams()
    },
    mounted () {

    },
    watch: {
        // 监测路由变化,只要变化了就调用获取路由参数方法将数据存储本组件即可
        '$route': 'getParams'
    },
    methods: {
        exit () {
            setTimeout(() => {
                this.$router.push({
                    name: 'login'
                })
            }, 100)
        },
        getParams () {
            // 取到路由带过来的参数 
            var routerParams = this.$route.params.id
            // 将数据放在当前组件的数据内
            this.id = routerParams
            console.log('mem页面id', this.id)
            this.getMemberInfo()
        },
        getMemberInfo () {
            console.log('接口id', this.id)
            this.$axios.get('project/serach_member_info/', { params: { id: this.id } }).then(res => {
                this.personInfo = res.data.data[0]
                console.log('idresult', res)
            }).catch(error => {
                this.$bkMessage({
                    message: error,
                    theme: 'error'
                })
            });
        },
        openEditPersonDialog () {
            this.editPersonInfo.primary.visible = true
        },
        submitEditPersonData () {
            console.log('personInfo', this.personInfo)
            if (this.personInfo.username === '') {
                this.$bkMessage({
                    message: '用户名不能为空！',
                    theme: 'error'
                })
            } else if (this.personInfo.password === '') {
                this.$bkMessage({
                    message: '密码不能为空！',
                    theme: 'error'
                })
            } else {
                this.$axios.post('project/edit_member_info/', this.personInfo).then(res => {
                    console.log('提交', res);
                    if (res.data.result === true) {
                        this.$bkMessage({
                            message: '修改成功！',
                            theme: 'success'
                        })
                        this.getMemberInfo()
                    } else {
                        this.$bkMessage({
                            message: '修改失败',
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
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
    background: #ffffff;
    height: 100%;
    overflow: hidden;
    margin: 0;
    padding: 0;
}
h1,
h2 {
    font-weight: normal;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
.card-demo {
    width: 400px;
    display: block;
    margin-left: 60px;
}
.bk-card-body p {
    margin-top: 0;
    margin-bottom: 10px;
}
</style>
