import pyjokes
import translate
res = translate.Translator(to_lang='ru', from_lang='en')

r = pyjokes.get_joke('en', 'neutral')
print(res.translate(r))

