import PySimpleGUIWeb as sg
import datetime
import statistics_modules as sm
import os

"""
VISUALIZAÇÃO DO MODULO ESTATISTICO

"""
print('Starting up...')

sg.ChangeLookAndFeel('LightGreen') 

txtSobre = """
A Wyden é uma instituição de ensino superior parte de um dos maiores grupos educacionais do mundo, a Adtalem Global Education, que oferece, qualidade internacional e experiência em transformar realidades por meio da educação no mundo inteiro. Oferecemos cursos de Graduação e Pós-Graduação nas modalidades presencial, semipresencial e à distância.
"""

# Menu principal
layout =  [
            [sg.Text('Metrocamp Exatas', size=(60,1), font=('Segoe UI', 20), text_color='red')],
            [sg.Button('Estatistica'),sg.Button('Matematica'),sg.Button('Fisica'),sg.Button('Sobre')],
            [sg.Text('', size=(60,1), font=('Segoe UI', 20), text_color='red')],
            [sg.Text('v1.0', size=(60,1), font=('Segoe UI', 10), text_color='black')],
	          #[sg.Exit('Sair', button_color=('white','red'))]
          ]
#Layout sobre a faculdade
layout3 =  [
            [sg.Text('Metrocamp - Sobre', size=(60,1), font=('Segoe UI', 20), text_color='red')],
            [sg.Text(txtSobre, size=(60,7), font=('Ariel', 12), text_color='black')],
            [sg.Text('Desenvolvedores:', size=(60,1), font=('Ariel', 16), text_color='black')],
            [sg.Text('Luana Santos Lima', size=(60,1), font=('Ariel', 12), text_color='black')],
            [sg.Text('Luís Fernando Sanchez', size=(60,1), font=('Ariel', 12), text_color='black')],
            [sg.Text('Fernando dos Santos da Silva', size=(60,1), font=('Ariel', 12), text_color='black')],
            [sg.Text('Henrique Matheus Florêncio Pini', size=(60,1), font=('Ariel', 12), text_color='black')],
            [sg.Text('Kaian Ferreira dos Santos', size=(60,1), font=('Ariel', 12), text_color='black')],
            [sg.Text('', size=(60,1), font=('Segoe UI', 20), text_color='red')],                                                       
	          [sg.Button('Voltar')],
            [sg.Text('', size=(60,1), font=('Segoe UI', 20), text_color='red')],
            [sg.Text('v1.0', size=(60,1), font=('Segoe UI', 10), text_color='black')],

          ]          
#Layout dos Modulos
layout2 =  [
            [sg.Text('Metrocamp Exatas - Estatistica', size=(60,1), font=('Segoe UI', 20), text_color='red')],
            #Template média
	    [sg.Text('', size=(60,1), font=('Segoe UI', 20), text_color='red')],
	    [sg.Text('Modulo média', size=(60,1), font=('Segoe UI', 20), text_color='red')],
	    [sg.Text('Para utilizar o modulo passe até 100 elementos numericos separados por virgulas', size=(60,1), font=('Arial', 12), text_color='black')],
            [sg.Input(key='data3'),sg.Button('Calcular', key = 'cl_media')],
            [sg.Text('', size=(60,1), font=('Arial', 12), text_color='black',key = 'media')],
            #Template média ponderada
	    [sg.Text('Modulo média ponderada', size=(60,1), font=('Segoe UI', 20), text_color='red')],
	    [sg.Text('Para utilizar o modulo passe 3 elementos numericos separados por virgulas', size=(60,1), font=('Arial', 12), text_color='black')],
            [sg.Input(key='data4'),sg.Button('Calcular', key = 'cl_mediap')],
            [sg.Text('', size=(60,1), font=('Arial', 12), text_color='black',key = 'mediap')],
	    #Template a mediana
	    [sg.Text('Modulo mediana', size=(60,1), font=('Segoe UI', 20), text_color='red')],
	    [sg.Text('Para utilizar o modulo passe até 10 elementos numericos separados por virgulas', size=(60,1), font=('Arial', 12), text_color='black')],
            [sg.Input(key='data'),sg.Button('Calcular', key = 'cl_mediana')],
            [sg.Text('', size=(60,1), font=('Arial', 12), text_color='black',key = 'mediana')],
            #Template a amplitude
	    [sg.Text('Modulo amplitude', size=(60,1), font=('Segoe UI', 20), text_color='red')],
	    [sg.Text('Para utilizar o modulo passe até 10 elementos numericos separados por virgulas', size=(60,1), font=('Arial', 12), text_color='black')],
            [sg.Input(key='data1'),sg.Button('Calcular', key = 'cl_amp')],
            [sg.Text('', size=(60,1), font=('Arial', 12), text_color='black',key = 'amplitude')],
	    #Template a variancia
	    [sg.Text('Modulo variancia', size=(60,1), font=('Segoe UI', 20), text_color='red')],
	    [sg.Text('Para utilizar o modulo passe até 10 elementos numericos separados por virgulas', size=(60,1), font=('Arial', 12), text_color='black')],
            [sg.Input(key='data2'),sg.Button('Calcular', key = 'cl_var')],
            [sg.Text('', size=(60,1), font=('Arial', 12), text_color='black',key = 'varianca')],
	    [sg.Text('', size=(60,1), font=('Arial', 18), text_color='black')],
	    [sg.Button('Voltar')],
      [sg.Text('', size=(60,1), font=('Segoe UI', 20), text_color='red')],
      [sg.Text('v1.0', size=(60,1), font=('Segoe UI', 10), text_color='black')],
          ]

