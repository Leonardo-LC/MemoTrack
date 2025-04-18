from packages.materia import Materia
from packages.usuario import Usuario

#testa cadastrar materia
user1 = Usuario('James','161078320','James@gmail')
user1.cadastrar_materia('APC','Nilton','2')
print(user1.materias)

#testa cadastrar materia que já foi cadastrada anteriormente
user1.cadastrar_materia('APC','Fabricio','2')

#testa remover materia
user1.remover_materia('APC')
print(user1.materias)

#testa remover matéria não existente
user1.remover_materia('DIAC')