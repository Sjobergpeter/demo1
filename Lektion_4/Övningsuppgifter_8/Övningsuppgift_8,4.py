todos = ['Städa', 'Handla', 'Plugga', 'Ge blod']
print (todos)
value_remove = input("ta bort todo (värde): ")

if value_remove in todos:
    todos.remove (value_remove)
print (todos)