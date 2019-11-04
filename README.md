## Google Books Command Line Interface (CLI) using Python
The Bookshelf collection allows you to view bookshelf metadata as well as to modify the contents of a bookshelf.

## Requirements
You must have python3 and pip installed on your machine

## Installations
1. ``` pip install click ```
2. ``` pip install requests ```
3. ``` pip install pyfiglet ```

## Help for every command
`python books.py --help`

`python books.py search --help`

`python books.py read --help`

`python books.py add --help`

`python books.py mybooks --help`

`python books.py clearbooks --help`

## Search for Books
`python books.py search <name>`

 You can pass a optional parameter to this like max response this is defaulted to 20
    
`python books.py search <name> <max>`

## Read Books description'
`python books.py read <bookID>`

## Adding Books in to shelf
`python books.py add <bookID>`

## Adding Books in to shelf
`python books.py add <bookID>`
    
## Reading books from Shelf
`python books.py mybooks`
`python books.py mybooks title`
`python books.py mybooks pageCount`

## Clearing all books from Shelf
`python books.py clearbooks`# google-books-api-python-cli
# google-books-api-python-cli
# google-books-api-python-cli
