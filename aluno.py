
class Aluno:
    def __init__(self, matricula, nome, curso, disciplinas, disciplinas_disponiveis):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.disciplinas = []
        for disc in disciplinas:
            for disc_disp in disciplinas_disponiveis:
                if disc == disc_disp.nome:
                    self.disciplinas.append(disc)
                    print("Aluno {} matriculado em {}".format(self.nome, self.disciplinas))
                else:
                    print("Aluno {} NÃO matriculado em {}".format(self.nome, self.disciplinas))

    def insere_disciplina(self, disciplina, disciplinas_disponiveis):
        
            if disciplina in disciplinas_disponiveis:
                self.disciplinas.append(disciplina)
                return "Aluno matriculado"
            else:
                return "Aluno não matriculado"
        

    def imprime_aluno(self):
        print("Matrícula: {}, nome: {}, curso: {}, disciplinas: {}".format(self.matricula, self.nome, self.curso, self.disciplinas))
