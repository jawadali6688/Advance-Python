import json
all_videos = []

def main():

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
                list_all_video(all_videos)
                
            case "2":
                add_video(all_videos)

            case "3":
                update_video(all_videos)

            case "4":
                delete_video(all_videos):
                    
            case "5":
                break
            
            case _:
                print("Oops! Invalid Choice....!")