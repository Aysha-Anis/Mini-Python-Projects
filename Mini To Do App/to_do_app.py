
def main():
    print(f"Welcome to To Do app")
    plan = []
    task_number=int(input(f"Please enter how many task you want to enter : "))
    
    for i in range(task_number):
        task= input(f"Enter task {i+1} :")
        plan.append(task)

    print(f"TOday's task's are : {plan}")

    while True:
        operation = input("Enter 1(Add)/2(Update)/3(Delete)/4(View)/5(Exit):")
        if operation == '1':
            task = input(f"Enter your task :")
            plan.append(task)
        elif operation =='2':
            update = input("Enter which task you want to update :")
            if update not in plan:
                print(f"No such item found\n")
            else:
                new_val=input("Enter new task : ")
                ind = plan.index(update)
                plan[ind]=new_val
                print(f"Updated successfully\n")
            
        elif operation =='3':

            delete = input("Which item you want to delete :")
            if delete not in plan:
                print(f"No such item found\n")
            else:
               ind = plan.index(delete)
               del plan[ind]
               print(f"Deleted successfully\n")

            
        elif operation=='4':
            print(f"{plan}\n")
        elif operation=='5':
            break
        else:
            print(f"Please enter an valid operation ")
                    



if __name__=='__main__':
    main()