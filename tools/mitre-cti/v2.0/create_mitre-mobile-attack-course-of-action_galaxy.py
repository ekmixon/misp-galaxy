#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Create a couple galaxy/cluster with cti\'s courses-of-action.\nMust be in the mitre/cti/mobile-attack/course-of-action folder')
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
    'name': "Mobile Attack - Course of Action",
    'type': "mitre-mobile-attack-course-of-action",
    'description': "ATT&CK Mitigation",
    'uuid': "0282356a-1708-11e8-8f53-975633d5c03c",
    'version': args.version,
    'icon': "chain",
    'namespace': "mitre-attack",
}

cluster = {
    'name': "Mobile Attack - Course of Action",
    'type': "mitre-mobile-attack-course-of-action",
    'description': "ATT&CK Mitigation",
    'version': args.version,
    'source': "https://github.com/mitre/cti",
    'uuid': "03956f9e-1708-11e8-8395-976b24233e15",
    'authors': ["MITRE"],
    'values': values,
}

with open('generate/galaxies/mitre-mobile-attack-course-of-action.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre-mobile-attack-course-of-action.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
