import os
import cv2
from deepface import DeepFace


# Recognize face
def find_faces(img):
    try:
        result = DeepFace.find(
            img_path=img,
            db_path='./database',
            enforce_detection=False,
            model_name="Facenet",
            detector_backend="retinaface",
            align=True,
        )

        name = f"{result[0]['identity'].iloc[0]}"
        name = name.split("/")

        return name[2]
    except Exception:
        return "unknown"


# Create a folder in database folder
def create_folder():
    while True:
        folder_name = str(input("Enter a folder name: "))

        folder_path = os.path.join('./database', folder_name)
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)

                print(f'Folder {folder_name} created')
                break
            except OSError as e:
                print(e.message)
        else:
            print("Folder already exists. Try another name.")


# Take a picture and store in a specific folder
def take_photo(img, folder_face_default: str | bool):
    database_folder = os.listdir('database')

    if not folder_face_default:
        while True:
            try:
                for i in range(0, len(database_folder)):
                    if not ".pkl" in database_folder[i]:
                        print(f" | [{i}]-{database_folder[i]}")

                face_id = int(input("Enter whose photo it will be: "))

                if face_id in range(0, len(database_folder) + 1):
                    face_folder = f'./database/{database_folder[face_id]}'
                    break
                else:
                    print("Please enter a valid number.")
                    continue
            except ValueError:
                print("Please enter a number.")
    else:
        face_folder = f'./database/{folder_face_default}'

    try:
        file_name = f"{int(len(os.listdir(face_folder))) + 1}"
        cv2.imwrite(f"{face_folder}/{file_name}.jpg", img)
        message = f"The photo of {folder_face_default if folder_face_default else database_folder[face_id]} was taken"
        error = False
    except Exception as e:
        message = e.__context__
        error = True

    return error, message
