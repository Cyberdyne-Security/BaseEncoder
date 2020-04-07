import base64
import codecs
import sys
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)


# Hex is base16 , base64.b16decode(Hex String as Byte[Must be Upper Case])

# Codecs codecs.encode(my_bytes, "[zip or bz2]")

Banner = """

 ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗███╗   ██╗███████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝████╗  ██║██╔════╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║  ██║ ╚████╔╝ ██╔██╗ ██║█████╗  
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║  ██║  ╚██╔╝  ██║╚██╗██║██╔══╝  
╚██████╗   ██║   ██████╔╝███████╗██║  ██║██████╔╝   ██║   ██║ ╚████║███████╗
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═══╝╚══════╝
                                                                            


This Module Encodes in:

Base85, Base64, Base32, Base16{hex}, Reverse, Replace

=====================================================================================|
How to Use:                                                                          |              
                                                                                     |   
1-    Start Commands With --> help                                                   |                   
                                                                                     |           
2-    Put your Code in Paste_bin then Save                                           |                               
                                                                                     |                                                  
3-    Do the Command You Like then Open the Paste_bin                                |       
                                                                                     |   
4-    This Module was Developed to Make things Easier for Developers                 |                       
=====================================================================================|
By CyberdyneSM101   
          
Contact at Discord: CyberdyneSM101#9233                     
"""
print(Banner)

Help = """
Tool Commands
=============

    Commands                   Description
    ---------                 ----------------------
    base85enc                 Encode with Base85
    base85dec                 Decode Base85  
    
    base64enc                 Encode with Base64
    base64dec                 Decode Base64                      
    
    base32enc                 Encode with Base32             
    base32dec                 Decode Base32     
    
    base16enc                 Encode with Base16[Hex]                         
    base16dec                 Decode Base16                  
    
    reverse                   reverse the Code
    replace                   replace character with another 
      
    help                      Show Tool Commands Menu
    exit                      Exit the Tool
"""

# https://emojiforu.com/text-art/ascii-thumbs-up-text-art/

def start_bin():
    f = open('Paste_bin.txt','w')
    f.close()

def read_bin():
    f = open('Paste_bin.txt','r')
    try:
        x = f.read()
        return x
    finally:
         f.close()

def paste_bin(x):
    f = open('Paste_bin.txt','w')
    try:
        f.write(x)
    finally:
         f.close()

def base85encode(x):
    return (base64.b85encode(bytes(x,'utf-8'))).decode()

def base85decode(x):
    return (base64.b85decode(bytes(x, 'utf-8'))).decode()

def base64encode(x):
    return (base64.b64encode(bytes(x, 'utf-8'))).decode()

def base64decode(x):
    return (base64.b64decode(bytes(x, 'utf-8'))).decode()

def base32encode(x):
    return (base64.b32encode(bytes(x, 'utf-8'))).decode()

def base32decode(x):
    return (base64.b32decode(bytes(x, 'utf-8'))).decode()

def base16encode(x):
    return (codecs.encode(bytes(x,'utf-8'),'hex')).decode()

def base16decode(x):
    return (codecs.decode(bytes(x, 'utf-8'), 'hex')).decode()

def reverse(x):
    return ''.join(reversed(x))

def replacer(string):
    replace_this=input("Your Character: ")
    with_this=input("Change to: ")
    return string.replace(f'{replace_this}',fr'{with_this}')

pathname = os.path.dirname(sys.argv[0])

while True:
    if os.path.isfile(pathname+'/Paste_bin.txt') == False:
        start_bin()
    else:pass
    try:
        Main = input("[*]Commands: ")

        if Main == 'help':
            print(Help)
        elif Main == 'exit':
            sys.exit()
        elif Main == 'base85enc':
            paste_bin(base85encode(read_bin()))
            print(Fore.GREEN +"[+]Encoded")

        elif Main == 'base85dec':
            paste_bin(base85decode(read_bin()))
            print(Fore.GREEN +"[+]Decoded")

        elif Main == 'base64enc':
            paste_bin(base64encode(read_bin()))
            print(Fore.GREEN +"[+]Encoded")
        elif Main == 'base64dec':
            paste_bin(base64decode(read_bin()))
            print(Fore.GREEN +"[+]Decoded")

        elif Main == 'base32enc':
            paste_bin(base32encode(read_bin()))
            print(Fore.GREEN +"[+]Encoded")
        elif Main == 'base32dec':
            paste_bin(base32decode(read_bin()))
            print(Fore.GREEN +"[+]Decoded")

        elif Main == 'base16enc':
            paste_bin(base16encode(read_bin()))
            print(Fore.GREEN +"[+]Encoded")
        elif Main == 'base16dec':
            paste_bin(base16decode(read_bin()))
            print(Fore.GREEN +"[+]Decoded")

        elif Main == 'reverse':
            paste_bin(reverse(read_bin()))
            print(Fore.GREEN +"[+]Reversed")

        elif Main == 'replace':
            paste_bin(replacer(read_bin()))
            print(Fore.GREEN +"[+]Replaced")
        else:
            print(Fore.RED +"[-]Please Input Right Command")
        continue

    except:
        print(Fore.RED +"[-]Can't Decode please Check your Code")
        continue
# https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/