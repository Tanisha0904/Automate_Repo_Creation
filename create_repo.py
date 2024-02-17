import os
import requests
from pprint import pprint
import argparse
from secrets_1 import GITHUB_TOKEN
parser=argparse.ArgumentParser()
parser.add_argument("--name", "--n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args=parser.parse_args()
print(args)

username="Tanisha0904"
repo_name=args.name
is_private=args.is_private

API_URL="https://api.github.com"

if is_private:
    payload='{"name": "'+repo_name+'", "private":true}'
    
else:
    payload='{"name": "'+repo_name+'", "private":false}'
    
print(payload)
# payload='{"name":"{repo_name}"}'

headers={
    "Authorization":"token "+ GITHUB_TOKEN,
    "Accept": "application/vnd.github+json"
}
try:
    r=requests.post(API_URL+"/user/repos", data=payload, headers=headers)
    r.raise_for_status()

except requests.exceptions.RequestException as err:
    raise SystemExit(err)

try:
    repo_path="D:\BMC\Create_Repo_Auto" #path to the directory where you want to create your repository in local computer  
    #below are some shell commands run in python using the os system functions to execute specific commands and os change directory 
    os.chdir(repo_path)
    os.system('mkdir '+repo_name)
    os.chdir(repo_path+"\\"+repo_name)
    #below are the usual git commands that we run when we create a new repo 
    os.system("git init")
    os.system("git remote add origin https://github.com/"+username+"/"+repo_name+".git")
    os.system("git add .")   
    os.system("git commit -m 'Initial Commit'")   
    os.system("echo '# "+repo_name+"' >> README.md")    
    os.system("git push -u origin main")   

except FileExistsError  as err:
    raise SystemExit(err)


pprint(r.json())