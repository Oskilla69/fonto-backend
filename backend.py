import csv
import json
import logging
from typing import List

road_types = {
    'road': True,
    'avenue': True,
    'ave': True,
    'street': True,
    'court': True,
    'way': True,
    'boulevard': True,
    'close': True
}

with open('postcodes.json', 'r') as postcodes:
    postcode_data = json.load(postcodes)

# function for getting street name
def get_street(road_str: str) -> List[str]:
    lower_road_str = map(lambda x: x.lower(), road_str)
    for idx, word in enumerate(lower_road_str):
        road_type = road_types.get(word)
        if road_type:
            return [' '.join(map(lambda x: x.capitalize(), road_str[:idx + 1]))]

# function for getting suburb and state
def get_suburb(postcode: str) -> List[str]:
    data = postcode_data.get(postcode)
    
    if data:
        state = data['state_name']
        suburb = data['place_name']
        return [suburb, state, postcode]
    else:
        logging.exception("invalid postcode")
        return None

# function for converting given strings to wanted format
def convert_format():
    with open('backend-data/sample_addresses.csv', 'r') as f:
        rows = csv.reader(f, delimiter=',')

        with open('output.csv', 'w+') as f_out:
            writer = csv.writer(f_out, delimiter=',')
            for row in rows:
                address = ''.join(row).split(" ")
                # last should always be postcode
                suburb_data = get_suburb(address[-1])

                # if suburb data exists, means is valid string provided
                if suburb_data:
                    # find street name
                    street_data = get_street(address)
                    writer.writerow(street_data + suburb_data)
                # otherwise move onto next input
                else: continue

            f_out.close()
        f.close()


convert_format()