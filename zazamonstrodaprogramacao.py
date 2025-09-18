RA = int(input('Qual o RA do aluno?'))
NOME = str(input('Qual o nome do aluno?'))
CURSO = str(input('Qual o curso do aluno?'))
NOTA = int(input('Qual foi a primeira nota do aluno?'))
NOTA2 = int(input('Qual foi a segunda nota do aluno?'))
MEDIA = (NOTA + NOTA2) / 2

print('RA do aluno:', RA)
print('Nome do aluno:', NOME)
print('Curso do aluno:', CURSO)
print('Nota do aluno no primeiro bimestre:', NOTA)
print('Nota do aluno no segundo bimestre:' , NOTA2)
print('Media do aluno:', MEDIA)

if MEDIA > 5:
 print('Pode melhorar, mas passou')

     elif MEDIA > 9:
         print('Muito bem!!')

             elif MEDIA == 10:
                 print('Excelente!!')

                     else:
                         print('Melhore na proxima vez')
              



