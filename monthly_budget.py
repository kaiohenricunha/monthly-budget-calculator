# -*- coding: utf-8 -*-
"""monthly_finances.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17UlKe_MrjmO-koTqKQVNA9EhLyxh0I1i
"""

def categories():
    #aqui o usuário insere categorias de despesas mensais, como aluguel, energia, etc
    #vou modificar esse trecho em breve para que as categorias informadas fiquem salvas
    name_list = ['Savings', 'Education', 'Billings', 'Transportation', 'Clothing', 'Housing', 'Personal Expenses']   

    assign_percentages(name_list)

def assign_percentages(listing):
    percent_list = [12, 34, 10, 10, 5, 15, 14]
    names_list = listing


    salary = float(input('How much did you earn this month?'))

    calculate(names_list, percent_list, salary)

def calculate(array_categ, array_percent, wage):
  amount = []
  category = array_categ
  percent = array_percent
  percent_size = len(percent)

  for i in range(percent_size):
    amt = wage * (percent[i] / 100)
    txt = "{valor:.2f}"
    #print(f'{lista_paises[i].ljust(20)}' + txt.format(valor = variacao) + '% entre 2013 e 2020.')
    print(f'\nYou should spend only R$' + txt.format(valor = amt) + f' on {category[i]}')

categories()