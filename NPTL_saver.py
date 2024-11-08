import requests
import shutil
from pathlib import Path


lect_no = input("please see the no. of last lecture...\n")
mod_no = input("plaese see the no. of module(s)\n")

base_url= input("please enter the base url\n")
print(base_url)

Path("/kaggle/working/vid").mkdir(parents=True, exist_ok=True)

destination="/kaggle/working/vid"

with open("num.txt","w") as f:
    f.write(str(1))
    f.close()

def get_lect():
   
    with open("num.txt","r") as f:
            
        x=f.read()
        x=int(x)
        f.close()
        
    return x

def download(url, destination,nop):
    class invalidResponse(Exception):
        pass
    try:
        response= requests.get(url, stream=True)
        
        if response.status_code == 404:
            raise invalidResponse
        with open(destination,"wb") as file_out:
            shutil.copyfileobj(response.raw,file_out)
        print("downloaded successfully ", nop)
        
        error_index=0
        x=get_lect()
        x+=1
        with open("num.txt","w") as f:
            f.write(str(x))
            f.close()
        
    except invalidResponse as e:
        print("error: file not found", e)
        error_index=1
    return error_index
        
def lect_loop(mod_no,base_url, destination):
    mod_no=int(mod_no)
    mod_no+=1
    for mod in range(1,mod_no):
        while True:
            e_index=0
            clect_no=get_lect()
            if clect_no<=9:
                if mod<=9:
                    url_mod=f"mod0{mod}lec0{clect_no}.mp4"
                if mod>9:
                    url_mod=f"mod{mod}lec0{clect_no}.mp4"
                url =f"{base_url}{url_mod}"
                destination_final=f"{destination}/{url_mod}"
                print(url)
                e_index = download(url, destination_final,clect_no)
                print(e_index)
             
                    
            if clect_no>9:
                if mod<=9:
                    url_mod=f"mod0{mod}lec{clect_no}.mp4"
                
                if mod>9:
                    url_mod=f"mod{mod}lec{clect_no}.mp4"
                url=f"{base_url}{url_mod}"
                destination_final=f"{destination}/{url_mod}"
                print(url)
                e_index=download(url, destination_final,clect_no)
  
                
            if e_index==1:
                break
lect_loop(mod_no,base_url, destination)
