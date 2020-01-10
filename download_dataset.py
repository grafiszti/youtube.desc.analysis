import os

import pandas as pd
from googleapiclient.discovery import build
from tqdm import tqdm


def youtube_search(developer_key: str, search_query: str = "Google", max_results: int = 50):
    youtube = build(serviceName='youtube', version='v3', developerKey=developer_key)
    search_response = youtube.search().list(q=search_query, part='id,snippet', maxResults=max_results).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(
                {
                    "id": search_result["id"]["videoId"],
                    "search_query": search_query,
                    "kind": search_result["id"]["kind"],
                    "publishedAt": search_result["snippet"]["publishedAt"],
                    "channelId": search_result["snippet"]["channelId"],
                    "title": search_result["snippet"]["title"],
                    "description": search_result["snippet"]["description"],
                    "channelTitle": search_result["snippet"]["channelTitle"]
                }
            )

    return pd.DataFrame(videos)


def main():
    developer_key_filepath = "developer_key.txt"
    result_dataset_path = "dataset.csv"
    queries_to_download = ["programming", "coding", "data science", "dogs", "cats", "kittens", "monkeys"]
    elements_per_query = 50

    if not os.path.exists(developer_key_filepath):
        print("Developer key file does not exists, please provide file which contain your developer key.")
        return

    with open(developer_key_filepath, "r") as f:
        developer_key = f.readline()

    if os.path.exists(result_dataset_path):
        print("Dataset with given name :`{}`, currently exists.".format(result_dataset_path))
    else:
        df = pd.concat(
            [youtube_search(developer_key, query, elements_per_query) for query in tqdm(queries_to_download)])
        df.to_csv(result_dataset_path, index=False)
        print("Dataset saved in `{}`.".format(result_dataset_path))


if __name__ == '__main__':
    main()
