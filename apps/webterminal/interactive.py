# -*- coding: utf-8 -*-
from .models import SshLog
from omsbackend import settings
import os
import socket
import sys
from paramiko.py3compat import u
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False
    raise Exception('This pro does\'t support windows')

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as e:
        import errno
        if e.errno == errno.EEXIST:
            pass



def interactive_shell(chan,channel,log_name=None,width=90,height=40):
    if has_termios:
        posix_shell(chan,channel,log_name=log_name,width=width,height=height)
    else:
        exit(1)
def posix_shell(chan,channel,log_name=None,width=90,height=40):
    from omsbackend.asgi import channel_layer
    import time
    import json
    stdout = list()
    begin_time = time.time()
    last_write_time = {'last_activity_time': begin_time}
    import select
    #oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        while True:
            r,w,e = select.select([chan,sys.stdin],[],[])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) ==0:
                        channel_layer.group_send(channel,{'text':json.dumps(['disconnect','\r\n*** EOF\r\n'])})
                        break
                    if x=="exit\r\n" or x=="logout\r\n":
                        chan.close()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                now = time.time()
                delay = now - last_write_time['last_activity_time']
                last_write_time['last_activity_time'] = now
                x = sys.stdin.read(1)
                if len(x) ==0:
                    break
                #chan.send(x)
                stdout.append([delay,x])
                channel_layer.group_send(channel,{'text':json.dumps(['stdout',x])})
                if log_name:
                    channel_layer.group_send(u'monitor-{0}'.format(log_name.rsplit('/')[1].rsplit('.json')[0]), {'text': json.dumps(['stdout',x])})
    finally:
        #termios.tcsetattr(sys.stdin,termios.TCSADRAIN,oldtty)
        attrs = {
            "version": 1,
            "width": width,
            "height": height,
            "duration": round(time.time() - begin_time, 6),
            "command": os.environ.get('SHELL', None),
            'title': None,
            "env": {
                "TERM": os.environ.get('TERM'),
                "SHELL": os.environ.get('SHELL', 'sh')
            },
            'stdout': list(map(lambda frame: [round(frame[0], 6), frame[1]], stdout))
        }
        mkdir_p('/'.join(os.path.join(settings.MEDIA_ROOT, log_name).rsplit('/')[0:-1]))
        with open(os.path.join(settings.MEDIA_ROOT, log_name), "a") as f:
            f.write(json.dumps(attrs, ensure_ascii=True, indent=2))
        audit_log = SshLog.objects.get(channel=channel, log=log_name.rsplit('/')[-1].rsplit('.json')[0])
        audit_log.is_finished = True
        from django.utils import timezone
        audit_log.end_time = timezone.now()
        audit_log.save()
        # hand ssh terminal exit
        queue = channel_layer._connection_list[0]
        redis_channel = queue.pubsub()
        queue.publish(channel, json.dumps(['close']))
