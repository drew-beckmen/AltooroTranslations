import json

# naming conventions
# ar.json and he.json are the original files
# *_to_translate.json contains the untranslated strings 
# *_translated contaians the translated strings
# *_updated.json is the final translated version.

def update_translations(old_filename, updated_translations, language):
    with open(old_filename) as f:
        data = json.load(f)
    with open(updated_translations) as ff:
        updated_data = json.load(ff)
    for key in data:
        if key in updated_data:
            data[key] = updated_data[key]
    with open(language + '_updated.json', 'w', encoding='utf8') as fff:
        json.dump(data, fff, indent=4, ensure_ascii=False)

update_translations('ar.json', 'ar_translated.json', 'ar')
update_translations('he.json', 'he_translated.json', 'he')
