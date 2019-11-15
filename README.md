## Google Books Command Line Interface (CLI) using Python
* Uses the Google Books API to query and retrieve volumes on a public bookshelf by inserting search terms that will show Book Titles, Author, and Publishing Company
* Can add Books into personal Reading List
* Can view what Books are in your personal Reading List

## System Requirements
`python3` and `pip` need to be installed on development machine

## pytest Installation to run Automated Tests
`pip install -U pytest`

## Command to run pytest tests
`pytest` or `pytest -v` for more verbose output

## Module Installations (if needed)
1. `pip install click`
2. `pip install requests`
3. `pip install pyfiglet`

## Command to search Book Titles
`python3 books.py search "<Search Term>" <Optional Results Number>`  
  
<pre>
 Example: `python3 books.py search "Game of Thrones" 4`
</pre>

## Command to add Books to your Reading List
`python3 books.py add "<Book ID>"`  
  
<pre>
  Example: `python3 books.py add "QnAG5M8lpm4C"`
</pre>
    
## Command to view Reading List of Books
`python3 books.py readinglist`

## Help Commands for using CLI
`python3 books.py --help`

`python3 books.py search --help`

`python3 books.py add --help`

`python3 books.py readinglist --help`