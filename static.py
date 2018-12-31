# -*- coding:utf-8 -*-
# date: 2018-12-27 1:44
"""
the index.html
"""

html = """<!DOCTYPE html>
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name=viewport content="width=device-width,initial-scale=1">
    <title>远程控制关机/睡眠</title>
    <link rel="stylesheet" href="https://cdn.bootcss.com/iview/3.1.5/styles/iview.css">
    <script src="https://cdn.bootcss.com/vue/2.5.21/vue.min.js"></script>
    <script src="https://cdn.bootcss.com/iview/3.1.5/iview.min.js"></script>
    <script src="https://cdn.bootcss.com/axios/0.18.0/axios.min.js"></script>
</head>
<body>
<div id="app" style="margin: auto">
    <template>
        <div style="background: #f8f8f9">
            <Card title="操作" icon="ios-options" shadow
                  style="max-width: 500px; margin: auto">
                <div slot="extra" style="">
                    <div>
                        <a href="https://www.jianshu.com/p/efc20edafb13" target="_blank">
                            <img class="ivu-icon" style="height: 19px;" alt="简书" src="/jianshu"></a>
                        <a target="_blank" href="https://github.com/ly1102/remote_shutdown">
                            <Icon type="logo-github" size="22"/>
                        </a>
                    </div>

                </div>

                <CellGroup @click="handleClickItem()">
                    <template v-for="(task, index) in init.tasks">
                        <Cell :title="task.operation" :label="task.time">
                            <i-Button type="warning" slot="extra" :loading="task.loading"
                                      @click="cancel_timing(task, index)">取消
                            </i-Button>
                        </Cell>
                    </template>
                    <Cell title="定时关机">
                        <i-Button type="primary" slot="extra" icon="md-alarm" @click="shutdown_timing()" ghost>定时关机
                        </i-Button>
                    </Cell>
                    <Cell title="定时睡眠">
                        <i-Button type="primary" slot="extra" icon="md-alarm" @click="sleep_timing()" ghost>定时睡眠
                        </i-Button>
                    </Cell>
                    <Cell title="立即关机">
                        <i-Button type="primary" slot="extra" icon="md-alert" @click="shutdown_now()">立即关机</i-Button>
                    </Cell>
                    <Cell title="立即睡眠">
                        <i-Button type="primary" slot="extra" icon="md-alert" @click="sleep_now()">立即睡眠</i-Button>
                    </Cell>
                    <Cell title="账号密码">
                        <i-Button type="primary" slot="extra" @click="set_user()">修改账号密码</i-Button>
                    </Cell>
                    <Cell title="开机自启动" label="建议开启，以便随时使用">
                        <i-Switch v-model="init.self_starting" :loading="switch_loading" @on-change="switch_change()"
                                  slot="extra" size="large"/>
                    </Cell>
                    <Cell title="访问地址" label="点击查看手机访问网页的链接">
                        <i-Button type="primary" slot="extra" @click="ip_modal=true">查看</i-Button>
                    </Cell>
                    <Cell title="关闭软件" label="点击后软件将关闭，网页会失去响应">
                        <i-Button type="error" slot="extra" @click="shutdown_server()">{{ shutdown_info }}</i-Button>
                    </Cell>
                </CellGroup>
            </Card>
        </div>
    </template>
    <template>
        <Modal v-model="check_modal" width="360">
            <div :style="'color:'+color+';text-align:center; font-size:25px;'">
                <Icon type="ios-information-circle"></Icon>
                <span v-html="check_msg"></span>
            </div>
            <div slot="footer">
                <i-Button :type="check_submit_btn" size="large" :loading="modal_loading" @click="submit_now()">确认
                </i-Button>
                <i-Button type="default" size="large" @click="check_modal=modal_loading=false">取消</i-Button>
            </div>
        </Modal>
    </template>

    <template>
        <Modal :title="timing_msg" v-model="timing_modal" :mask-closable="false">
            <div>
                <h1>{{ timing_msg }}</h1>
                <p>
                    <template>
                        选择时间
                        <Date-Picker v-model="timing_time" type="datetime" format="yyyy-MM-dd HH:mm"
                                     placeholder="Select date and time(Excluding seconds)"></Date-Picker>
                    </template>
                </p>
            </div>
            <div slot="footer">
                <i-Button type="warning" size="large" :loading="modal_loading" @click="submit_timing()">确认</i-Button>
                <i-Button type="default" size="large" @click="timing_modal=false">取消</i-Button>
            </div>
        </Modal>
    </template>

    <template>
        <Modal title="设置访问账号密码" v-model="user_modal" :mask-closable="false">
            <div style="width:300px; margin: auto;">
                <div v-if="init">
                    第一次使用，请先添加访问的账号密码，防止别人恶意操作电脑。
                    如果不添加，则<strong>任何人</strong>都可以访问该网页。
                </div>
                <label>
                    账号：
                    <i-Input v-model="username" placeholder="请输入账户名" clearable style="width: 200px;"></i-Input>
                </label>
                <br/>
                <label>
                    密码：
                    <i-Input v-model="password" placeholder="请输入密码" clearable style="width: 200px;"></i-Input>
                </label>
            </div>
            <div slot="footer">
                <i-Button type="warning" size="large" :loading="modal_loading" @click="submit_user()">确认</i-Button>
                <i-Button type="default" size="large" @click="user_modal=false">取消</i-Button>
            </div>
        </Modal>
    </template>

    <template>
        <Modal title="查看电脑所有可用网络地址" v-model="ip_modal">
            <div style="min-width:300px; margin: auto;">
                <h6>用手机访问以下的链接，如果能打开本网页，则以后可以用这个链接控制电脑。</h6>
                <h6>手机必须和电脑连接同一个路由器或者手机连接电脑发射的WiFi。</h6>
                <table style="width:300px;text-align: left; margin: auto;">
                    <tr>
                        <th>网络名</th>
                        <th>访问地址</th>
                    </tr>
                    <tbody>
                    <template v-for="ipi in ip_info">
                        <tr style="margin-top: 5px;">
                            <td>{{ ipi.name }}</td>
                            <td>{{ ipi.addr }}</td>
                        </tr>
                    </template>
                    </tbody>
                </table>
            </div>
            <div slot="footer">
                <i-Button type="default" size="large" @click="ip_modal=false">关闭</i-Button>
            </div>
        </Modal>
    </template>
</div>
</body>
<script type="text/javascript">
    new Vue({
        el: '#app',
        created() {
            if (this.init.init) {
                this.user_modal = true;
            }
            var this_ = this;
            setTimeout(function () {
                this_.check_starting();
                this_.get_ip_list();
            }, 800);
            if (this.init.error !== null) {
                alert(this.init.error);
            }
        },
        data() {
            return {
                init: %s,
                ip_info: [
                    {'name': '本地连接', 'addr': 'http://127.0.0.1:8888'},
                ],
                username: '',
                password: '',
                is_shutdown_server: false,
                check_modal: false,
                timing_modal: false,
                user_modal: false,
                ip_modal: false,
                modal_loading: false,
                btn_loading: false,
                timing_loading: false,
                switch_loading: false,
                now_operation: '',
                timing_time: new Date(),
                check_msg: '确认立即关机吗？',
                warning: '#ff9900',
                error: '#f60',
                color: '#ff9900',
                check_submit_btn: 'warning',
                timing_msg: '定时关机',
                shutdown_info: '关闭本软件',
            }
        },
        methods: {
            cancel_timing(task, index) {
                task.loading = true;
                var this_ = this;
                axios.post('/delete_timing', {
                    time: task.time,
                    operation: task.operation,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
                        this_.init.tasks.splice(index, 1);
                        this_.$Message.success('任务已经成功取消。');
                    } else {
                        alert(response.data.msg);
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert('请求遇到了错误:' + error)
                });
                task.loading = false;
            },

            shutdown_now() {
                this.check_modal = true;
                this.check_msg = '确认立即关机吗？<br/>确认后无法取消哦！';
                this.color = '#f60';
                this.check_submit_btn = 'error';
                this.now_operation = 'shutdown';
            },
            shutdown_server() {
                this.check_modal = true;
                this.check_msg = '确认关闭软件吗？<br/>软件在下一次开启前不能用，定时计划也不能完成哦！';
                this.color = '#f60';
                this.check_submit_btn = 'error';
                this.now_operation = 'shutdown_server';
            },
            sleep_now() {
                this.check_modal = true;
                this.check_msg = '确认立即睡眠吗？<br/>&emsp;&emsp;确认后无法取消哦！';
                this.color = '#f90';
                this.check_submit_btn = 'warning';
                this.now_operation = 'sleep';
            },
            submit_now() {
                this.modal_loading = true;
                var this_ = this;
                if (this.now_operation === 'shutdown_server') {
                    axios.post('/shutdown', {})
                        .then(function (response) {
                            console.log(response);
                            if (response.data.status === 'ok') {
                                this_.check_modal = false;
                                this_.shutdown_info = "5s";
                                this_.$Message.success('请求成功！软件在5秒后关闭。');
                                this_.refresh_shutdown(5, this_);
                            } else {
                                alert(response.data.msg);
                            }
                        }).catch(function (error) {
                        console.log(error);
                        alert('请求遇到了错误:' + error);
                    });
                } else {
                    axios.post('/operation', {
                        operation: this.now_operation,
                    }).then(function (response) {
                        console.log(response);
                        if (response.data.status === 'ok') {
                            this_.check_modal = false;
                            this_.$Message.success('请求成功，请注意观察电脑状态！');
                        } else {
                            alert(response.data.msg);
                        }
                    }).catch(function (error) {
                        console.log(error);
                        alert('请求遇到了错误:' + error);
                    });
                }

                this.modal_loading = false;
            },
            refresh_shutdown(seconds, this_) {
                this_.shutdown_info = seconds + 's';
                if (seconds === 0) {
                    this_.shutdown_info = '软件已关闭';
                } else {
                    setTimeout(function () {
                            this_.refresh_shutdown(seconds - 1, this_);
                        }
                        , 1000);
                }
            },
            shutdown_timing() {
                this.timing_modal = true;
                this.timing_msg = "定时关机";
                this.timing_operation = 'shutdown';
            },
            sleep_timing() {
                this.timing_modal = true;
                this.timing_msg = "定时睡眠";
                this.timing_operation = 'sleep';
            },
            submit_timing() {
                this.modal_loading = true;
                var this_ = this;
                axios.post('/timing', {
                    time: this.timing_time,
                    operation: this.timing_operation,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
                        this_.$Message.success('定时任务安排成功！');
                        this_.init.tasks.push({'operation': response.data.operation, 'time': response.data.time});
                        this_.timing_modal = false;
                    } else {
                        alert(response.data.msg);
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert('请求遇到了错误:' + error)
                });
                this.modal_loading = false;
            },
            set_user() {
                this.user_modal = true;
            },
            submit_user() {
                this.modal_loading = true;
                var this_ = this;
                axios.post('/user', {
                    username: this.username,
                    password: this.password,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
                        this_.user_modal = false;
                        this_.$Message.success('账号密码已经成功修改！');
                    } else {
                        alert(response.data.msg);
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert('请求遇到了错误:' + error)
                });
                this.modal_loading = false;
            },

            switch_change() {
                this.switch_loading = true;
                var this_ = this;
                if (!this.init.self_starting) {
                    axios.post('/starting', {
                        self_starting: this.init.self_starting,
                    }).then(function (response) {
                        console.log(response);
                        if (response.data.status === 'ok') {
                            this_.init.self_starting = false;
                            this_.$Message.success('开机启动已取消！');
                        } else {
                            alert(response.data.msg);
                            this_.init.self_starting = true;
                        }
                    }).catch(function (error) {
                        console.log(error);
                        alert('请求遇到了错误:' + error);
                        this_.init.self_starting = true;
                    });
                    this.switch_loading = false;
                } else {
                    axios.post('/starting', {
                        self_starting: this.init.self_starting,
                    }).then(function (response) {
                        console.log(response);
                        if (response.data.status === 'ok') {
                            this_.init.self_starting = true;
                            this_.$Message.success('开机启动已设置成功！');
                        } else {
                            alert(response.data.msg);
                            this_.init.self_starting = false;
                        }
                    }).catch(function (error) {
                        console.log(error);
                        alert('请求遇到了错误:' + error);
                        this_.init.self_starting = false;
                    });
                    this.switch_loading = false;
                }
            },

            get_ip_list() {
                var this_ = this;
                axios.get('/get_ip')
                    .then(function (response) {
                        console.log(response);
                        if (response.data.status === 'ok') {
                            this_.ip_info = response.data.net.slice(0);
                        } else {
                            alert(response.data.msg);
                        }
                    }).catch(function (error) {
                    console.log(error);
                    alert('请求遇到了错误:' + error);
                });
            },
            check_starting() {
                this.switch_loading = true;
                var this_ = this;
                axios.get('/check_self_starting')
                    .then(function (response) {
                        if (response.data.status === 'ok') {
                            this_.init.self_starting = response.data.self_starting;
                        } else {
                            alert(response.data.msg);
                        }
                    }).catch(function (error) {
                    console.log(error);
                    alert('请求遇到了错误:' + error)
                });
                this.switch_loading = false;
            },
        }
    })
</script>
</html>"""

