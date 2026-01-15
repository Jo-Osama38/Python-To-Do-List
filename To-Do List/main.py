
print ("Wolcome in your list ")

#Function to Add task in List
def adding_task ():
    name_task =input ('Name task is: ').strip().lower()
    with open("list.txt" , "a")as file:
        file.write(name_task+"\n")
    print("The task is adding ✅ ")
    print("=-"*40)

# Function to delete a task
def delete_task():
    name_task = input("Name task for delete: ").strip().lower()

    try:
        with open("list.txt" ,'r')as file:
            lines = file.readlines()
            
        with open("list.txt" , 'w')as f:
            found = False

            for item in lines:
                if name_task != item.strip():
                    f.write(item)
                else:
                    found = True
            if found:
                print("✅ The task is deleted")
            else:
                print("❌ The task not found ")
        print("=-"*40)
    except FileNotFoundError:
        print("your list is empty")

# Function to show your tasks
def show_list():
    try:
        with open("list.txt" ,"r")as file:
            items = file.readlines()
            print('=-'*40)
            for count,item in enumerate(items):

                print(f"{count+1} - {item}",end='')
            print('=-'*40)
    except FileNotFoundError:
        print ("the list is empty try adding first task")
# Function to Empty list
def delete_all ():
    chose = input("You sure (Y\\N) you want delete all tasks :").lower().strip()
    if chose == "y":
        with open ("list.txt","w")as file:
            print("All tasks deleted 🗑️ ")
        
            pass
    else:
        print("Nothing was deleted \n Your tasks are safe ")
        pass
    print("=-"*40)
# Run To-Do List
while True:
    chose=input("adding task '1' \nshow list '2' \ndelete task '3' \ndelete all '4' \nexit '5' \nYour choice: ").strip().lower()
    print('#'*35)
    if chose in ["adding task","adding", "a" ,"add",'1']:
        adding_task()
    elif chose in ["delete task" ,"delete" , "d" ,"del",'3']:
        delete_task()
    elif chose in ['show_list','show_tasks' ,'show' ,"s",'2']:
        show_list()
    elif chose in ["delete all","del all","da",'4']:
        delete_all()
    elif chose in ["exit","e",'5']:
        print("👋 see you soon 👋 \n Your tasks are saved")
        break
    else:
        print("Your choice is worng ,Please try again ")
        print ("=-"*40)

