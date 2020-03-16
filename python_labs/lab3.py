"""
  Автор: Гришутенко Павел, группа№1, подгруппа№2
	Вывод таблиц истиности
	Таблицы истиности для and, or, xor, equality
	
	Таблица выведена в текстовом режиме с помощью '*' в качестве логических операций 
  использовались конъюнкция, дизъюнкция, сильная дизъюнкция, эквивалентность
"""

logical_false = 0
logical_true = 1


delimiter  = "*"
space_symbol = " "

header = "* A *" + "* B *" + "* "+" A and B "+ "*"

table_width = len(header)
#print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
#1 and 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_true) and bool(logical_true)))) + "   *"
print(inp_str+res1)
#1 and 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_true) and bool(logical_false)))) + "   *"
print(inp_str+res1)
#0 and 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_false) and bool(logical_true)))) + "   *"
print(inp_str+res1)
#0 and 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_false) and bool(logical_false)))) + "   *"
print(inp_str+res1)
print(delimiter * table_width)
print()
#print (logical_A or logical_B)
header = "* A *" + "* B *" + "* "+" A or B "+ "*"

table_width = len(header)
print(delimiter * table_width)
print(header)
#1 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_true) or bool(logical_true)))) + "   *"
print(inp_str+res1)
#1 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_true) or bool(logical_false)))) + "   *"
print(inp_str+res1)
#0 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_false) or bool(logical_true)))) + "   *"
print(inp_str+res1)
#0 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_false) or bool(logical_false)))) + "   *"
print(inp_str+res1)
print(delimiter * table_width)
print()
#print (logical_A xor logical_B)
header = "* A *" + "* B *" + "* "+" A xor B "+ "*"

table_width = len(header)
print(delimiter * table_width)
print(header)
#1 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_true) != bool(logical_true)))) + "   *"
print(inp_str+res1)
#1 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_true) != bool(logical_false)))) + "   *"
print(inp_str+res1)
#0 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_false) != bool(logical_true)))) + "   *"
print(inp_str+res1)
#0 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_false) != bool(logical_false)))) + "   *"
print(inp_str+res1)
print(delimiter * table_width)
#print (logical_A = logical_B)
print()
header = "* A *" + "* B *" + "* "+" A = B "+ "*"

table_width = len(header)
print(delimiter * table_width)
print(header)
#1 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_true) == bool(logical_true)))) + "   *"
print(inp_str+res1)
#1 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_true)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_true) == bool(logical_false)))) + "   *"
print(inp_str+res1)
#0 or 1
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_true)+" *"

res1 = "*  "+str(int((bool(logical_false) == bool(logical_true)))) + "   *"
print(inp_str+res1)
#0 or 0
print(delimiter * table_width)
inp_str = "* "+str(logical_false)+" ** "+str(logical_false)+" *"

res1 = "*  "+str(int((bool(logical_false) == bool(logical_false)))) + "   *"
print(inp_str+res1)
print(delimiter * table_width)