import shutil
import tarfile
import os
import schedule
import time

DiretorioOrigem = r"C:\Users\ingri\OneDrive\Área de Trabalho\teste1"
DiretorioDestino = r"C:\Users\ingri\OneDrive\Área de Trabalho\teste2"

def FazerBackup(DiretorioOrigem, DiretorioDestino):
    for root, _, files in os.walk(DiretorioOrigem):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(DiretorioDestino, os.path.relpath(source_file, DiretorioOrigem))
            dest_dir = os.path.dirname(dest_file)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            shutil.copy2(source_file, dest_file)

def CompactaraBckup(DiretorioDestino):
    with tarfile.open(DiretorioDestino + '.tar.gz', 'w:gz') as tar:
        tar.add(DiretorioDestino, arcname=os.path.basename(DiretorioDestino))

def remover_arquivos_origem():
    shutil.rmtree(DiretorioOrigem)

#Irá inicializar o backup e compactar os arquivos,
def BackupCompactar():
    print("Iniciando o backup do diretório:", DiretorioOrigem)
    FazerBackup(DiretorioOrigem, DiretorioDestino)
    print("Backup concluído.")

    print("Iniciando a compactação do diretório:", DiretorioDestino)
    BackupCompactar(DiretorioDestino)
    print("Compactação concluída.")


#Essa parte não é extremamente necessária, pois seu diretório inicial será excluido, a não ser que voce deseja elimina-lo.
    #print("Removendo arquivos do diretório de origem:", DiretorioOrigem)
   # remover_arquivos_origem()
    #print("Remoção concluída.")

#Isso é o agendamento do backup, nesse caso está programado para realizar o backup de cinco em cinco horas
#Importante ressaltar que o primeiro backup será realizado após cinco horas, e não na hora em que você startar a aplicação.

#--------------------------------------------------------------------------------
schedule.every(5).hours.do(BackupCompactar)
#--------------------------------------------------------------------------------
while True:
    schedule.run_pending()
    time.sleep(1)
