from translate import Translator

print("Language Translation")
lang_from = input("From: ")
lang_to = input("To: ")
translator= Translator(from_lang = lang_from, to_lang = lang_to)
translation = translator.translate(input("Input: "))

print(translation)