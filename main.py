import sys
import os
import validators
from help import help
from error import error_1
from error import error_2
from start_msg import start
from dir import start_work
from dns import start_work_dns
#from threads import start_work_dns
if len(sys.argv) == 1:
    help()
elif len(sys.argv) == 2:
    if (str(sys.argv[1])).lower() == '-h' or (str(sys.argv[1])).lower() == '--help':
        help()
    else:
        error_2(sys.argv[1])   
elif len(sys.argv) == 3:
    command = sys.argv[1] +" "+sys.argv[2]
    error_2(command)             
elif len(sys.argv) == 4:
    if (str(sys.argv[1])).lower() == 'dir' or (str(sys.argv[1])).lower() == 'dns':
        if (str(sys.argv[1])).lower() == 'dir':
            try:
                text_file = open(sys.argv[2],'r')
                try:
                    link = validators.url(sys.argv[3])
                    if link == 1:
                        count = os.popen(f'wc -l < {sys.argv[2]}')
                        out = count.read().strip()
                        start(sys.argv[3],sys.argv[2],out)
                        start_work(sys.argv[3],sys.argv[2])
                        sys.exit
                    else:
                        print()
                        print("Enter valid url !!") 
                        print()
                        print("Use 'gpost --help' for more information about a command.")   
                except NameError:
                    print("validators Not Installed")
                    print("use 'pip install validators' to install")    
                    sys.exit()
            except FileNotFoundError:
                print("")
                print("Error : Wordlist Not Found.")    
                sys.exit() 
        else:        
            try:
                text_file = open(sys.argv[2],'r')
                try:
                    link = validators.url(sys.argv[3])
                    if link == 1:
                        count = os.popen(f'wc -l < {sys.argv[2]}')
                        out = count.read().strip()
                        start(sys.argv[3],sys.argv[2],out)
                        start_work_dns(sys.argv[3],sys.argv[2])
                        sys.exit
                    else:
                        print()
                        print("Enter valid url !!") 
                        print()
                        print("Use 'gpost --help' for more information about a command.")   
                except NameError:
                    print("validators Not Installed")
                    print("use 'pip install validators' to install")    
                    sys.exit()
            except FileNotFoundError:
                print("")
                print("Error : Wordlist Not Found.")    
                sys.exit()
    else:
        error_1(sys.argv[1])         
