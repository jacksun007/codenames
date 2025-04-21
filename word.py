#!/usr/bin/python3
import argparse

PACKS = ["vanilla.txt", "duet.txt", "undercover.txt", "potter.txt", "cge.txt", 
         "bgg.txt", "trucker.txt", "holiday.txt", "ages.txt", "blizzard.txt", 
         "simpsons.txt", "halloween.txt", "authors.txt", "disney.txt", "jack.txt" ]

def collect_words(file):
    all_words = []
    for pack in PACKS:
        try:
            with open(pack, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith('#'):
                        continue
                    elif line.startswith(('=', '-', '<')):
                        continue
                    elif line.startswith('>'):
                        word = line[1:].strip()
                    else:
                        word = line

                    if word in all_words:
                        print(f"warning: duplicate found in {pack}: {word}")
                    else:
                        all_words.append(word)
        except FileNotFoundError:
            print(f"warning: file not found: {pack}")

    all_words.sort()
    with open(file, 'w') as f:
        for word in all_words:
            f.write(word + '\n')

def extract_words():
    pass
    
import sys

def process_words(file):
    with open(file, 'r') as f:
        raw_lines = [line.rstrip('\n') for line in f if line.strip()]

    comment_lines = []
    entries = []
    seen_non_comment = False
    i = 0

    while i < len(raw_lines):
        line = raw_lines[i].strip()

        if line.startswith('#'):
            if seen_non_comment:
                print(f"error on line {i + 1}: comments must all be at the top of file")
                sys.exit(1)
            comment_lines.append(line)
            i += 1
            continue

        seen_non_comment = True

        if line.startswith('<'):
            if i + 1 >= len(raw_lines):
                print(f"error: line {i + 1} starts with '<' but is not followed by any line")
                sys.exit(1)

            next_line = raw_lines[i + 1].strip()
            if not next_line.startswith('>'):
                print(f"error: line {i + 1} starts with '<' but is not followed by a matching '>' line")
                sys.exit(1)

            left = line.strip().upper()
            right = next_line.strip().upper()
            key = left[1:].strip()
            entries.append((key, (left, right)))
            i += 2
        else:
            word = line.strip().upper()
            entries.append((word, word))
            i += 1

    entries.sort(key=lambda x: x[0])

    with open(file, 'w') as f:
        for line in comment_lines:
            f.write(line + '\n')
        for _, value in entries:
            if isinstance(value, tuple):  # angled pair
                f.write(value[0].strip() + '\n')
                f.write(value[1].strip() + '\n')
            else:
                f.write(value.strip() + '\n')

            
def main():
    parser = argparse.ArgumentParser(description="Codenames word pack manager")
    subparsers = parser.add_subparsers(dest='command')

    # Collect command
    parser_collect = subparsers.add_parser('collect', aliases=['c'], 
        help='Collect words from all word packs')
    parser_collect.add_argument('file', nargs='?', default='codenames.txt',
        help='Output file for collected words')

    # Extract command
    parser_extract = subparsers.add_parser('extract', aliases=['e'],
        help='Extract original words from infile and write to outfile')
    parser_extract.add_argument('infile', help='Input file containing words')
    parser_extract.add_argument('outfile', nargs='?', default='output.txt',
        help='Output file for extracted words')

    # Process command
    parser_process = subparsers.add_parser('process', aliases=['p'],
        help='Process words in file')
    parser_process.add_argument('file', 
        help='File containing words to be processed')

    args = parser.parse_args()

    if args.command in ['collect', 'c']:
        collect_words(args.file)
    elif args.command in ['extract', 'e']:
        extract_words(args.infile, args.outfile)
    elif args.command in ['process', 'p']:
        process_words(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()