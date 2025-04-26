from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://Rafypy:Rafypy@cluster0.y9frmoy.mongodb.net/", tlsAllowInvalidCertificates=True)
# not a good idea to include id and passowrd in code files
# tlsAllowInvalidCertificates=True - Not a good way to handle ssl errors, but for testing purposes it is ok

db = client["youtube_manager"]
videos_collection = db["videos"]

print(videos_collection)


def list_all_videos():
    print("*" * 50)

    for videos in videos_collection.find():
        print(
            f" ID : {videos['_id']}, Name : {videos['name']} and Time : {videos['time']}"
        )
    print("*" * 50)


def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})


def update_video(video_id, new_name, new_time):
    videos_collection.update_one(
        {"_id": ObjectId(video_id)}, 
        {"$set": {"name": new_name}, "time": new_time}
    )


def delete_video(video_id):
    videos_collection.delete_one({"id": video_id})
    print("video has been deleted from the list")


def main():
    while True:
        print("\n Youtube Manager with db || Choose an option below")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the name of the video: ")
            time = input("Enter the time duration of the video: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the name of the video: ")
            time = input("Enter the time duration of the video: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
# Compare this snippet from 11_database_mongodb/youtube_manager_mongodb.py:
