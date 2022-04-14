<template>
    <div class="wrapper">
        <div>
            <h1 style="float: left; margin: 20px">
                <bk-icon style="margin: 20px" type="dialogue" />{{msg}}
            </h1>
            <bk-tag theme="info" style="margin-top: 30px" radius="5px">{{identity}}</bk-tag>
            <bk-fixed-navbar v-if="showNav" style="background: #ebebeb" :position="position" :nav-items="navItems"></bk-fixed-navbar>
        </div>
        <div>
            <bk-tab :active.sync="active" :type="currentType" style="margin-top: 20px; width: 90%; margin: 0 auto" tab-position="left">
                <bk-tab-panel v-for="(panel, index) in panels" v-bind="panel" :key="index">
                    <div v-if="panel.name==='member'">用户
                        <bk-table style="margin-top: 15px;" :data="memberList" :size="size">
                            <bk-table-column type="index" label="id" width="60"></bk-table-column>
                            <bk-table-column label="昵称" prop="nickname"></bk-table-column>
                            <bk-table-column label="用户名" prop="username"></bk-table-column>
                            <bk-table-column label="密码" prop="password"></bk-table-column>
                            <bk-table-column label="个人介绍" prop="introduction"></bk-table-column>
                            <bk-table-column label="创建时间" prop="create_time"></bk-table-column>
                            <bk-table-column label="更新时间" prop="update_time"></bk-table-column>
                        </bk-table>
                    </div>
                    <div v-else-if="panel.name==='customer'">客服
                        <bk-table style="margin-top: 15px;" :data="customerList" :size="size">
                            <bk-table-column type="index" label="id" width="60"></bk-table-column>
                            <bk-table-column label="昵称" prop="nickname"></bk-table-column>
                            <bk-table-column label="用户名" prop="username"></bk-table-column>
                            <bk-table-column label="密码" prop="password"></bk-table-column>
                            <bk-table-column label="个人介绍" prop="introduction"></bk-table-column>
                            <bk-table-column label="创建时间" prop="create_time"></bk-table-column>
                            <bk-table-column label="更新时间" prop="update_time"></bk-table-column>
                            <bk-table-column label="操作" width="150">
                                <template slot-scope="props">
                                    <bk-button class="mr10" theme="primary" text @click="reset(props.row)">编辑信息</bk-button>
                                    <bk-button class="mr10" theme="primary" text @click="remove(props.row)">注销账号</bk-button>
                                </template>
                            </bk-table-column>
                        </bk-table>
                    </div>
                </bk-tab-panel>
            </bk-tab>
        </div>
        <!-- 便捷客服信息dialog -->
        <bk-dialog v-model="editInfo.primary.visible" theme="primary" :mask-close="false" :header-position="editInfo.primary.headerPosition" title="编辑客服信息">
            primary 主题，点击遮罩不会关闭弹框，esc 按键会关闭弹框
        </bk-dialog>
    </div>
</template>

<script>
export default {
    name: 'manager',
    data () {
        return {
            msg: 'Welcome to Online customer service management system !',
            identity: '管理员',
            panels: [
                { name: 'member', label: '会员用户管理', count: 10 },
                { name: 'customer', label: '客服用户管理', count: 20 },

            ],
            active: 'mission',
            type: ['card', 'border-card', 'unborder-card', 'vertical-card'],
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
            showNav: true,
            memberList: [],
            customerList: [],
            editInfo: {
                primary: {
                    visible: false,
                    headerPosition: 'left'
                }
            }
        }
    },
    mounted () {
        this.getMemberList(),
        this.getCustomerList()
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
                console.log('获取客服用户信息', res);
                if(res.data.result === true){
                    this.memberList = res.data.data
                }else{
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
        getCustomerList () {
            this.$axios.get('project/get_customer_list/').then(res => {
                console.log('获取用户信息', res);
                if(res.data.result === true){
                    this.customerList = res.data.data
                }else{
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
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
    /* background-image: url('../../images/homepage.jpg'); */
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
</style>
