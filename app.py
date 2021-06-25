import click
import json
from itertools import permutations

@click.command()
@click.option('--test', prompt='\nEnter in word to find anagrams')
def main(test):

    perms = [''.join(p) for p in permutations(test.lower())]
    perms = set(perms)

    with open('words_dictionary.json') as f:
        words = json.load(f)

    click.echo("\nThe anagrams for "+test+" are:\n")
    count = False
    for word in perms:
        if word in words:
            if word != test:
                print(word)
                count = True

    if count == False:
        click.echo("There are no anagrams for "+test)

if __name__ == "__main__":
    main()