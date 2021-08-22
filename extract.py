"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    rows = []
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            # diameter handling as float
            try:
                if row['diameter']:
                    row['diameter'] = float(row['diameter'])
                else:
                    row['diameter'] = float('nan')
                # name
                if not row['name']:
                    row['name'] = None
                # pha handling in case of value N or ''
                if row['pha'] in ['N', '']:
                    row['pha'] = False
                else:
                    row['pha'] = True
                neo = NearEarthObject(
                    pdes=row["pdes"],
                    name=row["name"],
                    diameter=(row['diameter']),
                    pha=row["pha"],
                )

            except Exception as e:
                print(e)
                continue

            rows.append(neo)
        return rows


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cad = []
    with open(cad_json_path, 'r') as infile:
        cad_data = json.load(infile)
        for ele in cad_data['data']:
            data = (dict(zip(cad_data["fields"], ele)))
            try:
                ca = CloseApproach(
                    des=data["des"],
                    cd=data["cd"],
                    dist=data["dist"],
                    v_rel=data["v_rel"],
                )
            except Exception as e:
                print(e)
                continue
            cad.append(ca)

    return cad
