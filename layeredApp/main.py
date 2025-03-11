from views.userView import UserView
from views.PostView import PostView

def main():
    userview = UserView()
    postview = PostView()

    while True:
        print("\nMenu:")
        print("1 - Create User")
        print("2 - List Users")
        print("3 - Create Post")
        print("4 - List Posts")
        print("5 - Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            userview.createUser()
        elif choice == "2":
            userview.listUsers()
        elif choice == "3":
            postview.createPost()
        elif choice == "4":
            postview.listPosts()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()