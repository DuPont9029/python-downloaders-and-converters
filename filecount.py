import os

def conta_file(cartella):
    count = 0
    for _, _, files in os.walk(cartella):
        count += len(files)
    return count

cartella = "INSERT PATH HERE"  #
numero_file = conta_file(cartella)
print(f"The number of files in the folder {cartella} is: {numero_file}")
