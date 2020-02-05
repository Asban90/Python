Hell=input(' inset you lang: ')
lang=Hell
def greets(lang):
    if lang=='es':
      return 'Hola'
    elif lang=='fr':
      return 'boujour'
    else :
      return'Hello'
print(greets('en'),"Ali")
print(greets('es'),"Sun")
print(greets('fr'),"Bill")
big = max('Hello World')
print(big)