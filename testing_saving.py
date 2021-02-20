import os
from multiprocessing import Pool
from urllib import request
from tqdm import tqdm


def fetch_data(x):
    try:
        word_list = ["rdpsn", "rhodo", "rhodopsin"]
        page = request.urlopen(f"https://www.uniprot.org/uniprot/{x}.txt").read()
        page = page.decode("utf-8").split("SEQUENCE")[0].split("\n")
        for i in range(len(page)):
            for i1 in range(len(word_list)):
                if word_list[i1] in page[i]:
                    print(page[i])
    except:
        print("error")
        return


if __name__ == '__main__':
    folder = "seq"
    files = os.listdir(folder)
    seq_list = []

    for i in range(len(files)):
        with open(f"{folder}/{files[i]}") as file:
            text = file.readlines()
            seq = [i.rstrip().lstrip(">").split("/")[0].split("_")[0] for i in text if ">" in i]
            seq_list.extend(seq)
            file.close()

    with Pool(os.cpu_count()) as p:
        p.map(fetch_data, seq_list)

    # pool = Pool(os.cpu_count())
    # for i in tqdm(pool.imap(fetch_data, seq_list), total=len(seq_list)):
    #     pass
