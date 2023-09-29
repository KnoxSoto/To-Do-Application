
import functions
import time
now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is", now)
print("Is below", now)
print("Is below", now)


while True:
    # Get user input and strip the whitespace from it
    user_action = input('Type add, show, edit, complete or exit:  ')
    user_action = user_action.strip()
# Use the match & case function to have different output from the user choice
    #
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

# new_todos =[item.strip('n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
# If user input edit/ Need to change the string to an integer
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a todo: ')
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif 'complete'in user_action:
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
        continue
    elif 'exit' in user_action:
        break
    else:
        print('command is not valid :')


print('Bye')




