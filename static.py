# -*- coding:utf-8 -*-
# date: 2018-12-27 1:44
"""

"""
bootstrap4c_css = """
/*
 *
 *
 *
 * Bootstrap 4 Component - Custom switch
 * Version: 1.0.11
 * Copyright (c) 2017-18 Martin Haubek
 *
 *
 *
 */
.custom-switch .custom-switch-input {
  display: none; }
  .custom-switch .custom-switch-input, .custom-switch .custom-switch-input:after, .custom-switch .custom-switch-input:before,
  .custom-switch .custom-switch-input *,
  .custom-switch .custom-switch-input *:after,
  .custom-switch .custom-switch-input *:before,
  .custom-switch .custom-switch-input + .custom-switch-btn {
    box-sizing: border-box; }
    .custom-switch .custom-switch-input:selection, .custom-switch .custom-switch-input:after:selection, .custom-switch .custom-switch-input:before:selection,
    .custom-switch .custom-switch-input *:selection,
    .custom-switch .custom-switch-input *:after:selection,
    .custom-switch .custom-switch-input *:before:selection,
    .custom-switch .custom-switch-input + .custom-switch-btn:selection {
      background: none; }
  .custom-switch .custom-switch-input + .custom-switch-btn {
    outline: 0;
    display: inline-block;
    position: relative;
    -webkit-user-select: none;
       -moz-user-select: none;
        -ms-user-select: none;
            user-select: none;
    cursor: pointer;
    width: 68px;
    height: 38px;
    margin: 0;
    padding: 4px;
    background: #ced4da;
    border-radius: 76px;
    transition: all 300ms ease; }
    .custom-switch .custom-switch-input + .custom-switch-btn:after, .custom-switch .custom-switch-input + .custom-switch-btn:before {
      position: relative;
      display: block;
      content: "";
      width: 30px;
      height: 30px; }
    .custom-switch .custom-switch-input + .custom-switch-btn:after {
      left: 2px;
      border-radius: 50%;
      background: white;
      transition: all 300ms ease; }
    .custom-switch .custom-switch-input + .custom-switch-btn:before {
      display: none; }
  .custom-switch .custom-switch-input:checked + .custom-switch-btn {
    background: #28a745; }
    .custom-switch .custom-switch-input:checked + .custom-switch-btn:after {
      left: 30px; }
    .custom-switch .custom-switch-input:checked + .custom-switch-btn ~ .custom-switch-content-checked {
      opacity: 1;
      height: auto; }
    .custom-switch .custom-switch-input:checked + .custom-switch-btn ~ .custom-switch-content-unchecked {
      display: none;
      opacity: 0;
      height: 0; }
  .custom-switch .custom-switch-input:not(:checked) + .custom-switch-btn ~ .custom-switch-content-checked {
    display: none;
    opacity: 0;
    height: 0; }
  .custom-switch .custom-switch-input:not(:checked) + .custom-switch-btn ~ .custom-switch-content-unchecked {
    opacity: 1;
    height: auto; }
  .custom-switch .custom-switch-input[disabled] + .custom-switch-btn {
    background: rgba(206, 212, 218, 0.6);
    cursor: default; }
  .custom-switch .custom-switch-input[disabled]:checked + .custom-switch-btn {
    background: rgba(40, 167, 69, 0.4); }

.custom-switch .custom-switch-form-text {
  display: inline-block;
  height: 38px;
  margin-left: .5rem;
  line-height: 38px;
  vertical-align: top; }

.custom-switch.custom-switch-label-io .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='68' height='38'%3E%3Ctext x='42.5' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EO%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-io .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='68' height='38'%3E%3Ctext x='18.13333' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EI%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-onoff .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='68' height='38'%3E%3Ctext x='38.85714' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EOff%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-onoff .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='68' height='38'%3E%3Ctext x='9.71429' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EOn%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-yesno .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='68' height='38'%3E%3Ctext x='38.85714' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3ENo%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-yesno .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='68' height='38'%3E%3Ctext x='9.71429' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EYes%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-status .custom-switch-input + .custom-switch-btn {
  width: 96px;
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='96' height='38'%3E%3Ctext x='38.85714' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EDisabled%3C/text%3E%3C/svg%3E"); }

.custom-switch.custom-switch-label-status .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='96' height='38'%3E%3Ctext x='9.71429' y='23.75' font-size='12px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EEnabled%3C/text%3E%3C/svg%3E"); }
  .custom-switch.custom-switch-label-status .custom-switch-input:checked + .custom-switch-btn:after {
    left: 58px; }

.custom-switch-sm .custom-switch-input + .custom-switch-btn {
  width: 60px;
  height: 31px;
  padding: 3.26316px;
  border-radius: 62px; }
  .custom-switch-sm .custom-switch-input + .custom-switch-btn:after, .custom-switch-sm .custom-switch-input + .custom-switch-btn:before {
    width: 25px;
    height: 25px; }
  .custom-switch-sm .custom-switch-input + .custom-switch-btn:after {
    left: 1px; }

.custom-switch-sm .custom-switch-input:checked + .custom-switch-btn:after {
  left: 29px; }

.custom-switch-sm .custom-switch-form-text {
  height: 31px;
  margin-left: .5rem;
  line-height: 31px; }

.custom-switch-sm.custom-switch-label-io .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='31'%3E%3Ctext x='37.5' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EO%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-io .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='31'%3E%3Ctext x='16' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EI%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-onoff .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='31'%3E%3Ctext x='32.87671' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EOff%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-onoff .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='31'%3E%3Ctext x='8.57143' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EOn%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-yesno .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='31'%3E%3Ctext x='32.87671' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3ENo%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-yesno .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='31'%3E%3Ctext x='8.57143' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EYes%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-status .custom-switch-input + .custom-switch-btn {
  width: 88px;
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='88' height='31'%3E%3Ctext x='32.87671' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EDisabled%3C/text%3E%3C/svg%3E"); }

.custom-switch-sm.custom-switch-label-status .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='88' height='31'%3E%3Ctext x='8.57143' y='19.375' font-size='11px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EEnabled%3C/text%3E%3C/svg%3E"); }
  .custom-switch-sm.custom-switch-label-status .custom-switch-input:checked + .custom-switch-btn:after {
    left: 57px; }

.custom-switch-xs .custom-switch-input + .custom-switch-btn {
  width: 48px;
  height: 24px;
  padding: 2.52632px;
  border-radius: 48px; }
  .custom-switch-xs .custom-switch-input + .custom-switch-btn:after, .custom-switch-xs .custom-switch-input + .custom-switch-btn:before {
    width: 18px;
    height: 18px; }
  .custom-switch-xs .custom-switch-input + .custom-switch-btn:after {
    left: 1px; }

.custom-switch-xs .custom-switch-input:checked + .custom-switch-btn:after {
  left: 24px; }

.custom-switch-xs .custom-switch-form-text {
  height: 24px;
  margin-left: .5rem;
  line-height: 24px; }

.custom-switch-xs.custom-switch-label-io .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='24'%3E%3Ctext x='27.42857' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EO%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-io .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='24'%3E%3Ctext x='12.8' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EI%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-onoff .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='24'%3E%3Ctext x='25.6' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EOff%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-onoff .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='24'%3E%3Ctext x='6.85714' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EOn%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-yesno .custom-switch-input + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='24'%3E%3Ctext x='25.6' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3ENo%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-yesno .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='24'%3E%3Ctext x='6.85714' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EYes%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-status .custom-switch-input + .custom-switch-btn {
  width: 76px;
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='76' height='24'%3E%3Ctext x='25.6' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EDisabled%3C/text%3E%3C/svg%3E"); }

.custom-switch-xs.custom-switch-label-status .custom-switch-input:checked + .custom-switch-btn {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='76' height='24'%3E%3Ctext x='6.85714' y='15' font-size='10px' font-family='-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji' fill='%23fff'%3EEnabled%3C/text%3E%3C/svg%3E"); }
  .custom-switch-xs.custom-switch-label-status .custom-switch-input:checked + .custom-switch-btn:after {
    left: 52px; }

"""

