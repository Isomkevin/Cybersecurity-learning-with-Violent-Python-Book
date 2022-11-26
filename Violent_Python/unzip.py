import zipfile

def mainFunc() -> None:

  for i in range(1, 8):
    path_to_zip_file = f'./Violent_Python/CH{i}.zip'
    directory_to_extract_to = './Violent_Python'
    
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


mainFunc()