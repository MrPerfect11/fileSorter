import os
import shutil

def organize_folder(folder_path):
    #Retrieve a list of all the files and directories in the folder.
    items = os.listdir(folder_path)

    #Make a directory for each file extension.
    for item in items:
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            extension = extension.lower()  #To ensure consistency, convert the extension to lowercase.

            #Make a directory for the extension if one does not already exist.
            extension_folder = os.path.join(folder_path, extension[1:])  # Remove the leading dot from the extension
            os.makedirs(extension_folder, exist_ok=True)

            #Sort the file to the proper extension folder.
            new_path = os.path.join(extension_folder, item)

            #If a file with the same name already exists in the target folder, replace it with a number.
            counter = 1
            while os.path.exists(new_path):
                base, ext = os.path.splitext(item)
                new_path = os.path.join(extension_folder, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(item_path, new_path)
            print(f"Moved: {item} to {extension_folder}")

    #Process subfolders
    for item in items:
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):
            organize_folder(item_path)

def organize_downloads_folder(download_folder):
    #Make sure the downloads folder path has a separator.
    download_folder = download_folder.rstrip(os.path.sep) + os.path.sep

    # Go through each subfolder in the Downloads folder.
    organize_folder(download_folder)

if __name__ == "__main__":
    downloads_folder = input("Enter the path to your Downloads folder: ")
    organize_downloads_folder(downloads_folder)
