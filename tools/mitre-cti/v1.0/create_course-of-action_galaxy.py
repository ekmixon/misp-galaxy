#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Create a couple galaxy/cluster with cti\'s courses-of-action.\nMust be in the mitre/cti/ATTACK/course-of-action folder')
parser.add_argument("-v", "--version", type=int, required=True, help="Version of the galaxy. Please increment the previous one")
args = parser.parse_args()

values = []

for element in os.listdir('.'):
    if element.endswith('.json'):
        with open(element) as json_data:
            d = json.load(json_data)
            json_data.close()

            temp = d['objects'][0]

            value = {'description': temp['description'], 'value': temp['name'], 'meta': {}}
            value['meta']['uuid'] = re.search('--(.*)$', temp['id'])[0][2:]
            values.append(value)

galaxy = {
    'name': "Course of Action",
    'type': "mitre-course-of-action",
    'description': "ATT&CK Mitigation",
    'uuid': "6fcb4472-6de4-11e7-b5f7-37771619e14e",
    'version': args.version,
    'icon': "chain",
}

cluster = {
    'name': "Course of Action",
    'type': "mitre-course-of-action",
    'description': "ATT&CK Mitigation",
    'version': args.version,
    'source': "https://github.com/mitre/cti",
    'uuid': "a8825ae8-6dea-11e7-8d57-7728f3cfe086",
    'authors': ["MITRE"],
    'values': values,
}

with open('generate/galaxies/mitre_course-of-action.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre_course-of-action.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
