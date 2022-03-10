import csv
import json

with open('backend-data/australian_post_codes.txt', 'r') as f:
    rows = csv.reader(f, delimiter=',')
    count = 0
    postcode_dict = {}
    for row in rows:
        if count > 0:
            postcode_dict[row[0]] = {
                'place_name': row[1],
                'state_name': row[2],
                'latitude': row[3],
                'longitude': row[4],
                'accuracy': row[5]
            }
        count += 1
    with open('postcodes.json', 'w+') as postcode_json:
        json.dump(postcode_dict, postcode_json)