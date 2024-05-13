
list_videos = ["Python", "Django"]
def list_all_videos():
    print("Here is video list!!")
    for video in list_videos:
        print(video)
def add_videos(video):
    list_videos.append(video)
    print("Here is your updated version of list!!")
    for video in list_videos:
        print(video)
def delete_videos(name):
    index = list_videos.index(name)
    list_videos.pop(index)
    print("Here is your updated version of list!!")
    for video in list_videos:
        print(video)
def update_videos(id, name):
    index = list_videos.index(id)
    list_videos[index] = name
    print("Here is your updated version of list!!")
    for video in list_videos:
        print(video)
def main():
    while True:
        print("\n Enter choice a from list")
        print("1. list of all videos")  
        print("2. add all videos")
        print("3. delete videos")
        print("4. update videos")
        print("5. exits videos")
        chioce = input("enter choice number: ")
        match chioce:
            case '1':
                list_all_videos()
            case '2':
               for video in list_videos:
                    print(video)
               name = input("Enter video name to add: ")
               add_videos(name)   
            case '3':
                for video in list_videos:
                    print(video)
                name = input("Enter video name to delete: ")
                delete_videos(name)
            case '4':
                for video in list_videos:
                    print(video)
                old_name = input("Enter video old name to update: ")
                new_name = input("Enter video new name to update: ")
                
                update_videos(old_name, new_name)
            case '5':
                break
            case _:
                print("invalid choice")     

if __name__ == "__main__":
    main()