import os

# Create your views here.
from django.shortcuts import render


def get_status(request):
    invoke_shell = "cd /home/pi/Soft/python/enterBjNotify;python3 /home/pi/Soft/python/enterBjNotify/launch.py 0 1 4"
    result = os.system(invoke_shell)
    render_str = ''
    if result is 0:
        render_str = "已发送进京证信息到微信"
    else:
        render_str = "系统错误, code %d" % result

    return render(request, "jjz_status.html", {'render_str': render_str})
