#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Create a couple galaxy/cluster with cti\'s courses-of-action.\nMust be in the mitre/cti/enterprise-attack/course-of-action folder')
parser.add_argument("-v", "--version", type=int, required=True, help="Version of the galaxy. Please increment the previous one")
args = parser.parse_args()

values = []

for element in os.listdir('.'):
    if element.endswith('.json'):
        with open(element) as json_data:
            d = json.load(json_data)
            json_data.close()

            temp = d['objects'][0]

            value = {
                'description': temp['description'],
                'value': temp['name']
                + ' - '
                + temp['external_references'][0]['external_id'],
                'uuid': re.search('--(.*)$', temp['id'])[0][2:],
                'meta': {},
            }

            value['meta']['external_id'] = temp['external_references'][0]['external_id']
            values.append(value)

galaxy = {
    'name': "Enterprise Attack - Course of Action",
    'type': "mitre-enterprise-attack-course-of-action",
    'description': "ATT&CK Mitigation",
    'uuid': "fb5a36c0-1707-11e8-81f5-d732b22a4982",
    'version': args.version,
    'icon': "chain",
    'namespace': "mitre-attack",
}

cluster = {
    'name': "Enterprise Attack - Course of Action",
    'type': "mitre-enterprise-attack-course-of-action",
    'description': "ATT&CK Mitigation",
    'version': args.version,
    'source': "https://github.com/mitre/cti",
    'uuid': "fb870a6a-1707-11e8-b548-17523e4d0670",
    'authors': ["MITRE"],
    'values': values,
}

with open('generate/galaxies/mitre-enterprise-attack-course-of-action.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre-enterprise-attack-course-of-action.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
