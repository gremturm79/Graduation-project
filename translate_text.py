from translate import Translator
import re

text = ['To continue setting up your OpenAI account, please verify that this is your email address.']

translator = Translator(from_lang='en', to_lang='ru')
reg = r'[A-z]'

for i in range(len(text)):
    if re.findall(reg, text[i]):
        text[i] = translator.translate(text[i])

print(text)
# print(text)
#translation = list(map(translator.translate,  text))
#print(translation)

