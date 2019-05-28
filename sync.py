import sys
import os.path
import pycurl

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

f = open(FilePath, "r")

c = pycurl.Curl()
c.setopt(c.URL,"https://nuvem.cmc.pr.gov.br/remote.php/webdav/scanner"+FileName)
c.setopt(c.USERPWD,"") #Definir a conta usada
c.setopt(c.UPLOAD,1L)
c.setopt(c.READDATA, f)
c.perform()
c.close()
