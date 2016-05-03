from unittest import TestCase, main
from numeros import Cardinais

class Teste(TestCase):
    def test_unidade(self):
        cardinais = Cardinais()
        n_lista = [0,1,2,3,4,5]
        t_lista = ['zero','um','dois', 'três', 'quatro', 'cinco']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_dezena(self):
        cardinais = Cardinais()
        n_lista = [10,11,12,13,14,15,20,30]
        t_lista = ['dez','onze','doze', 'treze', 'quatorze', 'quinze', 'vinte', 'trinta']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_centena(self):
        cardinais = Cardinais()
        n_lista = [100,200,300,400,500,600,700,800,900]
        t_lista = ['cem','duzentos','trezentos', 'quatrocentos', 'quinhentos',
                    'seissentos', 'setessentos', 'oitocentos', 'novessentos']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_milhar(self):
        cardinais = Cardinais()
        n_lista = [1000,2000,3000,4000,5000,60000]
        t_lista = ['um mil','dois mil','três mil','quatro mil','cinco mil','sessenta mil']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

    def test_mix(self):
        cardinais = Cardinais()
        n_lista = [215, 550, 111, 1201, 1001, 101]
        t_lista = ['duzentos e quinze', 'quinhentos e cinquenta', 'cento e onze',
                    'um mil duzentos e um', 'um mil e um', 'cento e um']

        for num, trans in zip(n_lista,t_lista):
            result = cardinais.transcrever(num)
            self.assertEqual(result, trans)

if __name__ == '__main__':
    main()
