import serial
import time
conexao = serial.Serial('COM4', 9600)
def pisca(tempo=1):
    while True:
        conexao.write('1') # Escreve 1 no arduino (LED acende)
        time.sleep(tempo) # Aguarda n segundos
        conexao.write('2') # Escreve 2 no arduino (LED apaga)
        time.sleep(tempo) # Aguarda n segundos
if __name__ == '__main__': # Executa a função
    pisca()