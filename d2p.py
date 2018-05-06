#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from time import sleep
from sodapy import Socrata
from config import *
from google.cloud import pubsub

"""
A simple script to

 - pull a chunk of data from Socrata API service
 - publish jsonized data to Google Cloud PubSub
"""


def main():
    sc_client = Socrata(SOCRATA_DOMAIN, SOCRATA_APP_TOKEN)
    publisher = pubsub.PublisherClient()
    data_list = sc_client.get(SOCRATA_DATASET_IDENTIFIER, limit=LIMIT)
    for data in data_list:
        publisher.publish(TOPIC, json.dumps(data))
    print('completed to publish data as of {0:%Y%m%d_%H%M%S}'.format(datetime.now()))


if __name__ == '__main__':
    while True:
        main()
        sleep(TIME_INTERVAL)
