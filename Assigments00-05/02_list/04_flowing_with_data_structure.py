"""
To see this in action, fill out the add_three_copies(...) function
which takes a list and some data and then adds three copies of the
data to the list. Don't return anything and see what happens! 
Compare this process to the x = change(x) example and note the differences.
"""

def three_copies(my_list, data):

    # add three copies of the data
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    
    # user input message
    message = input("\033[1;3m Enter a message to copy: \033[0m")

    # before empty list 
    my_list = []

    # print before list 
    print("List before:", my_list)

    three_copies(my_list,message)

    # print after list
    print("List after:", my_list)


if __name__ == '__main__':
    main()