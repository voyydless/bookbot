# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

### Features

- Counts total number of words in a text file
- Counts the frequency of each character
- Sorts and displays character frequency in descending order
- Supports UTF-8 encoded text files

### Usage

Run the program with a path to your text file:

```bash
python3 main.py books/your-book.txt
```

Example output:
```
============ BOOKBOT ============
Analyzing words found at books/your-book.txt...
----------- Word Count ----------
Found 1234 total words
--------- Character Count -------
e: 100
t: 90
a: 80
...
============= END ===============
```

### Project Structure

- `main.py` - Main program file with command-line interface
- `stats.py` - Core text analysis functions
- `books/` - Directory containing sample text files


