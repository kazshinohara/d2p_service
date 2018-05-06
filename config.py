#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Configurations for data pull and publish(d2p) service
"""

# overall
TIME_INTERVAL = 60

# data pull from SOCRATA API
SOCRATA_DOMAIN = 'data.cityofchicago.org'
SOCRATA_APP_TOKEN = 'YOUR_APP_TOKEN'
SOCRATA_DATASET_IDENTIFIER = '8v9j-bter'
LIMIT = 1500

# data publish to Cloud PUBSUB
TOPIC = 'projects/ksnhr-tech/topics/chicago_traffic_current_data'

