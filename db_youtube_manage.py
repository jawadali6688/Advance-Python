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
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} | Duration: {video['time']}")

def add_video(videos):
    name = input("Enter name of video: ")
    time = input("Enter time duration of video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    index = int(input("Enter the index number of video: "))
    if 1 <= index <= len(videos):
        new_name = input("Enter new name of video: ")
        new_time = input("Enter new time duration of video: ")
        videos[index - 1]["name"] = new_name
        videos[index - 1]["time"] = new_time
        save_data_helper(videos)
    else:
        print("Invalid index.")

def delete_video(videos):
    index = int(input("Enter the index number of video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index.")

def main():
    all_videos = load_data()
    
    while True:
        print("\nYoutube Manager || with Database")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the application")

        choice = input("Enter your choice please!....: ")

        if choice == "1":
            list_all_videos(all_videos)
        elif choice == "2":
            add_video(all_videos)
        elif choice == "3":
            update_video(all_videos)
        elif choice == "4":
            delete_video(all_videos)
        elif choice == "5":
            break
        else:
            print("Oops! Invalid Choice....!")
                
                
if __name__ == "__main__":
    main()
