from tqdm import tqdm
import requests


def download(url: str, fname: str, chunk_size=1024):
    resp = requests.get(url, stream=True)
    print(resp)
    total = int(resp.headers.get('content-length', 0))
    print(total)
    with open(fname + '.mp3', 'wb') as file, tqdm(desc=fname, total=total, unit='KB', unit_scale=True,
                                                  unit_divisor=1024) as bar:
        for data in resp.iter_content(chunk_size=chunk_size):
            size = file.write(data)
            bar.update(size)


download('https://s.voicecards.ru/c/15512.mp3', 'video')

