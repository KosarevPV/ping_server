import subprocess
import datetime

import chardet
from celery import shared_task
from celery.utils.log import get_task_logger

# import django
# django.setup()


# from .models import Domains


@shared_task
def sample_task():
    from .models import Domains
    domains_objects = Domains.objects.all()

    for domain in domains_objects:
        item = domain.domain_name
        args = ['ping', '-c', '1', item]
        res_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in res_ping.stdout:
            str_line = line.decode(encoding=chardet.detect(line)['encoding'])
            if "icmp_seq" in str_line:
                timing = str_line.split('time=')[-1].split(' ms')[0]
                response_time = datetime.time(microsecond=int(float(timing) * 1000))
                print(item, response_time)





# celery -A ping_server worker -l INFO
# celery -A ping_server beat -l INFO