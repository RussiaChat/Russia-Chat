import socket
import threading
from colorama import Fore, Back, Style
import os
import time
os.system('clear')

chat = True

print(Fore.RED + '[+]  ----------------  [+]')
print('[+]  ---CHAT---------  [+]')
print('[+]  ------RUSSIA----  [+]')
print('[+]  ----------------  [+]')

print(Fore.GREEN + '[+]  ----------  [Beta versia')
while chat:
  command = input('')
  if command == '/newsr':
    chat = False
    os.system('clear')
    name = input(Fore.GREEN + '[+]  --------  [+] name:')
    port = input(Fore.GREEN +  '[+]  --------  [+] port:')
    os.system('clear')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind (('localhost',38282))
    key = 2848 #Ключ шифрования
    client = [] #Массив адресов клиентов
    print(Fore.BLUE + '[+]  -------- Чат успешно создан! ')
    def xor_cipher(data, key):
       encript_message = ""
       for letter in data:
         
        encript_message += chr(ord(letter) ^ key)
       return encript_message
    while 1:
      data, adress = sock.recvfrom(10240)
      data=data.decode('utf-8')
      data=xor_cipher(data,key)
      print(adress[0], adress[1], data)
      data = xor_cipher(data, key)
      if adress not in client:
        client.append(adress)
        for clients in client:
          if clients == adress:
           continue
           sock.sendto(data.encode('utf-8'),clients)
  
  if command == '/connect':
    def xor_cipher(message, key):
      encript_message = ""
      for letter in message:
       encript_message += chr(ord(letter) ^ key)
      return encript_message
 
  def read_sok():
    while 1:
      data = soc.recv(10240)
      data=data.decode('utf-8')
      data = xor_cipher(data,key)
      print(data)
 
  server = 'localhost', 38282  #Данные сервера
  key = 2848 #Ключ шифрования
  print(Fore.GREEN + 'Nick:')
  nickname = input() #Никнейм для общения
  soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  soc.bind(('localhost', 38252)) #Задаем сокет как клиент
  soc.sendto(xor_cipher((nickname+'Connected'),key).encode('utf-8'), server)#Уведомляем чат о подключении
  thread = threading.Thread(target=read_sok)
  thread.start()
  while 1:
    message = input()
    cripted_message=xor_cipher('['+nickname+'] '+message,key)
    soc.sendto(cripted_message.encode('utf-8'), server)

  else:
    print(Fore.GREEN + '{ Error } -------- Команда не найдена! ')
    time.sleep(3)
    os.system('clear')
    print(Fore.RED + '[+]  ----------------  [+]')
    print('[+]  ---CHAT---------  [+]')
    print('[+]  ------RUSSIA----  [+]')
    print('[+]  ----------------  [+]')
