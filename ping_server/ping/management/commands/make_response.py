import subprocess
import datetime

import chardet

import ping.models


def my_dunc():
    resource_data = ('yandex.ru', 'youtube.com', 'stackoverflow.com', 'django.fun')

    for item in resource_data:
        ARGS = ['ping', '-c', '1', item]
        RES_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
        for line in RES_PING.stdout:
            str_line = line.decode(encoding=chardet.detect(line)['encoding'])
            if "icmp_seq" in str_line:
                timing = str_line.split('time=')[-1].split(' ms')[0]
                response_time = datetime.time(microsecond=int(float(timing)*1000))
                print(item, response_time)


