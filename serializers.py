import json

# id, title, author, year, status

id = 1
title = "Книга 1"
author = "Автор1"
year = "1234"
status = "выдана"

to_json = {'id':id, 'title': title, 'author': author, 'year': year, 'status': status}

with open('sw_templates.json', 'w') as f:
   f.write(json.dumps(to_json, ensure_ascii=False))

with open('sw_templates.json') as f:
    print(f.read())