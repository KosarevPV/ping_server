import subprocess
import datetime

import chardet
from celery import shared_task


@shared_task(name='save_response_time')
def save_response_time(domain_id):
    from .models import Responses, Domains

    domain = Domains.objects.get(pk=int(domain_id))

    args = ['ping', '-c', '1', domain.domain_name]
    res_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in res_ping.stdout:
        str_line = line.decode(encoding=chardet.detect(line)['encoding'])
        if "icmp_seq" in str_line:
            timing = str_line.split('time=')[-1].split(' ms')[0]
            response_time = float(timing)
            response = Responses.objects.create(domain=domain, responses_time=response_time)
            response.save()
