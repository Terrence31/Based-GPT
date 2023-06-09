from happytransformer import HappyTextToText
from happytransformer import TTSettings
from langdetect import detect

text1 = input('Enter the text to be translated:: ')
lang1 = detect(text1)
lang2 = input('Enter the language to translate the text into:: ')
API_URL = f"Helsinki-NLP/opus-mt-{lang1}-{lang2}"
print(API_URL)

happy_tt = HappyTextToText("MARIAN", f"Helsinki-NLP/opus-mt-{lang1}-{lang2}")
arg = TTSettings(min_length=2)
result = happy_tt.generate_text(text1, args=arg)
print(result.text)

