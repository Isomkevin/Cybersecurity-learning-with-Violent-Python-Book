import zipfile
from os import getenv
from typing import Union

# get Env Variables
mainPath = getenv("homePath")

def mainFunc() -> None:
  path_to_zip_file: str = f'{mainPath}/Violent_Python/resources/CH1/evil.zip'
  directory_to_extract_to: str  = f'{mainPath}/myViolentPython/resources'
  path_to_passFile: str  = f'{mainPath}/Violent_Python/resources/CH1/dictionary.txt'

  with open(path_to_passFile) as passFile:
    for line in passFile.readlines():
      zFilePWD = bytes(line.strip('\n'), encoding='utf-8')
      guess = extractZfile(path_to_zip_file, directory_to_extract_to, zFilePWD)
      if guess:
        PWDStr= str(guess.decode())
        print(f'[+] Password = {PWDStr}', end='\n\n')
        exit(0)

def extractZfile(path_from, directory_to, password) -> Union[None, bytes]:
  with zipfile.ZipFile(path_from, 'r') as zFile:
    try:
      zFile.extractall(directory_to, pwd=password)
      return password
    except Exception:
      pass 


