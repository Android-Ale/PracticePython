tot = list()
c = 0
m1 = list()
m2 = list()
m3 = list()
m4 = list()
m5 = list()
m6 = list()
m7 = list()
m8 = list()
m9 = list()
produto = 0
m1.append(int(input('Digite o valor:')))
if m1[0]% 2 == 0:
    produto += m1[0]
m2.append(int(input('Digite o valor:')))
if m2[0]% 2 == 0:
    produto += m2[0]
m3.append(int(input('Digite o valor:')))
if m3[0]% 2 == 0:
    produto += m3[0]
m4.append(int(input('Digite o valor:')))
if m4[0]% 2 == 0:
    produto += m4[0]
m5.append(int(input('Digite o valor:')))
if m5[0]% 2 == 0:
    produto += m5[0]
m6.append(int(input('Digite o valor:')))
if m6[0]% 2 == 0:
    produto += m6[0]
m7.append(int(input('Digite o valor:')))
if m7[0]% 2 == 0:
    produto += m7[0]
m8.append(int(input('Digite o valor:')))
if m8[0]% 2 == 0:
    produto += m8[0]
m9.append(int(input('Digite o valor:')))
if m9[0]% 2 == 0:
    produto += m9[0]
print(f'{m1}{m2}{m3}')
print(f'{m4}{m5}{m6}')
print(f'{m7}{m8}{m9}')
if m4[0] >= m5[0] and m4[0] >= m6[0]:
    print(f'A {m4[0]}° é a maior')
if m5[0] >= m4[0] and m5[0] >= m6[0]:
    print(f'A {m5[0]}° é a maior  ')
if m6[0] >= m4[0] and m6[0] >= m5[0]:
    print((f'A {m6[0]}° é a maior'))
total = m3[0] + m6[0] + m9[0]
print(f'A adição das númerações da terceira conluna é {total}')
print(f'A adição das númerações pares são {produto}')




#outra maneira de fazer:
#while c < 9:
    #tot.append(int(input('Digite ')))
    #c += 1
    #if c == 1:
        #m1.append(tot[:])
        #tot.clear()
   ## if c == 2:
        #m2.append(tot[:])
        #tot.clear()
    #if c == 3:
     #   m3.append(tot[:])
 #   if c == 4:
  #      m4.append(tot[:])
   #     tot.clear()
    #if c == 5:
     #   m5.append(tot[:])
      #  tot.clear()
 #   if c == 6:
  #      m6.append(tot[:])
   #     tot.clear()
  #  if c == 7:
   #     m7.append(tot[:])
    #    tot.clear()
 #   if c == 8:
  #      m8.append(tot[:])
   #     tot.clear()
#    if c == 9:
 #       m9.append(tot[:])
  #      tot.clear()