#!/usr/bin/env python3

import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        binary = FirefoxBinary('/usr/lib/firefox/firefox')
        self.browser = webdriver.Firefox(firefox_binary=binary)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Maria decidiu utilizar o novo app TODO. Ela entra em sua página principal:
        self.browser.get('http://localhost:8000')

        # Ela nota que o título da página menciona TODO
        self.assertIn('To-Do', self.browser.title)

        # Ela é convidada a entrar com um item TODO imediatamente

        # Ela digita "Estudar testes funcionais" em uma caixa de texto

        # Quando ela aperta enter, a página atualiza, e mostra a lista
        # "1: Estudar testes funcionais" como um item da lista TODO

        # Ainda existe uma caixa de texto convidando para adicionar outro item
        # Ela digita: "Estudar testes de unidade"

        # A página atualiza novamente, e agora mostra ambos os itens na sua lista

        # Maria se pergunta se o site vai lembrar da sua lista. Então, ela verifica que
        # o site gerou uma URL única para ela -- existe uma explicação sobre essa feature

        # Ela visita a URL: a sua lista TODO ainda está armazenada

        # Satisfeita, ela vai dormir


if __name__ == '__main__':
    unittest.main()
