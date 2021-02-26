# Altooro Translations

A series of scripts to read in JSON and detect untranslated strings. Those strings were then fed through a Google Apps Script that used google translate to convert English to the target language (either Hebrew or Arabic)

## Files

- `parase_translations.py`: reads in original files and finds the untranslated strings
- `update_translations.py`: uses the output of the Google Apps Script to generate the new complete list of localized strings.

## Google Apps Script

The basic script that uses the `Translate` API is [here](https://script.google.com/d/1IHf7HNQ_34LMgZgKJTb_F_N1tp3K_qQtvMGag8Xonsbce-INCVBjBlVD/edit?usp=sharing)

I'll also paste the code below:
```{js}
function translateStrings(obj, targetLanguage) {
  translated_obj = {};
  for (const key in obj) {
    const translated_str = LanguageApp.translate(obj[key], 'en', targetLanguage);
    translated_obj[key] = translated_str;
  }
  return translated_obj;
}

arabic_translations = translateStrings(ar_to_translate, "ar");
hebrew_translations = translateStrings(he_to_translate, 'he');
console.log(JSON.stringify(hebrew_translations, null, 2));
console.log(JSON.stringify(arabic_translations, null, 2));
```