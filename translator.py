'''
Build a Translator in Python
Author: Niharika
'''
#import the package
from googletrans import Translator
#you can take any lanuguage text or input from user will be a good option 
#i am taking french poem "Tomorrow, at dawn" 
text = ''' Je ne regarderai ni l’or du soir qui tombe,
Ni les voiles au loin descendant vers Harfleur,
Et quand j’arriverai, je mettrai sur ta tombe
Un bouquet de houx vert et de bruyère en fleur '''

#create an instance of translator to use
translator = Translator()

# detect the language
lang = translator.detect(text)
print(lang)
print(' ')

# Call the translate()
translated = translator.translate(text, dest = 'en')

#print the result
print(translated.text)