import pandas as pd
import json
import os
import requests
import shutil
import tempfile


def url_photos_parser(url, folder_path):
    """
    This method takes the url and the file path as the parameters and
    then parses and creates a folder with seperate photos and title
    url: the string we want to connect the api end points too
    folder_path: the path where the photos and title will be saved
    """
    json_df = pd.read_json(url)
    photo_id, title_id = 0, 0
    for val in json_df["url"]:
        try:
            photo_id = photo_id + 1
            name = str(photo_id) + ".png"
            file_name = os.path.join(folder_path, name)
            res = requests.get(val, stream=True)
            if res.status_code == 200:
                with open(file_name, 'wb') as f:
                    shutil.copyfileobj(res.raw, f)
                print('Image Sucessfully Downloaded: ', file_name)
            else:
                print('Image Couldn\'t be retrieved')
        except Exception as e:
            print("Failed to download the image")

    json_df["title"].to_csv(folder_path + '/title.txt', header=None, index=None, sep=' ', mode='a')

def url_users_parser(url_user, folder_path):
    """
    This method takes the url and the file path as the parameters and
    then parses and creates a csv with user information
    url_user: the string we want to connect the api end points too
    folder_path: the path where the csv will be saved
    """
    r = requests.get(url_user)
    json_str = json.dumps(r.json())
    json_dict_arr = json.loads(json_str)
    dataframe = pd.DataFrame(json_dict_arr)
    dataframe.to_csv(folder_path + "/" + "users_info.csv")


if __name__ == "__main__":
    url_photos_parser("https://jsonplaceholder.typicode.com/photos", "/Users/pranavdtandon/PycharmProjects/GluxKind_Backend/resources/photos_title")
    url_users_parser("https://jsonplaceholder.typicode.com/users", "/Users/pranavdtandon/PycharmProjects/GluxKind_Backend/resources")