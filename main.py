# POO
class Celular:
    marca = 'Nokia'
    cor = 'Azul'
    tem_camera = False

    def fazer_ligacoes(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Despertando...')

    def somar(self, v1, v2):
        return v1 + v2

celular = Celular()     

print(celular.tem_camera)
print(celular.marca)

celular.fazer_ligacoes()
celular.jogar_cobrinha()
celular.despertador()

resultado = celular.somar(3,6)
print(resultado)