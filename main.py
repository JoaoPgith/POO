from aluno import Aluno
from disciplina import Disciplinas

disciplinas_disponives = []

disc = Disciplinas("POO", "Alysson", 64, "LECI")
disciplinas_disponives.append(disc)

disc2 = Disciplinas("Matematica", "Euler", 32, "I2118")
disciplinas_disponives.append(disc)


aluno1 = Aluno("20224006068", "Joao", "ECA", ["ECOP"], disciplinas_disponiveis)

print(aluno1.disciplinas)

aluno1.imprime_aluno()

aluno1.insere_disciplinas("ciencias humanas", disciplinas_disponives)
print(aluno1.disciplinas)