# Cria menu principal
window = sg.Window('Exatas',
                  layout=layout,
                   default_element_size=(12,1),
                   font='Helvetica 18',
                   )

start_time = datetime.datetime.now()
#  Loop de eventos
while True:
   event, values = window.Read(timeout=10)     # read with a timeout of 10 ms
   if event != sg.TIMEOUT_KEY:                 # if got a real event, print the info
        print(event, values)
   # Clique do botao Sobre
   if event == 'Sobre':
        window1 = sg.Window('Exatas - Sobre',	
                  layout=layout3,
                   default_element_size=(12,1),
                   font='Helvetica 18',
                   )
        window = window1

   # Clique no botão estatistica modifica para o layout 2 (layout dos modulos)
   if event == 'Estatistica':
       
        window1 = sg.Window('Exatas - Estatistica',	
                  layout=layout2,
                   default_element_size=(12,1),
                   font='Helvetica 18',
                   )
        window = window1

   # Clique que executa o calculo da média
   if event == 'cl_media':
        try:
          print(sm.media(values['data3'].split(',')))
          media = sm.media(values['data3'].split(','))
          window.Element('media').Update('A media é: '+str(media))
        except:
          window.Element('media').Update('Quantidade de elementos deve ser de até 100 e não pode haver itens não numéricos')
   # Clique que executa o calculo da média ponderada
   if event == 'cl_mediap':
        try:
          values =  values['data4'].split(',')
          print(sm.mediaPonderada(*values))
          mediap = sm.mediaPonderada(*values)
          window.Element('mediap').Update('A media é: '+str(mediap))
        except:
          window.Element('mediap').Update('Quantidade de elementos deve ser igual a 3 e não pode haver itens não numéricos') 

   # Clique que executa o calculo da mediana
   if event == 'cl_mediana':
        try:
          print(sm.mediana(values['data'].split(',')))
          mediana = sm.mediana(values['data'].split(','))
          window.Element('mediana').Update('A mediana é: '+str(mediana))
        except:
          window.Element('mediana').Update('Quantidade de elementos deve ser menor que 11 e não pode haver itens não numéricos')

   # Clique que executa o calculo da amplitude
   if event == 'cl_amp':
        try:
          print(sm.amplitude(values['data1'].split(',')))
          mediana = sm.amplitude(values['data1'].split(','))		
          window.Element('amplitude').Update('A amplitude é: '+str(mediana))
        except:
          window.Element('amplitude').Update('Quantidade de elementos deve ser menor que 11 e não pode haver itens não numéricos')

   # Clique que executa o calculo da varianca
   if event == 'cl_var':
        try:
          print(sm.variancia(values['data2'].split(',')))
          mediana = sm.variancia(values['data2'].split(','))
          window.Element('varianca').Update('A varianca é: '+str(mediana))
        except:
          window.Element('varianca').Update('Quantidade de elementos deve ser menor que 11 e não pode haver itens não numéricos')

   # Clique que volta para o menu principal
   if event == 'Voltar':
        
        window1 = sg.Window('Exatas',
                  layout=layout,
                   default_element_size=(12,1),
                   font='Helvetica 18',
                   )
        window = window1
   #if event in (None, 'Exit', 'Sair'):
   #     break
        
 

# Exiting the program
window.Close()    # fecha o programa
window1.Close()
print('Completed shutdown')
