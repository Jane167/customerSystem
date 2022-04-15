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
                    <div class="chatPanel">

                    </div>
                    <div class="chatInput">
                        <bk-input :type="'textarea'" :rows="4" :maxlength="999" style="width: 90%; margin-top:10px;">
                        </bk-input>
                        <bk-button style="margin: 10px; margin-bottom: -100px" :theme="'default'" type="submit" :title="'基础按钮'" @click="handleClick" class="mr10">
                            发送
                        </bk-button>
                    </div>
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
        }
    },
    created () {
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
