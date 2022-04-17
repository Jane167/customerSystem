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
            </div>
            <bk-tab :active.sync="active" :type="currentType" style="margin-top: 10px; width: 90%; margin: 0 auto" tab-position="left">
                <bk-tab-panel v-for="(panel, index) in panels" v-bind="panel" :key="index">                  
                    <textarea id="chat-log" cols="100" rows="20"></textarea><br>
                    <input id="chat-message-input" type="text" size="100"><br>                   
                    <bk-button id="chat-message-submit" theme="primary" @click="websocketonmessage">发送</bk-button>
                </bk-tab-panel>
            </bk-tab>
        </div>

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
            websock: ''
        }
    },
    created () {
        this.initWebSocket()
    },
    mounted () {
        this.getMemberList()
    },
    watch: {
    },
    methods: {
        exit () {
            setTimeout(() => {
                this.$router.push({
                    name: 'login'
                })
            }, 100)
        },
        getMemberList () {
            this.$axios.get('project/get_member_list/').then(res => {
                console.log('获取会员用户信息', res);
                if (res.data.result === true) {
                    this.memberList = res.data.data
                    console.log(this.memberList)
                    for (const item of this.memberList) {
                        console.log('item', item)
                        const username = item['username']
                        const nickname = item['nickname']
                        if (nickname !== '') {
                            var label = username + '-' + nickname
                        } else {
                            var label = username
                        }
                        const name = username
                        console.log('name', name)
                        this.panels.push({
                            name: name,
                            label: label,
                            count: 0
                        })

                    }

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
        // webscoket实现长连接
        initWebSocket () {
            //初始化websocket
            const wsurl = 'ws://' + '127.0.0.1:6379' + '/ws/table/' + this.roomName + '/'
            // const wsurl = 'ws://' + window.location.host + '/ws/table/' + this.roomName + '/'

            this.websock = new WebSocket(wsurl);
            this.websock.onopen = this.websocketonopen;
            this.websock.onerror = this.websocketonerror;
            this.websock.onmessage = this.websocketonmessage;

            this.websocket = this.websocket;
            this.websock.onclose = this.websocketclose;
        },
        websocket () {
            this.initWebSocket();
        },
        websocketonopen (e) {
            console.log("WebSocket连接成功", e);
        },
        websocketonerror (e) { //错误
            console.log("连接错误", e);

        },

        websocketonmessage (res) {
            // console.log("数据", res.data);'
            console.log('数据', res)
        },
        websocketclose (e) {
            console.log('断开连接', e)
            console.log('websocket 断开: ' + e.code + ' ' + e.reason + ' ' + e.wasClean)
        },
        sendMesg () {
            this.chatSocket = new WebSocket('ws://' + window.location.host + '/ws/table/' + this.roomName + '/');
            // this.chatSocket = new WebSocket('ws://' + '127.0.0.1:8000' + '/ws/table/' + this.roomName + '/');

            this.chatSocket.onmessage = function (e) {
                const data = JSON.parse(e.data);
                document.querySelector('#chat-log').value += (data.message + '\n');
            };

            this.chatSocket.onclose = function (e) {
                console.error('Chat socket closed unexpectedly');
            };

            console.log('chatSocket', this.chatSocket)
            var messageInputDom = document.querySelector('#chat-message-input')
            var message = messageInputDom.value
            this.chatSocket.onopen = function (e) {
                this.$bkMessage({
                    message: '发送成功',
                    theme: 'success'
                })
                // this.chatSocket.send(JSON.stringify(message));
                // messageInputDom.value = '';
                // this.$bkMessage({
                //     message: '发送成功',
                //     theme: 'success'
                // })
            }

            // this.whatever()

            //添加状态判断，当为OPEN时，发送消息

        },
        destroyed () {
            this.websocketclose()
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
.chatPanel {
    background-color: #c3c3c3;
    width: 1200px;
    height: 400px;
}
.chatInput {
    background-color: #c3c3c3;
    width: 1200px;
    height: 160px;
    border: 1px solid #42b983;
}
</style>