html = """
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
        <div style="padding: 10px;background: #f8f8f9">
            <Card title="操作" icon="ios-options" shadow
                  style="max-width: 500px; margin: auto">
                <div slot="extra">
                    <a href="https://github.com/ly1102/remote_shutdown" type="extra">
                        <Icon type="logo-github" size="20"/>
                    </a>
                </div>

                <CellGroup @click="handleClickItem()">
                    <template v-for="(task, index) in init.tasks">
                        <Cell :title="task.name" :label="task.time">
                            <i-Button type="warning" slot="extra" :loading="task.loading"
                                      @click="cancel_timing(task, index)">取消
                            </i-Button>
                        </Cell>
                    </template>
                    <Cell title="立即关机">
                        <i-Button type="error" slot="extra" icon="md-alert" @click="shutdown_now()">立即关机</i-Button>
                    </Cell>
                    <Cell title="定时关机">
                        <i-Button type="error" slot="extra" icon="md-alarm" @click="shutdown_timing()" ghost>定时关机
                        </i-Button>
                    </Cell>
                    <Cell title="立即睡眠">
                        <i-Button type="warning" slot="extra" icon="md-alert" @click="sleep_now()">立即睡眠</i-Button>
                    </Cell>
                    <Cell title="定时睡眠">
                        <i-Button type="warning" slot="extra" icon="md-alarm" @click="sleep_timing()" ghost>定时睡眠
                        </i-Button>
                    </Cell>
                    <Cell title="账号密码">
                        <i-Button type="primary" slot="extra" @click="set_user()">修改账号密码</i-Button>
                    </Cell>
                    <Cell title="开机自启动" label="建议开启，以便随时使用">
                        <i-Switch v-model="init.self_starting" :loading="switch_loading" @on-change="switch_change()"
                                  slot="extra" size="large"/>
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
                    第一次使用，请先添加访问的账号密码，防止别人恶意操作电脑
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
</div>
</body>
<script type="text/javascript">
    new Vue({
        el: '#app',
        created() {
            if (this.init.init) {
                this.user_modal = true;
            }
        },
        data() {
            return {
                init: %s,
                username: '',
                password: '',
                check_modal: false,
                timing_modal: false,
                user_modal: false,
                modal_loading: false,
                btn_loading: false,
                timing_loading: false,
                switch_loading: false,
                now_operation: '',
                timing_time: new Date(),
                timing_operation: 'shutdown',
                check_msg: '确认立即关机吗？',
                warning: '#ff9900',
                error: '#f60',
                color: '#ff9900',
                check_submit_btn: 'warning',
                timing_msg: '定时关机',
            }
        },
        'methods': {
            cancel_timing(task, index) {
                task.loading = true;
                var this_ = this;
                axios.post('/delete', {
                    time: task.time,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
                        this_.init.tasks.splice(index, 1)
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
                axios.post('/operation', {
                    operation: this.now_operation,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
                        this_.check_modal = false;
                    } else {
                        alert(response.data.msg);
                    }
                }).catch(function (error) {
                    console.log(error);
                    alert('请求遇到了错误:' + error);
                });
                this.modal_loading = false;
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
                axios.post('/timing_operation', {
                    time: this.timing_time,
                    operation: this.timing_operation,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
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
                axios.post('/user', {
                    username: this.username,
                    password: this.password,
                }).then(function (response) {
                    console.log(response);
                    if (response.data.status === 'ok') {
                        this.user_modal = false;
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
                console.log(this.init.self_starting);
                var this_ = this;
                if (!this.init.self_starting) {
                    alert(123);
                    axios.post('/starting', {
                        self_starting: this.init.self_starting,
                    }).then(function (response) {
                        console.log(response);
                        if (response.data.status === 'ok') {
                            this_.init.self_starting = false;
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
        }
    })
</script>
</html>
"""


