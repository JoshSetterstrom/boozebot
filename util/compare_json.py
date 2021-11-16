import json
from jsondiff import diff

##Compares new JSON with old JSON new stock or restock##
def compare_json(json1, json2):
    difference = json.loads(diff(json1, json2, dump=True))
    updates = {"new": [], "updated": []}
    
    ##If a new item has been added to the site
    try:
        for position in difference['items']['$insert']:
            updates['new'].append({
                "name": position[1]['name'],
                "link": position[1]['link'],
                "img": position[1]['img']})

    except: pass ##No new items##
    
    ##If an existing item has been modified/restocked##
    try:
        for position in difference['items']:
            for key in list(difference['items'][position]):
                updates['updated'].append({
                        key: difference['items'][position][key],
                        "name": json2['items'][int(position)]['name'],
                        "link": json2['items'][int(position)]['link'],
                        "img": json2['items'][int(position)]['img']})

    except: pass ##No modified items##

    return updates