import logging.handlers
import os
import sys
import subprocess
from pathlib import Path

import chardet
from celery import shared_task
from ping_server.settings import BASE_DIR

PATH = os.path.join(BASE_DIR, 'server.log')

SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.INFO)

LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(SERVER_FORMATTER)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(logging.INFO)


@shared_task(name='save_response_time')
def save_response_time(domain_id):
    from .models import Responses, Domains

    domain = Domains.objects.get(pk=int(domain_id))

    res_ping = subprocess.Popen(['ping', '-c', '1', domain.domain_name], stdout=subprocess.PIPE)
    for line in res_ping.stdout:
        str_line = line.decode(encoding=chardet.detect(line)['encoding'])
        if "icmp_seq" in str_line:
            timing = str_line.split('time=')[-1].split(' ms')[0]
            response_time = float(timing)
            response = Responses.objects.create(domain=domain, responses_time=response_time)
            response.save()
            LOGGER.info(f'{domain.domain_name}: время отклика {response_time}')