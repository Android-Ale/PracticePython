print('=-'*5+'Emprestimo bancaria consorcio casa'+'-='*5)
v = float(input('Qual é o valor da casa ?'))
s = float(input('Qual o valor do seu salário ?'))
a = int(input('Em quantos anos vc  irá pagar ?'))
pm = (s * 30 // 100)
total = ((pm *a)*12)
em =((pm*a)/12)
print('d', pm)
print('t', total)
print('em', em)
if v >= total:
    print('Total a pagar é R${}, emprestimo será negado.'.format(em))
else:
    print('Total a pagar até o final é R${}, o emprestimo será concedido.'.format(em))