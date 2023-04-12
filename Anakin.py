import time
import ascii
import pyttsx3
import requests
import pywhatkit
import wikipedia
import webbrowser
from datetime import date
from datetime import datetime
from googletrans import Translator, constants


print('\n')
print('------------------------------------------------------------------')
print('       db                                         88              ')
print('      d88b                              88        ""              ')
print('     d8  8b                             88        88               ')
print('    d8    8b     8b,dPPYba,  ,adPPYYba, 88   ,d8  88 8b,dPPYba,   ')
print('   d8YaaaaY8b    8P     `"8a ""     `Y8 88 ,a8"   88 8P     `"8a  ')
print('  d8""""""""8b   88       88  ,adPPPPP8 8888[     88 88       88  ')
print(' d8          8b  88       88 88,    ,88 88`"Yba,  88 88       88  ')
print('d8            8b 88       88 `"8bbdP"Y8 88   `Y8a 88 88       88  ')
print('\n------------------------------------------------------------------')
print('\nOlá!, Me chamo Anakin e sou o seu novo assistente virtual. 😄')
print('Agora que já me apresentei, que tal eu lhe mostrar alguns comandos? Caso esteja interessado, é só digitar "help" que lhe darei todas as informações.')
print('------------------------------------------------------------------------------------------------------------------------------------------------------\n')

def calculadora():

    num1 = float(input('Digite o primeiro número: '))
    operacao = input('Digite a operação desejada (+, -, *, /): ')
    num2 = float(input('Digite o segundo número: '))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        print('Operação inválida!')
        return None

    print('Resultado: ', resultado)
    return resultado

