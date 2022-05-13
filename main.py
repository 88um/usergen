
import requests
import random
import os
import time

class Generator:

    def check(self,word): #Make sure the first/last letter is not a underscore or dot and that there isnt two dots 
        return word not in users and not word.isdigit() and word[0] != "." and word[0] != "_" and ".." not in word and not word.endswith(".") and self.check2(word)

    def check2(self,word):
        return any(i.isdigit() for i in word) or "." in word or "_" in word

    def check3(self,word):
        return "-" not in word and " " not in word

    def threeL(self,count):
        added = 0
        while added!=count:
            word = "".join(random.choice(letters) for i in range(3))
            if word not in users:
                users.append(word) #Make sure the word hasnt been generated already
                file.write(f"{word}\n")
                added+=1

    def threeC(self,count):
        added = 0
        while added!=count:
            word = "".join(random.choice(letters2) for i in range(3))
            if self.check(word): 
                users.append(word)
                file.write(f"{word}\n")
                added+=1

    def fourL(self,count):
        added = 0
        while added!=count:
            word = "".join(random.choice(letters) for i in range(4))
            if word not in users:
                users.append(word)
                file.write(f"{word}\n")
                added+=1

    def fourC(self,count):
        added = 0
        while added!=count:
            word = "".join(random.choice(letters2) for i in range(4))
            if self.check(word):
                users.append(word) 
                file.write(f"{word}\n")
                added+=1
    
    def singleWord(self,count):
        added = 0
        while added!=count:
            try:
                url = f"https://random-word-form.herokuapp.com/random/noun/{random.choice(letters)}?count={count}"
                words = requests.get(url).text
                for i in words.split(","):
                    word = i.replace('"',"").replace(']',"").replace("[","")
                    if word not in users and self.check3(word):
                        users.append(word) 
                        file.write(f"{word}\n")
                        added+=1
            except:pass
    

if __name__ == "__main__":
    gen = Generator()
    os.system('cls' if os.name == 'nt' else 'clear')
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters2 = "._1234567890"+letters
    file = open("users.txt",'a')
    users = open("users.txt",'r').read().splitlines()
    choice = input("\n[1] Generate 3L\n[2] Generate 3C\n[3] Generate 4L\n[4] Generate 4C\n[5] Generate Single-Words\n\n[+] Choose one: ")
    count = int(input("[+] How many to generate?: "))
    print("Generating...")
    if choice == "1":
        gen.threeL(count)
    elif choice == "2":
        gen.threeC(count)
    elif choice == "3":
        gen.fourL(count)
    elif choice == "4":
        gen.fourC(count)
    elif choice == "5":
        gen.singleWord(count)
    else:print("[!] Invalid choice");time.sleep(2);exit(0);
    print(f"\n[!] Done generated {count} users ==> Saved to users.txt")
    time.sleep(5)
