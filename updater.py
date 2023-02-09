import os
import urllib.request
import zipfile
import shutil
import json

class Updater:
    def __init__(self):
        self.url = 'https://github.com/iaZe/Open-Order/archive/main.zip'
        self.version_url = 'https://api.github.com/repos/iaZe/Open-Order/releases/latest'

    def get_version(self):
        with urllib.request.urlopen(self.version_url) as url:
            data = json.loads(url.read().decode())
            return data['tag_name']

    def check_update(self):
        try:
            with open("version.txt", "r") as f:
                current_version = f.read()
                latest_version = self.get_version()
                if latest_version is None:
                    return False

                if current_version < latest_version:
                    return True
                else:
                    return False
        except FileNotFoundError:
            return True

    def download(self):
        urllib.request.urlretrieve(self.url, "update.zip")

    def unzip(self):
        with zipfile.ZipFile("update.zip", "r") as zip_ref:
            zip_ref.extractall()

    def delete_zip(self):
        os.remove("update.zip")

    def move(self):
        shutil.move("Open-Order-main/openorder.pyw", "openorder.pyw")
        shutil.move("Open-Order-main/updater.py", "updater.py")
        shutil.move("Open-Order-main/version.txt", "version.txt")
        shutil.rmtree("Open-Order-main")

    def update(self):
        if self.check_update():
            self.download()
            self.unzip()
            self.move()
            self.delete_zip()

updater = Updater()