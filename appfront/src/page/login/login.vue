<template>
    <div class="wrapper">
        <h2 class="title">{{msg}}</h2>
        <div class="loginTab">
            <bk-tab :active.sync="active" type="unborder-card">
                <bk-tab-panel v-for="(panel, index) in panels" v-bind="panel" :key="index">
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
            active: 'mission'
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
    /* 
    top: 30%;
    left: 20%;
    width: 30%; */
    /* position: fixed; */
    margin: 0 auto;
    margin-top: 5%;
}
.loginTab{
    width: 40%;
    margin: 0 auto;
    margin-top: 5%;
}
</style>
