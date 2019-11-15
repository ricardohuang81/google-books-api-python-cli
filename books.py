import os # portable way of using operating system dependent functionality
import pprint # prints arbitrary data structures in a form that can be used as input to the interpreter
import json # data interchange format
import click  # package for CLIs - porvides arbitrary nesting of commands and automatic generation of Help Pages
import requests  # allows you to send HTTP/1.1 requests, can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access response data in the same way
from pyfiglet import Figlet # full port of FIGlet into pure python - makes large letters out of ordinary text
fig = Figlet(font = 'small') # adjusts Fitlet letters to a smaller size

# Constants that will be used throughout the program
URL = 'https://www.googleapis.com/books/v1/volumes'
ID_URL = 'https://www.googleapis.com/books/v1/volumes/{}'
VOLUME_INFO = 'volumeInfo'
TITLE = 'title'
JSON_LIST = 'readinglist.json'

@click.group() # creates a new Group with a function as callback
def main():
    "Basic CLI for querying and adding books to Reading List using the Google Books API"
    pass

@main.command()
@click.argument('query', default = '')  # provide default value
@click.argument('max', default = 5) # provide default value
def search(query, max):
    queryKey = 'q' # variable for 'q'
    ID = 'id'  # varible for 'id'
    authors = 'authors' # variable for 'authors'
    "Returns 5 (maximum) search results"
    print(fig.renderText("Searching..."))

    if not query:
        click.echo("Some popular search terms include 'Harry Potter','Twilight','Python', 'Game of Thrones', 'JavaScript'")
        query = click.prompt("Enter a Book Title to search: ")
    else:
        click.echo('List of books available for given Search: "{}"'.format(query))

    query = "+".join(query.split())
    query_params = {
        queryKey: query,
        'maxResults': max
    }

    response = requests.get(URL, params = query_params)

    for response in response.json()['items']: # loop through Books List
        # pprint.pprint(response)
        if 'publisher' not in response[VOLUME_INFO] and 'authors' not in response[VOLUME_INFO]:
            click.echo("ID: " + response[ID] + " | Title: " + response[VOLUME_INFO][TITLE]+" | Author: N/A" + " | Publishing Company: N/A")
        elif 'authors' not in response[VOLUME_INFO]:
            click.echo("ID: " + response[ID] + " | Title: " + response[VOLUME_INFO][TITLE]+" | Author: N/A" + " | Publishing Company: " + response[VOLUME_INFO]['publisher'])
        elif 'publisher' not in response[VOLUME_INFO]:
            click.echo("ID: " + response[ID] + " | Title: " + response[VOLUME_INFO][TITLE]+" | Author: " + response[VOLUME_INFO][authors][0] + " | Publishing Company: N/A")
        else:
            click.echo("ID: " + response[ID] + " | Title: " + response[VOLUME_INFO][TITLE]+" | Author: " + response[VOLUME_INFO][authors][0] + " | Publishing Company: " + response[VOLUME_INFO]['publisher'])

# print("what is this?", callable(search))

@main.command()
@click.argument('id', default = '', metavar = '<Book ID>')
def add(id):
    read = 'r' # variable for 'r'
    write = 'w' # variable for 'w'
    "Adds a Book into your Reading List by inputing <Book ID>"
    if not id:
        id = click.prompt("Enter a Book ID to add it in to your Reading List: ")
    bookDetails = requests.get(ID_URL.format(id))
    if('error' not in bookDetails.json()):
        if os.path.exists(JSON_LIST):
            jsonFile = open(JSON_LIST, read) # Opens and Reads the JSON File
            data = json.load(jsonFile) # Loads JSON File
            jsonFile.close()
            for response in data: # Loop through Reading List
                available = False
                if (response['id'] == id):
                    available = True
            if(not available):
                with open(JSON_LIST, write) as outfile: # Writes Book Information you added to JSON File (Reading List)
                    data.append(bookDetails.json())
                    json.dump(data, outfile)
                    print(fig.renderText("Book Successfully Added to Reading List"))
            else:
                click.echo("This Book is already in your Reading List.")
        else:
            with open(JSON_LIST, write) as outfile:
                data = []
                data.append(bookDetails.json())
                json.dump(data, outfile)
                print(fig.renderText("Book Successfully Added to Reading List"))
    else:
        click.echo("Invalid, please enter valid Book ID.")

@main.command()
@click.argument('sortby', default = '')
def readinglist(sortby):
    read = 'r' # variable for 'r'
    "Lists all Book Titles in Reading List"
    if os.path.exists(JSON_LIST):
        jsonFile = open(JSON_LIST, read) # Opens and Reads the JSON File
        data = json.load(jsonFile) # Loads JSON File
        jsonFile.close()
        if not sortby:
            newlist = data
        else:
            newlist = sorted(data, key = lambda e: e.get(VOLUME_INFO, {}).get(sortby))
        for response in newlist: # traversal of your Reading List
            click.echo("Title: "+ response[VOLUME_INFO][TITLE])
    else:
        click.echo("There are currenlty no Books in your Reading List.")

if __name__ == "__main__":
    main()
