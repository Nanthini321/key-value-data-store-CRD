import os
import threading 
from threading import*
import time

filepath = "D:\data.json"
d={} 
def changefilepath(path):
    filepath = path

def create(key,value,timeout=0):
    json_file = open(filepath, "r") 
    data = json.load(json_file)
    if key in d:
         print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024):  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
    outfile = open(filepath, "w") #write the given data in json object
    json.dump(data,outfile)
            
def read(key):
    json_file = open(filepath, "r")
    data = json.load(json_file)
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+st(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            string=str(key)+":"+str(b[0])
            return string


def delete(key):
    json_file = open(filepath, "r")
    data = json.load(json_file)
    f = open(filepath, "r")
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            if key in d:
                del d[key]
            print("key is successfully deleted")
     outfile = open(filepath, "w")
    json.dump(data,outfile);
