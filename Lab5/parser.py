import json
import re

def parse(file):
    items, item = [], {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            l = line.strip()

            if re.match(r'^\d+\.$', l):
                if item:
                    items.append(item)
                item = {"id": l.strip(".")}

            elif re.match(r'^[А-Яа-яA-Za-z]', l):
                item["name"] = l

            elif re.match(r'^\d+,\d+\s*x\s*\d+,\d+', l):
                q, p = re.findall(r'\d+,\d+', l)
                item["qty"], item["price"] = q.replace(',', '.'), p.replace(',', '.')

            elif re.match(r'^\d+,\d+$', l):
                item["total"] = l.replace(',', '.')

            elif "ИТОГО" in l:
                total = next(f).strip()
                items.append({"total": total.replace(',', '.')})

    if item:
        items.append(item)

    return items

file = "/Users/alimanbibolov/Documents/PP2/Lab5/row.txt"
json_file = "row.json"

data = parse(file)

with open(json_file, 'w', encoding='utf-8') as jf:
    json.dump(data, jf, ensure_ascii=False, indent=4)
