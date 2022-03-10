import csv
import json
import logging

road_types = {
    'road': True,
    'avenue': True,
    'ave': True,
    'street': True,
    'court': True,
    'way': True,
    'boulevard': True,
}

with open('postcodes.json', 'r') as postcodes:
    postcode_data = json.load(postcodes)

with open('backend-data/sample_addresses.csv', 'r') as f:
    rows = csv.reader(f, delimiter=',')

    with open('output.csv', 'w+') as f_out:
        writer = csv.writer(f_out, delimiter=',')
        for row in rows:
            address = ''.join(row).split(" ")
            data = postcode_data.get(address[-1])
            if data:
                state = data['state_name']
                suburb = data['place_name']
                # print(suburb, state)
            else:
                logging.exception("invalid postcode")

        f_out.close()
    f.close()
