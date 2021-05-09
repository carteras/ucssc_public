people = {}
people['adam'] = {
    'hair':'ginger',
    'eyes':'hazel',
    'height':'tall',
    'profession':'nerdwrangler',
    'given_name':'adam'
}
people['ada'] = {
    'hair':'brown',
    'eyes':'blue',
    'height':'average',
    'profession':'nerd',
    'given_name':'ada'
}

for key in people:
    print(key, people[key]['profession'])