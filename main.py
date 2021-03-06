import argparse

from data_handling.create_dataset import make_dataset
from data_handling.transform_dataset import transform_dataset
from train import train_lenet, test
from utils import get_device

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser that controls the script.')

    parser.add_argument('action', help='the action that the script should do.')
    parser.add_argument('--gcommands_fold',
                        help='the path to the root folder of te google commands dataset before splitting.')
    parser.add_argument('--out_path', default='dataset', help='the path where to save the files splitted to folders.')
    parser.add_argument('--dataset', help='the path to the root folder of te google commands dataset after splitting.')
    parser.add_argument('--test_dataset', help='the path to the root folder of the test dataset.')
    parser.add_argument('--model', help='the path to the model.')

    args = parser.parse_args()

    if args.action == 'create_dataset':
        make_dataset(args.gcommands_fold, args.out_path)

    elif args.action == 'transform_dataset':
        transform_dataset(args.dataset)

    elif args.action == 'train':
        device = get_device()
        train_lenet(device, args.dataset)

    elif args.action == 'test':
        device = get_device()
        test(device, args.test_dataset, args.model)
