<template>
    <div class="wrapper">
        <div>
            <h1 style="float: left; margin: 20px">
                <bk-icon style="margin: 20px" type="dialogue" />{{msg}}
            </h1>
            <bk-tag theme="info" style="margin-top: 30px" type="stroke" radius="5px">{{identity}}</bk-tag>
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
                        <bk-table style="margin-top: 15px;" :data="customerList">
                            <bk-table-column type="index" label="id" width="60"></bk-table-column>
                            <bk-table-column label="昵称" prop="nickname"></bk-table-column>
                            <bk-table-column label="用户名" prop="username"></bk-table-column>
                            <bk-table-column label="个人介绍" prop="introduction"></bk-table-column>
                            <bk-table-column label="创建时间" prop="create_time"></bk-table-column>
                            <bk-table-column label="更新时间" prop="update_time"></bk-table-column>
                            <bk-table-column label="操作" width="150">
                                <template slot-scope="props">
                                    <bk-button class="mr10" theme="primary" text @click="openChatDialog(props.row)">
                                        <bk-icon type="dialogue-empty" />
                                        联系
                                    </bk-button>
                                    <bk-button class="mr10" theme="primary" text @click="openScoreDialog(props.row)">
                                        <bk-icon type="star" />
                                        评分
                                    </bk-button>
                                </template>
                            </bk-table-column>
                        </bk-table>
                    </div>
                </bk-tab-panel>
            </bk-tab>
        </div>
        <!-- 编辑人个人资料信息dialog -->
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
        <!-- 聊天dialog -->
        <bk-dialog v-model="chatToCustomer.primary.visible" 
        @confirm="sendToCustomer" theme="primary" 
        :mask-close="false" 
        :header-position="chatToCustomer.primary.headerPosition" 
        title="聊天框"
        ok-text="发送"
        cancel-text="关闭"
        fullscreen='true'
        :auto-close='false'
        >
            <bk-form :label-width="100" :model="personInfo">
                <bk-form-item :property="'records'" :desc="customDesc" style="margin-top: 200">
                    <div id="chat-log">
                        <div class="senderMes">
                            <bk-tag theme="success">我</bk-tag><br>
                            <span>{{chatToCustomer.message}}</span>
                        </div>
                        <div class="receiverMes">
                            <bk-tag theme="info">我的</bk-tag><br>
                            <span>这是消息</span>
                        </div>
                        <div class="senderMes">
                            <bk-tag theme="success">我</bk-tag><br>
                            <span>{{chatToCustomer.message}}</span>
                        </div>
                        <div class="receiverMes">
                            <bk-tag theme="info">我的</bk-tag><br>
                            <span>这是消息</span>
                        </div>
                    </div>
                </bk-form-item>
                <bk-form-item required="true" :property="'chat-messageinput'" :desc="customDesc">
                    <bk-input id='chat-message-input' type="textarea" placeholder="请输入你要发送的信息" v-model='chatToCustomer.message'></bk-input>
                </bk-form-item>
            </bk-form>
        </bk-dialog>
        <!-- 给客服评分Dialog -->
        <bk-dialog v-model="scoreToCustomer.primary.visible" theme="primary" :mask-close="false" :header-position="scoreToCustomer.primary.headerPosition" title="给个五星好评叭">
            <bk-form :label-width="150" :model="personInfo">
                <bk-form-item label="请选择你的评分等级" :property="'records'">
                    <bk-rate :rate.sync="rate" :edit="true" @score="chooseRate" :tooltips="tooltips" :width="18" :height="18"></bk-rate>
                </bk-form-item>
            </bk-form>
        </bk-dialog>
        <!-- <bk-dialog>
            <bk-input type="textarea" id='chat-log'></bk-input>
            <bk-input id='chat-message-input' v-model='message'></bk-input>
            <bk-button id="chat-message-submit" theme="primary" @click="sendToCustomer">发送</bk-button>
        </bk-dialog> -->
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
                }
            ],
            rate: 5,
            tooltips: [1, 2, 3, 4, 5],
            customerList: '',
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
            chatToCustomer: {
                primary: {
                    visible: false,
                    headerPosition: 'center'
                }
            },
            chatToCustomerData: {
                id: '',   //接收者id
                message: ''
            },
            scoreToCustomer: {
                primary: {
                    visible: false,
                    headerPosition: 'left'
                }
            },
            scoreToCustomerData: {
                id: '',   //接收者id
                message: ''
            },
            message: '',
            sender: '',
            receiver: ''

        }
    },
    created () {
        this.getParams()
    },
    mounted () {
        this.getCustomerList()
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
            this.$axios.get('project/search_member_info/', { params: { id: this.id } }).then(res => {
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
        openChatDialog (row) {
            this.chatToCustomer.primary.visible = true
            this.chatToCustomerData.id = row.id
        },
        openScoreDialog (row) {
            this.scoreToCustomer.primary.visible = true
            this.scoreToCustomerData.id = row.id
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
        },
        getCustomerList () {
            this.$axios.get('project/get_customer_list/').then(res => {
                console.log('获取用户信息', res);
                if (res.data.result === true) {
                    this.customerList = res.data.data
                } else {
                    this.$bkMessage({
                        message: '获取客服列表失败',
                        theme: 'error'
                    })
                }

            }).catch(error => {
                this.$bkMessage({
                    message: error,
                    theme: 'error'
                })
            });
        },
        sendToCustomer () {
            this.sender = this.personInfo.id
            this.receiver = this.chatToCustomerData.id
            this.message = this.chatToCustomerData.message
            console.log('message', this.message)
            console.log('发送者id', this.sender)
            console.log('接受者', this.receiver)
            this.$axios.get('project/member_send_to_customer/', { params: { sender: this.sender, receiver: this.receiver, message: this.message, } }).then(res => {
                console.log('res', res)
                if (res.data.result === true) {
                    this.$bkMessage({
                        message: '发送成功',
                        theme: 'success'
                    })
                    document.getElementById('chat-message-input').value = ''
                    this.message = ''
                } else {
                    this.$bkMessage({
                        message: '发送失败！',
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
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#chat-log{
    margin-top: 20px;
    width: 90%;
    height: 450px;
    border:1px solid #c4c6cc;
    overflow: auto;
}
#chat-message-input{
    width: 90%;
}
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
.senderMes{
    width: 100%;
}
.senderMes .bk-tag, 
.senderMes span{
    float: right;
}
.receiverMes{
    width: 100%;
}

</style>
