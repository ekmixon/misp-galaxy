#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Create a couple galaxy/cluster with cti\'s tools\nMust be in the mitre/cti/ATTACK/tool folder')
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
            value['meta']['refs'] = [
                reference['url']
                for reference in temp['external_references']
                if 'url' in reference
            ]

            if'x_mitre_aliases' in temp:
                value['meta']['synonyms'] = temp['x_mitre_aliases']
            value['meta']['uuid'] = re.search('--(.*)$', temp['id'])[0][2:]
            values.append(value)

galaxy = {
    'name': "Tool",
    'type': "mitre-tool",
    'description': "Name of ATT&CK software",
    'uuid': "d5cbd1a2-78f6-11e7-a833-7b9bccca9649",
    'version': args.version,
    'icon': "gavel",
}

cluster = {
    'name': "Tool",
    'type': "mitre-tool",
    'description': "Name of ATT&CK software",
    'version': args.version,
    'source': "https://github.com/mitre/cti",
    'uuid': "d700dc5c-78f6-11e7-a476-5f748c8e4fe0",
    'authors': ["MITRE"],
    'values': values,
}

with open('generate/galaxies/mitre_tool.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre_tool.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
