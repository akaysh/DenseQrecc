import argparse
import random
from os import walk
import ast
import pprint
import json
import numpy as np

def shuffle_and_read(path, split_ratio):

    with open(path) as f:
        data = json.loads(f.read())
    assert (args['split_ratio'] >= 0)

    random.shuffle(data)

    train_sub = int(np.floor(len(data)*args['split_ratio']))
    train = data[:train_sub]
    dev = data[train_sub:]

    return train, dev


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Split train data into train and dev with randomization.')
    parser.add_argument('--data_path', help='Directory path of the train data file(s).', required=True)
    parser.add_argument('--data_sub', type=float, help='Fraction of data to subset.', default=None)
    parser.add_argument('--split_ratio', type=float, help='Train Dev data split ratio.', default=None)
    args = vars(parser.parse_args())

    train_data, dev_data = shuffle_and_read(args['data_path'],args['split_ratio'])
    

    train_path = "/".join(args['data_path'].split("/")[:-1]) + '/qrecc_train.json'
    dev_path = "/".join(args['data_path'].split("/")[:-1]) + '/qrecc_dev.json'

    with open(train_path, 'w') as file:
        file.write(json.dumps(train_data, indent=4))
    print(f"Train Split saved in file {train_path}")
    with open(dev_path, 'w') as file:
        file.write(json.dumps(dev_data, indent=4))
    print(f"Dev Split saved in file {dev_path}")