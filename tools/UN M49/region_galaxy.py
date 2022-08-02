#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import argparse
import uuid
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Region Galaxy - only create the list of values')
    parser.add_argument("-c", "--csv", required=True, help="input csv")
    args = parser.parse_args()

    values = []

    with open(args.csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        pass_first_line = True
        for data in csvreader:
            if pass_first_line:
                pass_first_line = False
                continue
            temp = {}
            value_name = f"{data[0]} - {data[1]}"

            test = next((1 for value in values if value['value']==value_name), 0)
            if test==0:
                temp['value'] = value_name
                temp['meta'] = {'subregion': []}
                values.append(temp)

    """----------------  column 2 ------------------"""

    with open(args.csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        pass_first_line = True
        for data in csvreader:
            if pass_first_line:
                pass_first_line = False
                continue
            temp = {}
            value_name = f"{data[2]} - {data[3]}"
            parent_name = f"{data[0]} - {data[1]}"
            if value_name == " - ":
                continue

            test = next((1 for value in values if value['value']==value_name), 0)
            if test==0:
                temp['value'] = value_name
                temp['meta'] = {'subregion': []}
                values.append(temp)

            for value in values:
                if value['value']==parent_name:
                    test = next((1 for sub in value['meta']['subregion'] if sub == value_name), 0)
                    if test == 0:
                        value['meta']['subregion'].append(value_name)

    """----------------  column 3 ------------------"""

    with open(args.csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        pass_first_line = True
        for data in csvreader:
            if pass_first_line:
                pass_first_line = False
                continue
            temp = {}
            value_name = f"{data[4]} - {data[5]}"
            parent_name = f"{data[2]} - {data[3]}"
            if value_name == " - ":
                continue

            test = next((1 for value in values if value['value']==value_name), 0)
            if test==0:
                temp['value'] = value_name
                temp['meta'] = {'subregion': []}
                values.append(temp)

            for value in values:
                if value['value']==parent_name:
                    test = next((1 for sub in value['meta']['subregion'] if sub == value_name), 0)
                    if test == 0:
                        value['meta']['subregion'].append(value_name)


    """----------------  column 4 ------------------"""

    with open(args.csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        pass_first_line = True
        for data in csvreader:
            if pass_first_line:
                pass_first_line = False
                continue
            temp = {}
            value_name = f"{data[6]} - {data[7]}"
            parent_name = f"{data[4]} - {data[5]}"
            if value_name == " - ":
                continue

            test = next((1 for value in values if value['value']==value_name), 0)
            if test==0:
                temp['value'] = value_name
                temp['meta'] = {'subregion': []}
                values.append(temp)

            for value in values:
                if value['value']==parent_name:
                    test = next((1 for sub in value['meta']['subregion'] if sub == value_name), 0)
                    if test == 0:
                        value['meta']['subregion'].append(value_name)

    """----------------  column 5 ------------------"""

    with open(args.csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        pass_first_line = True
        for data in csvreader:
            if pass_first_line:
                pass_first_line = False
                continue
            temp = {}
            value_name = f"{data[8]} - {data[9]}"
            x=6
            y=7
            test = 0
            while test == 0:
                parent_name = f"{data[x]} - {data[y]}"
                if parent_name == " - ":
                    x=x-2
                    y=y-2
                else:
                    test=1

            for value in values:
                if value['value']==parent_name:
                    test = next((1 for sub in value['meta']['subregion'] if sub == value_name), 0)
                    if test == 0:
                        value['meta']['subregion'].append(value_name)


    print (values)

    with open('region_valuea.json', 'w') as outfile:
            json.dump(values, outfile)
