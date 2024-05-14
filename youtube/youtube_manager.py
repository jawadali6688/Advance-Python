import json

file_name = "youtube.txt"
def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    
    except FileNotFoundError: 
        return []

def save_data_helper(videos):
    with open(file_name, "w") as file:
        return json.dump(videos, file)
    
def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video["name"]} | Duration: {video["time"]}")

def add_video(videos):
    name = input("Enter name of video: ")
    time = input("Enter the time duration of video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    index = int(input("Enter the index number of video: "))

    if 1 <= index <= len(videos):
        name = input("Enter new name of video: ")
        time = input("Enter new time of video: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index selected....")
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index number of video: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        
    else:
        print("Invalid index selected....")


def main():
    all_videos = []
    
    while True:
        
        print("\n")
        print("Youtube Manager || with Database")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the application")

        choice = input("Enter your choice please!....: ")

        match choice:
            case "1":
                list_all_videos(all_videos)
                
            case "2":
                add_video(all_videos)

            case "3":
                update_video(all_videos)

            case "4":
                delete_video(all_videos)
                    
            case "5":
                break
            
            case _:
                print("Oops! Invalid Choice....!")
                
                
if __name__ == "__main__":
    main()