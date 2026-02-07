while True:
    meme_dict = {
                "CRINGE": "Algo vergonhoso ou constrangedor",
                "STALKEAR": "Investigar a vida de alguém online",
                'GG': 'Abreviação para Good Game (bom jogo)',
                'EZ': 'Abreviação para Easy (muito fácil)',
                'W': 'Algo bom, vitória, elogiar algo',
                'L': 'Algo ruim, derrota, criticar algo, usado para humilhação',
                }
    
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Palavra não encontrada')
        # O que devemos fazer se a palavra não for encontrada?
