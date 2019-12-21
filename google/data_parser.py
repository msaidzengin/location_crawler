import json

all_data_path = 'all_data.json'
result_path = 'all_result.json'

with open(all_data_path) as json_file:
    all_data = json.load(json_file)

location_data = []
for i in range(99):
    data = {}
    data['name'] = all_data[0][0][0][9][0][i][0][1]
    data['tag'] = all_data[0][0][0][9][0][i][0][2]
    try:
        data['star'] = all_data[0][0][0][9][0][i][0][5][0][0]
        data['comment'] = all_data[0][0][0][9][0][i][0][5][0][1]
    except:
        data['star'] = -1
        data['comment'] = -1
    data['coordinates'] = all_data[0][0][0][9][0][i][0][15]
    try:
        data['photo_url'] = all_data[0][0][0][9][0][i][0][13][0][2][0]
    except:
        data['photo_url'] = ""
    
    location_data.append(data)

with open(result_path, 'w', encoding='utf-8') as f:
    json.dump(location_data, f, ensure_ascii=False, indent=4)