jianshu = b'\x00\x00\x01\x00\x01\x00  \x00\x00\x01\x00 \x00\xa8\x10\x00\x00\x16\x00\x00\x00(\x00\x00\x00 \x00\x00\x00@\x00\x00\x00\x01\x00 \x00\x00\x00\x00\x00\x00\x10\x00\x00\x12\x0b\x00\x00\x12\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Id\xed\x1cHa\xe6\xa6H`\xe6\xe6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe6\xe6Ha\xe6\xa6Id\xed\x1c\x00\x00\x00\x00Id\xed\x1cHa\xe5\xedH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffHa\xe5\xedId\xed\x1cHa\xe6\xa6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffHa\xe6\xa6H`\xe6\xe6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe6\xe6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\x8a\x99\xee\xff\x9a\xa7\xf0\xffj}\xe9\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffMd\xe5\xff\x9a\xa7\xf0\xff\xa0\xad\xf1\xff\x9c\xa9\xf1\xffx\x89\xeb\xffIa\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xf4\xf6\xfd\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff}\x8e\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xcb\xd2\xf7\xffKc\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffi}\xe9\xff\xa1\xad\xf1\xff\xa3\xaf\xf1\xff\xd1\xd7\xf8\xff\xff\xff\xff\xff\xff\xff\xff\xff\x91\xa0\xef\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffVl\xe7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xba\xc3\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8e\x9d\xee\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xf1\xf3\xfd\xff\xc2\xca\xf6\xffdx\xe9\xffH`\xe5\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc9\xd0\xf7\xff\xa6\xb1\xf2\xff\xa6\xb1\xf2\xff\xa6\xb1\xf2\xff\xad\xb8\xf3\xff\xed\xf0\xfc\xff\xff\xff\xff\xff\xef\xf1\xfc\xff]r\xe8\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\x91\xa0\xef\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\x92\xa0\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\x9e\xaa\xf1\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\x93\xa1\xef\xffIa\xe5\xffIa\xe5\xffIa\xe5\xffIa\xe5\xff\x87\x97\xee\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb9\xc2\xf5\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb8\xc1\xf5\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\xe4\xfa\xff\xc6\xcd\xf6\xff\xc6\xcd\xf6\xff\xc6\xcd\xf6\xff\xc6\xcd\xf6\xff\xd8\xdd\xf9\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb7\xc1\xf4\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\x9b\xa8\xf0\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\x81\x91\xed\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb7\xc0\xf4\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\x9b\xa8\xf0\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\x81\x91\xed\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb6\xc0\xf4\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x8f\x9d\xef\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb5\xbf\xf4\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xc2\xca\xf6\xff\xff\xff\xff\xff\xfd\xfd\xfe\xffH`\xe5\xffH`\xe5\xff\x85\x95\xed\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xe5\xe8\xfb\xff\xa5\xb1\xf2\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffh|\xe9\xffz\x8b\xec\xffz\x8c\xec\xff\xb4\xbe\xf4\xff\xca\xd1\xf7\xff\xa7\xb2\xf2\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffIa\xe5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff`u\xe8\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbc\xc5\xf5\xffm\x80\xea\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x98\xa5\xf0\xff\x99\xa7\xf0\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xbc\xc5\xf5\xff\xff\xff\xff\xff\xf5\xf6\xfd\xff_t\xe8\xff\xcf\xd5\xf8\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbd\xc6\xf5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xa0\xad\xf1\xffTj\xe6\xff\x7f\x90\xec\xff\xff\xff\xff\xff\xfc\xfd\xfe\xff}\x8e\xec\xffH`\xe5\xff\xab\xb6\xf3\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xca\xd1\xf7\xff\xe1\xe5\xfa\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\xc0\xc8\xf6\xff\x95\xa3\xf0\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xfc\xfd\xfe\xff\xf5\xf6\xfd\xff\xad\xb8\xf3\xffTj\xe6\xffMd\xe5\xffH`\xe5\xff\x7f\x90\xec\xff\xe8\xeb\xfb\xff\xe1\xe5\xfa\xff\\r\xe7\xffH`\xe5\xffu\x87\xeb\xff\xff\xff\xff\xff\xbc\xc5\xf5\xffQh\xe6\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xcb\xd2\xf7\xff\xf7\xf8\xfd\xff\xc4\xcb\xf6\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xa3\xaf\xf1\xff\xfa\xfb\xfe\xff\xff\xff\xff\xff\xce\xd4\xf8\xffOf\xe6\xffH`\xe5\xff\xba\xc3\xf5\xff\xff\xff\xff\xff\xf5\xf6\xfd\xffNe\xe5\xffH`\xe5\xffau\xe8\xff\xee\xf0\xfc\xff\xff\xff\xff\xff\xdd\xe2\xfa\xffYn\xe7\xffH`\xe5\xffMd\xe5\xff\xf7\xf8\xfd\xff\xff\xff\xff\xff\xad\xb8\xf3\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffm\x80\xea\xff\xf4\xf6\xfd\xff\xff\xff\xff\xff\xd7\xdc\xf9\xff\x99\xa7\xf0\xff\xf6\xf7\xfd\xff\xff\xff\xff\xff\xd8\xdd\xf9\xff\x8f\x9d\xef\xff\x94\xa2\xef\xff\x96\xa3\xf0\xfffz\xe9\xff\xdd\xe2\xfa\xff\xff\xff\xff\xff\xde\xe2\xfa\xff\x99\xa7\xf0\xff\xb2\xbc\xf4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb2\xbc\xf4\xff\x99\xa7\xf0\xff\x99\xa7\xf0\xffz\x8b\xec\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff}\x8e\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x9c\xa9\xf1\xff_t\xe8\xff\xfa\xfb\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf1\xf3\xfd\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xcc\xd3\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xffi|\xe9\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\xba\xc3\xf5\xff\xff\xff\xff\xff\xff\xff\xff\xff\x88\x98\xee\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\x8c\x9b\xee\xff\xff\xff\xff\xff\xff\xff\xff\xff\x91\x9f\xef\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xff\x7f\x90\xec\xff\xff\xff\xff\xff\xff\xff\xff\xff\x9e\xaa\xf1\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe6\xe6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffJa\xe5\xffJa\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe6\xe6Ha\xe6\xa6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffHa\xe6\xa6Id\xed\x1cHa\xe5\xedH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffHa\xe5\xedId\xed\x1c\x00\x00\x00\x00Id\xed\x1cHa\xe6\xa6H`\xe6\xe6H`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe5\xffH`\xe6\xe6Ha\xe6\xa6Id\xed\x1c\x00\x00\x00\x00\x80\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x01'