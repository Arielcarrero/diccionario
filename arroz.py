meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"una carita muriendo de risa",
            "WTF":"es una mala palabra en ingles",
            "HDP":"es una mala palabra en ingles",
            "VR":"significa realidad virtual"
}
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    
        
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    print("no e encontrado esa palabra😓")
    # ¿Qué hacer si no se encuentra la palabra?  
