#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.argparser import parse_cli


def main():
    args = parse_cli()
    # diff = generate_diff(args.first_file, args.second_file, args.format)
    # print(diff)
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
