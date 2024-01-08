from django.test import TestCase

from core.forms import ContatoForms

class ContatoFromTestCase(TestCase):
    def setUp(self):
        self.nome = 'xxxx xxx'
        self.email = 'xxx@gmail.com'
        self.asssunto = 'xxxxxx'
        self.mensagem = 'xxxxxxxxxxxx'
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.asssunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForms(data=self.dados)
    
    def test_send_email(self):
        form1 = ContatoForms(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEqual(res1, res2)