def comando_user():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'brazil' in voice.id:
            engine.setProperty('voice', voice.id)
            
    comando = input('Digite algo para Anakin: ').lower()

    if 'data' in comando:
        data = date.today()
        dataBR = '{}/{}/{}'.format(data.day, data.month, data. year)
        engine.say('A data de hoje é')
        engine.runAndWait()
        print('\nA data de hoje é:',dataBR, '\n')
        print('\n------------------------------------\n')
        
    if 'horas' in comando:
        hora_atual = datetime.now().strftime('%H:%M')
        engine.say('A hora atual é', hora_atual)
        engine.runAndWait()
        print('\nA hora atual é:',hora_atual, '\n')
        print('\n------------------------------------\n')
      

    if 'navegador' in comando:
        webbrowser.open('https://www.google.com/')
        print('Abrindo navegador', '\n')
        print('\n------------------------------------\n')

    if 'calculadora' in comando:
        resultado = calculadora()
        if resultado is not None:
            engine.say('O resultado da operação é')
            engine.runAndWait()
            engine.say(resultado,'\n')
            engine.runAndWait()
            print('\n------------------------------------\n')


    if 'pesquisa' in comando:
        resultado = input('O que você deseja saber?: \n')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(resultado,10)
        print(resultado, '\n')
        print('\n------------------------------------\n')


    if 'toque' in comando:
        escolha = input('Você deseja ver os resultados da sua busca? (s/n): ')
        music = input('O que você deseja ouvir?: ')

        if escolha.lower() == 's':
            webbrowser.open(url= f'https://www.youtube.com/results?search_query={music}')

        if escolha.lower() == 'n':
            pywhatkit.playonyt(music)
            time.sleep(1)
        print('------------------------------------')
        time.sleep(1)
        
       
    if 'buscar' in comando:
        busca = input('O que você deseja saber?: ')
        search = f'https://www.google.com/search?q={busca}'
        webbrowser.open(url=search,)
        engine.say('Procurando informações sobre a sua busca')
        engine.runAndWait()
        print('\n------------------------------------\n')


    if 'nome' in comando:
        print('Meu nome é Anakin, em homenagem a um personagem de Star Wars.')
        engine.say('Meu nome é Anakin, em homenagem a um personagem de Star Wars.')
        engine.runAndWait()
        print('\n------------------------------------\n')


    if 'clima' in comando:
        webbrowser.open('https://www.google.com.br/search?q=meu+clima')
        engine.say('Procurando informações sobre o seu clima com base na sua localização atual')
        engine.runAndWait()
        print('\n------------------------------------\n')

    if 'ascii' in comando:
        url = input('Insira o URL da imagem: ')
        output = ascii.loadFromUrl(url)
        print(output)
        print('\n------------------------------------\n')

    
    if 'piada' in comando:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        data = response.json()
        joke = data['setup'] + "\n" + data['punchline']
        print('\n',joke)
        translator = Translator()
        translated_joke = translator.translate(joke, dest='pt').text
        print('\n',translated_joke)
        print('\n------------------------------------\n')
   
       
    if 'help' in comando:
        print('Comandos: ↓↓↓ \n', 
            'Data\n',
            'Horas\n',
            'Navegador\n',
            'Calculadora\n',            
            'Pesquisa\n',
            'Toque\n',
            'Buscar\n',
            'Nome\n',
            'Clima\n',
            'Ascii\n',
            'piada\n',
            'Sair\n')
        print('\n------------------------------------\n')


    if 'vader' in comando:
        print('''

                     ⡀⣀⣀⣤⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣶⣿⣿⡿⣿⢿⣷⣽⣿⣿⣿⣷⣆⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣛⣽⣿⠿⠿⢻⣿⡟⣷⣼⣉⣿⣿⣿⣿⣟⠻⣿⣿⣟⢿⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⢏⣤⣶⣿⣿⣿⢹⣿⣿⡟⣿⣿⣿⣿⣿⣷⣄⣈⣻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠿⣿⣇⣿⣿⣿⣿⣿⣿⣾⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⡁⢿⣿⣟⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⣿⣿⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⡿⣿⡏⠉⢻⣿⣿⣿⣿⣿⣿⢸⣿⣿⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⢿⣿⣙⣿⣿⡟⠁⠀⠀⢸⠀⠘⠀⠀⠀⣿⣿⣿⣿⣿⣿⢸⣿⡏⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣶⣻⡿⠋⣹⣿⡀⠀⠀⢀⣿⣀⠀⣀⣶⣴⣿⣿⣷⣿⣷⣦⣬⣻⣧⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠟⣹⣿⢋⣀⣿⡿⠿⠿⠷⣶⢾⣿⡟⢙⣿⠿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣅⢻⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢣⣾⣿⣿⣿⣿⡿⠿⠿⣿⣶⣦⣼⣿⣧⣤⣾⣿⣿⣛⣛⡛⠿⣿⣿⣿⡍⢿⣿⣟⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⠋⠉⢛⣿⣿⣿⣿⣟⣿⣿⣿⣟⢉⣽⣿⣿⣷⣮⣿⣿⣿⣦⡀⣿⣾⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣷⣰⣿⣿⣿⡿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣷⡜⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⠀⣿⣿⣯⣼⣿⣿⣿⣷⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣆⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣿⡿⣿⣿⣽⣤⣽⣛⣛⣛⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⡿⣿⣿⣧⣬⣥⣴⡿⠿⣻⣧⣟⣿⣿⠿⠿⠿⢿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⣹⣿⣿⣿⣾⠋⠉⠹⣿⣿⣷⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣷⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⢸⣿⣿⣿⣭⣦⣤⣤⣿⣿⡻⣷⣤⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⣇⠀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣴⢟⣿⡿⢻⣿⣿⣿⣿⣿⣿⣿⣌⣿⣟⢿⣟⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⡄⠀
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣿⡿⣳⣿⣿⡟⢻⣿⣿⣿⣿⣿⣟⣿⣧⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢳⡀
⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣷⣿⣿⡿⠇⠸⠿⠸⢿⣟⣿⣿⣮⣱⢿⣿⡋⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠁
⠀⠉⠙⠛⠛⠛⠛⠛⢛⣿⣿⣿⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⣸⣿⣷⣎⣿⣿⣯⣁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣷⣦⣀⣀⣠⣠⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⠀⠀
⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠉⠉⠉⠉⢉⣽⣿⣿⣄⣀⣴⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣶⣦⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           
             Darth Vader Mode Actived.../''')
        
        escolha = input('Digite 1 para consultar cnpj e 2 para cep: ')

        if escolha == '1':

            cnpj = input('Digite o CNPJ: ') # substitua pelo CNPJ que você deseja consultar

            response = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')

            if response.status_code == 200:
                    data = response.json()
                    print('\n')
                    print('Nome empresarial:', data['nome'])
                    print('Nome fantasia:', data['fantasia'])
                    print('Endereço:', data['logradouro'], data['numero'], data['complemento'], data['bairro'])
                    print('Cidade:', data['municipio'], '(', data['uf'], ')', 'CEP:', data['cep'])
                    print('Atividade principal:', data['atividade_principal'][0]['text'])
                    print('Atividades secundárias:')
                    for atividade in data['atividades_secundarias']:
                        print(atividade['text'])
                    print('QSA:')
                    print('Situação:', data['situacao'])
                    print('Data de abertura:', data['abertura'])
                    print('Telefone:', data['telefone'])
                    print('E-mail:', data['email'])
                    print('Capital social:', data['capital_social'])
                    print('Natureza jurídica:', data['natureza_juridica'])
                    print('Órgão expedidor:', data['logradouro'])
                    print('Documento:', data['numero'])
                    print('\n')

            else:
                print('Erro ao buscar o CNPJ:', response.status_code)


        if escolha == '2':

            cep = input('Digite o endereço CEP: ') # Digite o CEP que você deseja buscar
            url = f'https://viacep.com.br/ws/{cep}/json/'

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                print('\n')
                print('Endereço:', data['logradouro'])
                print('Complemento:', data['complemento'])
                print('Bairro:', data['bairro'])
                print('Cidade:', data['localidade'])
                print('Estado:', data['uf'])
                print('\n')
            else:
                print('Erro ao buscar o CEP:', response.status_code)


        if escolha == 'darth':
            print('''
            ÁREA DE EXTREMO RISCO, A RESPONSABILIDADE É SUA!
-----------------------------------------------------------------------
            ⠀⢀⣈⣻⣿⣿⣿⣶⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣡⣶⣿⣷⣶⣍⠻⣿⣿⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⣿⣿⣿⣿⣿⣿⣷⡙⣿⣿⡆⠀
⠀⠀⠀⠤⠤⠤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⡟⢻⣿⣿⣿⣇⢹⣿⣿⡄
⠀⢰⡄⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣿⡟⣸⣿⣿⣇
⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⣿⣿⣿⠟⣱⣿⣿⣿⣿ 
⣭⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⡿⢟⣫⣷
⠈⢻⡿⣶⣾⣭⣽⣛⣛⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣛⣛⣻⣭⣽⣷⣶⣿⣿⣿⡏
⠀⠈⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠈⠉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠀⠀⠈⢉⣉⣩⣭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠛⣛⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠿⠿⠛⠋⠉⠀⠀
                        Death Star......Loading[DEATH!]
           ''')
            
            print('\nFilmes e Séries [1]: ',
                  '\nAnimes e Mangás [2]: ',
                  '\nOráculo [3]: ',
                  '\nDeep Web [4]: ',
                  '\nYou Are a Pirate [5]: ',
                  '\nThe Pirate Bay [6]: ',
                  '\n4Chan [7]: ',
                  '\nNavegador recomendado [8]: ',
                  '\nJogos [9]: ',
                  '\nSe arrependeu de ter vindo? tudo bem.. digite "anakin" e tudo estará bem novamente..',
                  )
            
            dark = input('\nQuais opções o senhor deseja?: ')

            if dark == '1':
                print('''
                \nLinks:
                \nhttps://vizer.tv/
                \nhttps://digaonline.pro/
                \nhttps://redecanais.la/
                \nhttps://pobreflix.biz/
                \nhttps://netcine.to/
                \nhttps://megafilmeshd50.com/
                \nhttps://megatela.sx/

               Bônus:\nhttps://www.southparkstudios.com.br/seasons/south-park

                ''')
                      
            if dark == '2':
                print('''

                \nLinks abaixo 

                \nhttps://www.anitube.vip/
                \nhttps://animefire.net/
                \nhttps://animesbrasil.org/
                \nhttps://animesbr.cc/
                \nhttps://animesup.top/
                
                \nhttps://mangalivre.net/
                \nhttps://muitomanga.com/
                \nhttps://www.brmangas.net/
                \nhttps://mangaschan.com/
                
                ''')
            if dark == '3':
                print('''
                \nLinks abaixo. e eu recomendo não ficar muito dependente delas, afinal é uma ferramenta

                \nhttps://openai.com/blog/chatgpt
                \nhttps://you.com/
                \nhttps://app.writesonic.com/

                ''')
            if dark == '4':
                print('''
                \nAcesse por sua conta e risco!

                *Não clique em links desconhecidos

                *Confirme que o URL está correto

                *Use senhas fortes

                *Use uma VPN

                *Use e-mails alternativos

                *Não forneça informações pessoais

                *Evite os serviços de proxy

                *Cubra sua webcam e microfone

                *Não baixe nada

                *Evite fazer compras

                *Use um software antivírus

                \n*Cuidado para que seus dados não parem no mercado negro. Se você acha que foi vítima de roubo de identidade ou fraude, denuncie o golpe da internet como faria com qualquer outro crime.

                1-Passo
                    Instale um navegador compatível com links.onion
                    *https://www.torproject.org/pt-BR/download/

                \n2-Passo
                    VPN
                    https://protonvpn.com/pt_br/free-vpn/

                \n3-Passo 
                    LEIA A PORRA DO TEXTO NOVAMENTE E TENHA CERTEZA DO QUE ESTÁ PRESTES A FAZER!

                \n4-Passo
                    Links e Nomes

                    The Hidden Wiki
                    DuckDuckGo
                    Sci-Hub

                    Ahmia — http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/

                    DuckDuckGo — https://3g2upl4pq6kufc4m.onion

                    Hidden Wiki — http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page

                    TORCH – http://xmh57jrzrnw6insl.onion/ 

                    https://hackersec.com/conheca-mais-de-100-sites-que-voce-pode-acessar-na-deep-web/

                      ''')
            if dark == '5':
                print(''' 
                \nVocê é um pirata agora!
                https://piratelol.ytmnd.com/

                ''')
                print()
            if dark == '6':
                print(''' 
                \nAqui tem de tudo e um pouco mais

                https://pirate-bay-proxy.org/pt/

                ''')
            if dark == '7':
                print('''
                \nNão recomendo muito alguém ficar vagando aqui

                https://www.4chan.org/

                ''')
            if dark == '8':
                print(''' 
                \nNavegador sem anúncios e com uma privacidade boa/moderada

                https://brave.com/pt-br/download/


                ''')
            if dark == '9':
                print(''' 
                \nJogos crackeados

                https://fitgirl-repacks.site/
                https://steamunlocked.net/

                ''')

            if dark == 'anakin':
                print('\nOk, hora de voltar ao mundo real')
                return comando


    if 'sair' in comando:
        engine.say('Desligando o Assistente virtual')
        engine.runAndWait()
        exit()

while True:
    comando_user()
