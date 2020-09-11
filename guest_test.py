prompt = "\n请输入您的名字："
message = input(prompt)
file_name = 'welcome.txt'
if message != 'quit':
    print("欢迎" + message + "!")
with open(file_name, 'a') as file_object:
    file_object.write(message + '\n')


print(message)
