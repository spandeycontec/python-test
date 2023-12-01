import zipfile

# formatted = now.strftime("%Y-%m-%d-%H-%M-%S")
# filename="allzipfile" + formatted + ".zip"

def extract_archive(filepaths,dest_dir):

    with zipfile.ZipFile(filepaths[0], 'r') as zip_ref:
        zip_ref.extractall(dest_dir)
