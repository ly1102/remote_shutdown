# -*- coding:utf-8 -*-
# date: 2018-12-25 14:35
import os
import sys
import json
import time
import psutil
import datetime
import winshell
import subprocess
import webbrowser
from win32com.client import Dispatch
from static import html, jianshu
from base64 import b64decode
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

default_config = {'init': True, 'port': 8888, 'error': None,
                  'tasks': [], 'self_starting': False,
                  'username': '', 'password': ''}

link_path = os.path.join(os.path.dirname(winshell.desktop()),
                         r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")


def read_config():
    if not os.path.exists('config.dt'):
        return default_config
    try:
        with open('config.dt', 'r', encoding='utf-8') as fp:
            config = fp.read()
            return json.loads(config)
    except Exception as e:
        write_config()
        return default_config


global_config = read_config()
host = ('0.0.0.0', global_config['port'])


def open_browser(addr):
    time.sleep(0.5)
    webbrowser.open(addr)


class TaskThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if global_config['tasks']:
                for index, task in enumerate(global_config['tasks']):
                    task_time = datetime.datetime.strptime(task['time'], "%Y-%m-%d %H:%M")
                    now = datetime.datetime.now()
                    if task_time.month == now.month and task_time.day == now.day and \
                            task_time.hour == now.hour and task_time.minute == now.minute:
                        if task['operation'] in ['关机', 'shutdown']:
                            global_config['tasks'].pop(index)
                            write_config()
                            exc_operation('shutdown')
                        elif task['operation'] in ['睡眠', 'sleep']:
                            global_config['tasks'].pop(index)
                            write_config()
                            exc_operation('sleep')
            else:
                return
            time.sleep(60)


def write_config():
    try:
        with open('config.dt', 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(global_config))
        return True
    except Exception:
        return False


class MyHttpHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        # self.config = config
        self.params = {}
        # self.server = server
        self.authenticate = b"""<HTML><HEAD><TITLE>401 Unauthorized</TITLE></HEAD>
                         <BODY BGCOLOR="#cc9999"><H4>401 Unauthorized</H4>
                             Authorization required.
                         </BODY></HTML>"""
        super().__init__(request, client_address, server)

    def do_GET(self):
        path = self.path
        if path == '/jianshu':
            self.send_response(200)
            self.send_header('Content-type', 'image/x-icon')
            self.end_headers()
            self.wfile.write(jianshu)
            return
        if 'Authorization' not in self.headers and not global_config['init']:
            self.authenticate_response()
            return
        else:
            if not global_config['init']:
                authorization = self.headers.get('Authorization', '')
                if authorization and authorization[:6] == 'Basic ':
                    user, password = b64decode(authorization[6:]).split(b':', 1)
                    if user.decode() != global_config['username'] or password.decode() != global_config['password']:
                        self.authenticate_response()
                        return
                else:
                    self.authenticate_response()
                    return

            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write((html % json.dumps(global_config)).encode())
                global_config['error'] = None
            elif path == '/check_self_starting':
                self.check_self_starting()
            elif path == '/get_ip':
                self.get_ip()
            else:
                self.json_response({'status': 'fail', 'msg': '未知的路径 {}'.format(path)})
                return

    def do_POST(self):
        self.parse_params()
        path = self.path
        if 'Authorization' not in self.headers and not global_config['init']:
            self.send_response(401)
            self.send_header('Content-type', 'text/html')
            self.send_header('WWW-Authenticate', 'Basic realm="pikaqiu"')
            self.end_headers()
            self.wfile.write(self.authenticate)
        else:
            if 'Authorization' not in self.headers and not global_config['init']:
                self.authenticate_response()
                return
            else:
                if not global_config['init']:
                    authorization = self.headers.get('Authorization', '')
                    if authorization and authorization[:6] == 'Basic ':
                        user, password = b64decode(authorization[6:]).split(b':', 1)
                        if user.decode() != global_config['username'] or password.decode() != global_config['password']:
                            self.authenticate_response()
                            return
                    else:
                        self.authenticate_response()
                        return

                if path == '/user':
                    self.add_user()
                    return
                elif path == '/operation':
                    self.add_operation()
                    return
                elif path == '/timing':
                    self.add_timing()
                    return
                elif path == '/delete_timing':
                    self.delete_timing()
                    return
                elif path == '/starting':
                    self.self_starting()
                    return
                elif path == '/shutdown':
                    def kill_server(server):
                        time.sleep(5)
                        server.shutdown()

                    kill_t = Thread(target=kill_server, args=(http_server,))
                    self.json_response({'status': 'ok'})
                    kill_t.start()
                    return
                else:
                    self.json_response({'status': 'fail', 'msg': '未知的路径 {}'.format(path)})
                    return

    def add_user(self):
        username = self.params.get('username')
        password = self.params.get('password')
        if not username or not password:
            self.json_response({"status": "fail", "msg": "账号或者密码为空"})
            return
        global_config['username'] = username
        global_config['password'] = password
        global_config['init'] = False
        write_config()
        self.json_response({'status': 'ok'})

    def add_operation(self):
        operation = self.params.get('operation')
        if not operation:
            self.json_response({'status': 'fail', 'msg': '操作类型为空'})
            return

        self.json_response({'status': 'ok'})
        op_thread = Thread(target=exc_operation, args=(operation,))
        op_thread.start()

    def add_timing(self):
        operation = self.params.get('operation')
        op_time_str = self.params.get('time')
        if operation not in ['shutdown', 'sleep', '关机', '睡眠']:
            self.json_response({'status': 'fail', 'msg': '操作类型为空'})
            return
        op_time = datetime.datetime.strptime(op_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")

        true_time = op_time + datetime.timedelta(hours=8)
        operation_chinese = '关机' if operation == 'shutdown' else '睡眠'
        global_config['tasks'].append(
            {'operation': operation_chinese, 'time': true_time.strftime("%Y-%m-%d %H:%M"), 'loading': False})
        self.json_response({'status': 'ok',
                            'time': true_time.strftime("%Y-%m-%d %H:%M"),
                            'operation': '关机' if operation == 'shutdown' else '睡眠'
                            })
        write_config()
        if len(global_config['tasks']) == 1:
            start_task_thread()

    def delete_timing(self):
        op_time_str = self.params.get('time')
        operation = self.params.get('operation')
        if operation in ['关机', 'shutdown']:
            operation = 'shutdown'
        elif operation in ['睡眠', 'sleep']:
            operation = 'sleep'
        else:
            self.json_response({'status': 'fail', 'msg': '操作的类型为{}，不符合要求'.format(operation)})
            return
        if not op_time_str:
            self.json_response({'status': 'fail', 'msg': '时间为空，请刷新页面'})
            return
        op_time = datetime.datetime.strptime(op_time_str, "%Y-%m-%d %H:%M")
        indexes = []
        for index, task in enumerate(global_config['tasks']):
            task_time = datetime.datetime.strptime(task['time'], "%Y-%m-%d %H:%M")
            task_op = task['operation']
            if task_time.month == op_time.month and task_time.day == op_time.day and \
                    task_time.hour == op_time.hour and task_time.minute == op_time.minute:
                if task_op == operation:
                    indexes.append(index)
        if not indexes:
            self.json_response({'status': 'fail', 'msg': '未找到匹配的时间的操作，请刷新页面'})
            return
        for index in indexes:
            global_config['tasks'].pop(index)
        write_config()
        self.json_response({'status': 'ok', 'msg': '删除成功，取消了{}个定时任务'.format(len(indexes))})

    def self_starting(self):
        starting_status = self.params.get('self_starting', None)
        if starting_status is None:
            self.json_response({'status': 'fail', 'msg': '参数异常'})
            return
        if starting_status:
            res = create_shortcut()
            if res == True:
                self.json_response({'status': 'ok'})
                global_config['self_starting'] = True
                write_config()
            else:
                self.json_response({'status': 'fail', 'msg': '遇到错误: {}'.format(res)})
        else:
            res = delete_shortcut()
            if res == True:
                self.json_response({'status': 'ok'})
                global_config['self_starting'] = False
                write_config()
            else:
                self.json_response({'status': 'fail', 'msg': '遇到错误: {}'.format(res)})

    def check_self_starting(self):
        self.json_response({'status': 'ok', 'self_starting': is_auto_starting()})

    def get_ip(self):
        all_ip = get_net_info()
        self.json_response({'status': 'ok', 'net': all_ip})

    def authenticate_response(self):
        self.send_response(401)
        self.send_header('Content-type', 'text/html')
        self.send_header('WWW-Authenticate', 'Basic realm="pikaqiu"')
        self.end_headers()
        self.wfile.write(self.authenticate)

    def json_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode())

    def parse_params(self):
        param_bytes = self.rfile.read(int(self.headers['content-length']))
        param_str = param_bytes.decode('utf-8')
        # params_str = param_str.split('&')
        # print(params_str)
        # params = dict(i.split('=', maxsplit=1) for i in params_str)
        params = json.loads(param_str)
        self.params = params


def exc_operation(command):
    time.sleep(0.5)
    if command == 'sleep':
        result = subprocess.Popen("powercfg -hibernate off",
                                  shell=True, stderr=subprocess.PIPE,
                                  stdout=subprocess.PIPE, bufsize=0)
        std_err = result.stderr.read().replace(b'\r', b'').strip(b'\n').decode('gbk')
        print(std_err)
        print(result.stdout.read().decode('gbk'))

        total_cmd = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        if '0x65b' not in std_err:
            total_cmd = total_cmd + "&& powercfg -hibernate on"

        subprocess.Popen(total_cmd, shell=True, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE, bufsize=0)

    if command == 'shutdown':
        subprocess.Popen("shutdown -s -t 0", shell=True, stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE, bufsize=0)


def is_auto_starting():
    starting_path = link_path
    starting_file = os.path.join(starting_path, 'easyControl.lnk')
    is_auto = os.path.exists(starting_file)
    if is_auto != global_config['self_starting']:
        global_config['self_starting'] = is_auto
        write_config()
    return is_auto


def create_shortcut():
    to_path = link_path
    to_file = os.path.join(to_path, 'easyControl.lnk')
    this_path = os.path.abspath(sys.executable)
    icon = this_path
    work_dir = os.path.dirname(this_path)
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(to_file)
    shortcut.Targetpath = this_path
    shortcut.WorkingDirectory = work_dir
    shortcut.IconLocation = icon
    try:
        shortcut.save()
    except Exception as e:
        return str(e)
    return True


def delete_shortcut():
    starting_path = link_path
    starting_file = os.path.join(starting_path, 'easyControl.lnk')
    try:
        os.remove(starting_file)
    except Exception as e:
        return False
    return True


def start_task_thread():
    task_thread = TaskThread()
    task_thread.start()


# 获取网卡名称和其ip地址和MAC地址，不包括回环。
def get_net_info():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        if not v[0][1] == '127.0.0.1' and '169.254' not in v[1][1]:
            netcard_info.append({'name': k, 'addr': 'http://{}:{}'.format(v[1][1], global_config['port'])})
    return netcard_info


if __name__ == '__main__':
    first_port = global_config['port']
    while True:
        try:
            http_server = HTTPServer(host, MyHttpHandler)
            break
        except OSError:
            global_config['port'] += 1
            host = ('0.0.0.0', global_config['port'])

    if first_port != global_config['port']:
        write_config()
        global_config['error'] = '{}端口被占用，现在采用的是{}端口'.format(first_port, global_config['port'])
    print("Starting server, listen at: %s:%s" % host[:2])
    if not os.path.exists('config.dt') or first_port != global_config['port']:
        t = Thread(target=open_browser, args=('http://127.0.0.1:' + str(global_config['port']),))
        t.start()
    http_server.serve_forever()
    http_server.server_close()
    os.listdir(os.path.abspath(os.path.dirname(__file__)))
