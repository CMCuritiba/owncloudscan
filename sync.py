import sys
import os.path
import os

OwncloudRoot = "/var/www/owncloud"

if len(sys.argv) < 2:
    exit()
else:
    FilePath = sys.argv[1]

#O watcher.py executa o script para tudo que for criado dentro da pasta, porem so interessa o upload dos arquivos e nao a criacao das pastas
if not os.path.isfile(FilePath):
    exit()

#Pega o nome do usuario pelo nome da pasta criada pela impressora
FilePathSplit = FilePath.split('/')
UserName = FilePathSplit[len(FilePathSplit)-2]
FileName = FilePathSplit[len(FilePathSplit)-1]

UserFilesRoot = OwncloudRoot + "/data/" + UserName + "/files/"

if not os.path.exists(UserFilesRoot+"scanner"):
    os.system("sudo -u www-data mkdir "+UserFilesRoot+"scanner")

os.system("cp "+FilePath+" "+UserFilesRoot+"scanner/")
os.system("chown www-data:www-data "+UserFilesRoot+"scanner/"+FileName)
os.system('sudo -u www-data /var/www/owncloud/occ --quiet files:scan --path="/'+UserName+'/files/scanner/'+FileName+'"')
os.system('rm -f '+FilePath)
