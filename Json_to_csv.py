import pandas as pd
import json
import os

#%%

with open(os.path.expanduser("~/Downloads/SheetC.json")) as file:
    data = json.load(file)


#%%

json_test_result_data = json.loads(data['test_result'])
final_json = dict()

#%%

i = 1
for key, value in json_test_result_data.items():
    temp_dict = dict()
    temp_dict['sample_item_index'] = value['sample_item_index']
    temp_dict['item_material'] = value['meta_data']['item_material']
    temp_dict['is_frozen'] = value['meta_data']['is_frozen']
    temp_dict['grill_type'] = value['meta_data']['grill_type']
    temp_dict['thumbs_up_score'] = value['survey_result']['thumbs_up_score']
    temp_dict['guess_grill_correct'] = value['survey_result']['guess_grill_correct']
    final_json[i] = temp_dict
    i = i+1

#%%

pdObj = pd.read_json(json.dumps(final_json), orient='index')
csvData = pdObj.to_csv('final_SheetC_converted.csv', index=False)
