#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Create a couple galaxy/cluster with cti\'s attack-patterns\nMust be in the mitre/cti/mobile-attack/attack-pattern folder')
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
                'meta': {},
            }

            value['meta']['refs'] = []
            for reference in temp['external_references']:
                if 'url' in reference and reference['url'] not in value['meta']['refs']:
                    value['meta']['refs'].append(reference['url'])
                if 'external_id' in reference:
                    value['meta']['external_id'] = reference['external_id']
            value['meta']['kill_chain'] = [
                killchain['kill_chain_name']
                + ':mobile-attack:'
                + killchain['phase_name']
                for killchain in temp['kill_chain_phases']
            ]

            if 'x_mitre_data_sources' in temp:
                value['meta']['mitre_data_sources'] = temp['x_mitre_data_sources']
            if 'x_mitre_platforms' in temp:
                value['meta']['mitre_platforms'] = temp['x_mitre_platforms']
            values.append(value)
            value['uuid'] = re.search('--(.*)$', temp['id'])[0][2:]

galaxy = {
    'name': "Mobile Attack - Attack Pattern",
    'type': "mitre-mobile-attack-attack-pattern",
    'description': "ATT&CK Tactic",
    'uuid': "1c6d1332-1708-11e8-847c-e3c5643c41a5",
    'version': args.version,
    'icon': "map",
    'namespace': "mitre-attack",
}

cluster = {
    'name': "Mobile Attack - Attack Pattern",
    'type': "mitre-mobile-attack-attack-pattern",
    'description': "ATT&CK tactic",
    'version': args.version,
    'source': "https://github.com/mitre/cti",
    'uuid': "1e606d06-1708-11e8-8a43-df11c8cf9ae2",
    'authors': ["MITRE"],
    'values': values,
}

with open('generate/galaxies/mitre-mobile-attack-attack-pattern.json', 'w') as galaxy_file:
    json.dump(galaxy, galaxy_file, indent=4)

with open('generate/clusters/mitre-mobile-attack-attack-pattern.json', 'w') as cluster_file:
    json.dump(cluster, cluster_file, indent=4)
