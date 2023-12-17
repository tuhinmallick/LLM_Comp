import json

lima_platypus = []
with open("lima_platypus.jsonl", "r") as jsonl_file:
    lima_platypus.extend(json.loads(line) for line in jsonl_file)
leetcode_platypus = []
with open("leetcode_platypus.jsonl", "r") as jsonl_file:
    leetcode_platypus.extend(json.loads(line) for line in jsonl_file)
math_platypus = []
with open("math_platypus.jsonl", "r") as jsonl_file:
    math_platypus.extend(json.loads(line) for line in jsonl_file)
scienceqa_platypus = []
with open("scienceqa_platypus.jsonl", "r") as jsonl_file:
    scienceqa_platypus.extend(json.loads(line) for line in jsonl_file)
reclor_platypus = []
with open("reclor_platypus.jsonl", "r") as jsonl_file:
    reclor_platypus.extend(json.loads(line) for line in jsonl_file)
scibench_platypus = []
with open("scibench_platypus.jsonl", "r") as jsonl_file:
    scibench_platypus.extend(json.loads(line) for line in jsonl_file)
arb_oasst1 = []
with open("arb_oasst1.jsonl", "r") as jsonl_file:
    arb_oasst1.extend(json.loads(line) for line in jsonl_file)
thm_obqa = []
with open("filtered_theoremqa.jsonl", "r") as jsonl_file:
    thm_obqa.extend(json.loads(line) for line in jsonl_file)
platypus = lima_platypus + leetcode_platypus + math_platypus + scienceqa_platypus + reclor_platypus + scibench_platypus + arb_oasst1 + thm_obqa
print(len(platypus))
with open("ours_platypus.jsonl", "w") as jsonl_file:
    jsonl_file.write("\n".join([json.dumps(row) for row in platypus]))

