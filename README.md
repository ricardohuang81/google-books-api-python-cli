## Google Books Command Line Interface (CLI) using Python
* Uses the Google Books API to query and retrieve volumes on a public bookshelf by inserting search terms that will show Book Titles
* Can add Books into personal Reading List
* Can view what Books are in your personal Reading List

## Requirements
Must have `python3` and `pip` installed on development machine

## Module Installations (if needed)
1. `pip install click`
2. `pip install requests`
3. `pip install pyfiglet`

## Command to search Book Titles
`python3 books.py search "<Search Term>"`

## Command to add Books to your Reading List
`python3 books.py add "<Book ID>"`

    
## Command to view Reading List of Books
`python3 books.py readinglist`

## Help Commands for using this CLI
`python3 books.py --help`

`python3 books.py search --help`

`python3 books.py add --help`

`python3 books.py readinglist --help`