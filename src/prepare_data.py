import json
import pandas as pd


data = []
with open('./data/subtask1_test_set_with_answer.json') as f:
    for line in f:
        data.append(json.loads(line))

# convert json to pairs of prompt & completion
prompt_lst, completion_lst = [], []
for ix, _row in enumerate(data):
    text = _row['originalText']
    all_entities = _row['entities']

    entity_lst = []
    label_type_lst = []
    combine_entity_lst = []
    for entity_info in all_entities:
        # entity_info = all_entities[0]
        entity = text[entity_info['start_pos']: entity_info['end_pos']]
        label_type = entity_info['label_type']

        entity_lst += [entity]
        label_type_lst += [label_type]
        combine_entity_lst += [f'{label_type}-{entity}']

    completion_lst += ['\n'.join(combine_entity_lst) + ' END']
    prompt_lst += [text + '\n\n Entity: \n\n']

    if divmod(ix, 10)[1] == 0:
        print(f'{divmod(ix, 10)[0]} / {len(data)/10} have been processed')


sample_data = pd.DataFrame({'prompt': prompt_lst, 'completion': completion_lst})

sample_data.to_json('./data/entities_.json', orient='records', lines=True)


