import requests
import json

# Get real-time (static or dynamic) parking data from the RDW Open dataset, and parse it as a JSON file

api_url = "https://npropendata.rdw.nl/parkingdata/v2/"
select = 'Kanaalweg Westzijde'
dd = {}
b = ''

def Extract(): # Gets and filters the full dataset
    r = requests.get(api_url).json()
    for _k, _v in r.items():  # ParkingFacilities
        for locations in _v:
            for i, j in locations.items():
                static_url = locations.get('staticDataUrl')
                dynamic_url = locations.get('dynamicDataUrl')
                dd[locations.get('name')] = {
                            "static": static_url, "dynamic": dynamic_url}
    #with open("locations.json", "w") as location_file:
    #    dump = json.dumps(dd, indent=4)
    #    location_file.write(dump)
        return dd

def Location(select,dd): # Filters single location from data
    with open("locatie.json", "w") as locatie:
        if select in dd.keys():
            a = dd.get(select)
            if 'static' in a:
                a = requests.get(a['static']).json()
            dump = json.dumps(a, indent=4)
            locatie.write(dump)


def main():
    Extract()
    Location(select,dd)

if __name__ == "__main__":
    main()
