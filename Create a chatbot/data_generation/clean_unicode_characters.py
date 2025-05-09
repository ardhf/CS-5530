import unicodedata

TRANSLATE = {
    ord('\u00A0'): ' ',   # NO-BREAK SPACE           → normal space
    ord('\u00E9'): 'e',   # é                        → e
    ord('\u2009'): ' ',   # THIN SPACE               → space
    ord('\u2011'): '-',   # NON-BREAKING HYPHEN      → hyphen-minus
    ord('\u2013'): '-',   # EN DASH                  → hyphen-minus
    ord('\u2014'): '-',   # EM DASH                  → hyphen-minus
    ord('\u2018'): "'",   # LEFT SINGLE QUOTATION    → apostrophe
    ord('\u2019'): "'",   # RIGHT SINGLE QUOTATION   → apostrophe
    ord('\u202F'): ' ',   # NARROW NO-BREAK SPACE    → space
}

with open('data/intents_expanded.json', 'r', encoding='utf-8') as f:
    data = ''.join(f.readlines())

fixed = data.encode('utf-8').decode('unicode_escape')

normalized = unicodedata.normalize('NFKD', fixed)

translated = normalized.translate(TRANSLATE)

cleaned_unicode = translated.encode('ascii', 'ignore').decode('ascii')

with open('data/intents_expanded.json', 'w') as f:
    f.write(cleaned_unicode)
