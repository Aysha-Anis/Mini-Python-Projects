import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"{filename} has been created successfully\n")
    except FileExistsError:
        print("File already existed")
    except Exception as e:
        print(f"{e} error occur" )

def view_files():
    files = os.listdir("Txt File Management/")
    if not files:
        print("NO file found")
    else:
        print("Files are :\n")
        for file in files:
            print(file)

def read_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(f"Content of {filename} :\n{content}")
    except FileNotFoundError:
        print("File not Found")
    except Exception as e:
        print(f"{e} error occured")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} deleted successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"{e} error occured")

def update_file(filename):
    try:
        with open(filename,'a') as f:
            content = input("Enter your content : \n")
            f.write(content)
            print("Content added successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"{e} error occured")



def main():
    while True:
        print("Welcome to File Management APP")
        print("Create File ---1\nView File ---2\nRead File ---3\nDelete File ---4\nUpdate File ---5\nExit ---6")

        operation = int(input("Enter your operation : "))

        if(operation==1):
            filename = input("Enter file name : ")
            create_file("Txt File Management/"+filename)

        elif(operation ==2):
            view_files()

        elif(operation ==3):
            filename =input("Enter file name : ")
            read_file("Txt File Management/"+filename)

        elif(operation ==4):
            filename = input("Enter file name : ")
            delete_file("Txt File Management/"+filename)

        elif(operation==5):
            filename = input("Enter file name : ")
            update_file("Txt File Management/"+filename)

        elif(operation==6):
            break
        
        else:
            print("Enter correct operation")

if __name__=='__main__':
    main()