import threading
import time
import random

class Filosofo(threading.Thread):
    executando = True

    def __init__(self, nome, garfo_esquerda, garfo_direita):
        threading.Thread.__init__(self)
        self.nome = nome
        self.garfo_esquerda = garfo_esquerda
        self.garfo_direita = garfo_direita

    def run(self):
        self.pensar()

    def pensar(self):
        while (self.executando):
            print('%s esta pensando.' % self.nome)
            time.sleep(random.uniform(3, 13))
            self.comer()

    def comer(self):
        garfo1, garfo2 = self.garfo_esquerda, self.garfo_direita

        print('%s esta pegando os garfos.' % self.nome)
        while self.executando:
            garfo1_disponivel = garfo1.acquire()
            garfo2_disponivel = garfo2.acquire()
            if garfo1_disponivel and garfo2_disponivel: break
            garfo1.release()
            # garfo1, garfo2 = garfo2, garfo1
        else:
            return

        print('%s esta comendo.' % self.nome)
        time.sleep(random.uniform(1, 10))
        print('%s parou de comer.' % self.nome)
        garfo2.release()
        garfo1.release()