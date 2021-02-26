import json

def find_untranslated_strings(file_name):
    with open(file_name) as f:
        data = json.load(f)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    to_translate = {}
    for key in data:
        # special case with interpolated status code
        if "status" in data[key]:
            continue
        for letter in data[key]:
            if letter.upper() in alphabet:
                to_translate[key] = data[key]
    return to_translate

hebrew = find_untranslated_strings('he.json')
arabic = find_untranslated_strings('ar.json')

with open('ar_to_translate.json', 'w') as f:
    json.dump(arabic, f, indent=4)


with open('he_to_translate.json', 'w') as e:
    json.dump(hebrew, e, indent=4)
