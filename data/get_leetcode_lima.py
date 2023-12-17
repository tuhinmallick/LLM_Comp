from datasets import load_dataset

leetcode = load_dataset("TigerResearch/tigerbot-kaggle-leetcodesolutions-en-2k")["train"]
all_examples = []
for example in leetcode:
    dict_example = {
        "instruction": example["instruction"],
        "input": example["input"],
        "output": example["output"],
    }
    all_examples.append(dict_example)

import json
jsonl_data = [json.dumps(row) for row in all_examples]
with open("leetcode_platypus.jsonl", "w") as jsonl_file:
    jsonl_file.write("\n".join(jsonl_data))

lima = load_dataset("GAIR/lima")["train"]
all_examples = []
for example in lima:
    dict_example = {
        "instruction": example["conversations"][0],
        "input": "",
        "output": example["conversations"][1],
    }
    all_examples.append(dict_example)

import json
jsonl_data = [json.dumps(row) for row in all_examples]
with open("lima_platypus.jsonl", "w") as jsonl_file:
    jsonl_file.write("\n".join(jsonl_data))
