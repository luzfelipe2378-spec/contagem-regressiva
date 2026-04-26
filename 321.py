import time

contagem = int(input('Digite a contagem regressiva: '))
msg_final = input('Digite a mensagem final: ')

while contagem > 0:
    print(contagem)
    contagem -= 1
    time.sleep(1)

print(msg_final)