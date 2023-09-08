todos = ['Städa', 'Handla', 'plugga', 'ge blod']
print (todos)
todo_pop = input("Ta bort todo (index): ")
todo_pop = int(todo_pop)
del todos[todo_pop]
print (todos)