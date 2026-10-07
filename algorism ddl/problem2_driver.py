import sys
from problem2 import SinglyLinkedList


my_list=SinglyLinkedList()


for line in sys.stdin:
    line=line.strip()

    if line=="" or line.startswith("#"):
        continue

    parts=line.split()
    command=parts[0]

    try:
        if command=="append" and len(parts)==2:
            my_list.append(int(parts[1]))

        elif command=="prepend" and len(parts)==2:
            my_list.prepend(int(parts[1]))

        elif command=="insert" and len(parts)==3:
            my_list.insert(int(parts[1]),int(parts[2]))

        elif command=="get" and len(parts)==2:
            index=int(parts[1])
            print("get(" + str(index) + ") = " + str(my_list.get(index)))

        elif command=="find" and len(parts)==2:
            value=int(parts[1])
            print("find(" + str(value) + ") = " + str(my_list.find(value)))

        elif command=="len" and len(parts)==1:
            print("len = " + str(len(my_list)))

        elif command=="update" and len(parts)==3:
            my_list.update(int(parts[1]),int(parts[2]))

        elif command=="delete" and len(parts)==2:
            value=int(parts[1])

            if my_list.delete(value)==False:
                print("Warning")

        elif command=="delete_at" and len(parts)==2:
            index=int(parts[1])
            print("delete_at(" + str(index) + ") = " + str(my_list.delete_at(index)))

        elif command=="print_list" and len(parts)==1:
            my_list.print_list()

        else:
            print("Warning")

    except (ValueError,IndexError):
        print("Warning")


print("Final list: ",end="")
my_list.print_list()