import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePath(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4}.png'
    
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(self.filename), len(arquivo))

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')
    
    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')
    
    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')
    
    def test_str(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)


class RecursoTesteCase(TestCase):
    def setUp(self):
        self.recurso = mommy.make('Recurso')
    
    def test_str(self):
        self.assertEqual(str(self.recurso), self.recurso.tecnologia)