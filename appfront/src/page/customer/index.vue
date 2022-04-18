<template>
    <div class="wrapper">
        <div>
            <h1 style="float: left; margin: 20px">
                <bk-icon style="margin: 20px" type="dialogue" />{{msg}}
            </h1>
            <bk-tag theme="success" style="margin-top: 30px" type="stroke" radius="5px">{{identity}}</bk-tag>
            <bk-fixed-navbar v-if="showNav" style="background: #ebebeb" :position="position" :nav-items="navItems"></bk-fixed-navbar>
        </div>
        <div style="margin-top: 30px">
            <div style="float: left; margin-left: 80px">
                <bk-tag theme="info" icon="icon-panel-permission" type="stroke">会员列表</bk-tag>
            </div><br><br>
            <bk-table style="margin: 0 auto; width: 85%;" :data="memberList">
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
                            发消息
                        </bk-button>
                    </template>
                </bk-table-column>
            </bk-table>
        </div>

        <!-- 聊天dialog -->
        <bk-dialog v-model="chatToMember.primary.visible" @confirm="sendToMember" :on-close="closeChatDialog" theme="primary" :mask-close="false" :header-position="chatToMember.primary.headerPosition" title="聊天框" ok-text="发送" cancel-text="关闭" :fullscreen=true :auto-close='false'>
            <bk-form :label-width="100">
                <bk-form-item :property="'records'" style="margin-top: 200">
                    <div id="chat-log">
                        <bk-link theme="primary" style="margin-left: 47%" @click="searchMemberMessage">
                            <bk-icon type="password" />点击加载聊天记录
                        </bk-link>
                        <div v-for="item in message_records" v-bind="item" :key="item" class="receiverMes">
                            <bk-tag theme="info">{{username}}： {{item.message}}
                                <br>发送时间：{{item.send_time}}
                            </bk-tag><br>
                        </div>
                    </div>
                </bk-form-item>
                <bk-form-item :required=true :property="'chat-messageinput'" >
                    <bk-input id='chat-message-input' type="textarea" placeholder="请输入你要发送的信息" v-model='chatToMemberData.message'></bk-input>
                </bk-form-item>
            </bk-form>
        </bk-dialog>
    </div>

</template>


<script>

export default {
    name: 'customer',
    data () {
        return {
            icons: ['icon-right-shape', 'icon-down-shape'],
            status: false,
            msg: 'Welcome to Online customer service management system !',
            identity: '客服',
            panels: [],
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
                    }
                }
            ],
            showNav: true,
            memberList: '',
            value: '',
            roomName: '1',
            chatSocket: null,
            websock: '',
            chatToMember: {
                primary: {
                    visible: false,
                    headerPosition: 'center'
                }
            },
            chatToMemberData: {
                //会员id
                id: '',
                username: '',
                message: ''
            },
            // 客服id
            id: '',
            username: '',
            message_records: ''
        }
    },
    created () {
        this.getParams()
    },
    mounted () {
        this.getMemberList()
        
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
            console.log('客服页面id', this.id)
        },
        getMemberList () {
            this.$axios.get('project/get_member_list/').then(res => {
                console.log('获取会员用户信息', res);
                if (res.data.result === true) {
                    this.memberList = res.data.data
                    console.log(this.memberList)

                } else {
                    this.$bkMessage({
                        message: '获取会员用户列表失败',
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
        openChatDialog (row) {
            this.chatToMember.primary.visible = true
            this.chatToMemberData.id = row.id
            this.username = row.username
            console.log('聊天对象：', this.username)
        },
        closeChatDialog () {
            console.log('关闭')
            this.message_records = ''
            console.log('聊天记录', this.message_records)
            this.chatToMember.primary.visible = false

        },
        // 获取收到的聊天记录
        searchMemberMessage () {
            // this.sender = this.personInfo.id
            this.receiver = this.chatToMemberData.id
            this.$axios.get('project/member_message_records/', { params: { sender: this.receiver, receiver: this.id } }).then(res => {
                console.log('res', res)
                if (res.data.result === true) {
                    this.message_records = res.data.data
                    console.log('消息记录', this.message_records)
                } else {
                    this.$bkMessage({
                        message: '消息记录查询失败！',
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
        sendToMember(){
            console.log('发送消息！')
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
#chat-log {
    margin-top: 20px;
    width: 90%;
    height: 450px;
    border: 1px solid #c4c6cc;
    overflow: auto;
}
#chat-message-input {
    width: 90%;
}
.senderMes {
    width: 100%;
    height: 45px;
}
.senderMes .bk-tag {
    margin-right: 10px;
    float: right;
    height: 40px;
}

.receiverMes {
    height: 45px;
    width: 100%;
}
.receiverMes .bk-tag{
    height: 40px;
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

</style>
