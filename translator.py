



def translator(language):
    translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
                    }
    
    def translate_word(word):
        return translations.get(language, {}).get(word, f"No translation found for '{word}' in {language}.")
    
    return translate_word


translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  

    