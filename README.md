# Word-Length Text Matcher

This is a simple tool designed to match a string of text with part of a corpus. This can be useful in identifying the plaintext in ciphers where the spaces are the same in the plaintext and the ciphertext. Given enough words, the set of word lengths becomes unique to that string of text, allowing a match to be found in a corpus if the type of plaintext is known but not the text itself e.g. if all plaintext is drawn from the works of Jane Austen but it is not known what exactly it is.

## Arguments and Options

The following options and arguments are available.

- `file` is the corpus of text to search against
- `-v, --verbosity`

The following options are mutually exclusive with one another.

- `-s` specifies a series of integers representing the word lengths
- `-c` specifies the ciphertext to try and find a match for against the corpus

## Examples

```bash
python3 -m wordlengthmatcher -s '4,3,4,4,2,1,5' corpus.txt
```

```bash
python3 -m wordlengthmatcher -c 'kjd menqu djdd m' corpus.txt
```
