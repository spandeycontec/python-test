import zipfile
import pathlib
from datetime import datetime
now = datetime.now()
formatted = now.strftime("%Y-%m-%d-%H-%M-%S")
filename="allzipfile" + formatted + ".zip"

def make_archive(filepaths,dest_dir):
    dest_dir = pathlib.Path("output",filename)
    with zipfile.ZipFile(dest_dir,'w') as archive:
        
        for filepath in filepaths:
            filepath=pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)
    

if __name__ == '__main__':
    make_archive(filepaths=['match_case.py','printname.py'],dest_dir='output')
