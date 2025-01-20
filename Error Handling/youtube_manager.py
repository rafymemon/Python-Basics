import json


def load_data():
    try:
        with open("F:\python_programs\Error Handling\youtube.txt", "r") as file:
            test = json.load(file)
            #   print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("F:\python_programs\Error Handling\youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("-" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']} ")
    print("-" * 50)


def add_video(videos):
    name = input("Enter the name of the video ")
    time = input("Enter the time of the video ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("video has been added to the list")


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update "))
    if 1 <= index <= len(videos):
        name = input("Enter the new name of the video ")
        time = input("Enter the new time of the video ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("video has been updated to the list")
    else:
        print("Invalid video index selected.")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print(f"video has been deleted fromthe list")

    else:
        print("Invalid video index selected!")


def main():

    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option below")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice ")

        # print("Total videos are : ",videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()
