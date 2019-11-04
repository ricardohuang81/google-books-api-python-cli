import os # portable way of using operating system dependent functionality
import json # data interchange format
import click  # package for CLIs - porvides arbitrary nesting of commands and automatic generation of Help Pages
import requests  # allows you to send HTTP/1.1 requests, can add headers, form data, multipart files, and parameters with simple Python dictionaries, and access response data in the same way
from pyfiglet import Figlet # full port of FIGlet into pure python - makes large letters out of ordinary text
fig = Figlet(font = 'small') # adjusts Fitlet letters to a smaller size


@click.group() # creates a new Group with a function as callback
def main():
    "Basic CLI for querying and adding books to Reading List using the Google Books API"
    pass

@main.command()
@click.argument('query', default='')  # provide default value
@click.argument('max', default = 5) # provide default value
def search(query, max):
    "Returns 5 (maximum) search results"
    print(fig.renderText("Searching..."))
    if not query:
        click.echo("Some popular search terms include 'Harry Potter','Twilight','Python', 'Game of Thrones', 'JavaScript'")
        query = click.prompt("Enter a Book Title to search: ")
    else:
        click.echo('List of books available for given Search: "{}"'.format(query))

    url = 'https://www.googleapis.com/books/v1/volumes'

    query = "+".join(query.split())

    query_params = {
        'q': query,
        'maxResults': max
    }

    response = requests.get(url, params = query_params)

    for response in response.json()['items']: # loop through Books List
        click.echo("Book ID: " + response['id'] + " | Book Title: " + response['volumeInfo']['title']+" | Book Author: "+ response['volumeInfo']['authors'][0] + " | Book Publishing Company: " + response['volumeInfo']['publisher'])

@main.command()
@click.argument('id', default='', metavar='<Book ID>')
def add(id):
    "Adds a Book into your Reading List by inputing <Book ID>"
    url = 'https://www.googleapis.com/books/v1/volumes/{}'
    if not id:
        id = click.prompt("Enter a Book ID to add it in to your Reading List: ")
    bookDetails = requests.get(url.format(id))
    if('error' not in bookDetails.json()):
        if os.path.exists('readinglist.json'):
            jsonFile = open('readinglist.json', 'r') # Opens and Reads the JSON File
            data = json.load(jsonFile) # Loads JSON File
            jsonFile.close()
            for response in data: # Loop through Reading List
                available = False
                if (response['id'] == id):
                    available = True
            if(not available):
                with open('readinglist.json', 'w') as outfile: # Writes Book Information you added to JSON File (Reading List)
                    data.append(bookDetails.json())
                    json.dump(data, outfile)
                    print(fig.renderText("Book Successfully Added to Reading List"))
            else:
                click.echo("This Book is already in your Reading List.")
        else:
            with open('readinglist.json', 'w') as outfile:
                data = []
                data.append(bookDetails.json())
                json.dump(data, outfile)
                print(fig.renderText("Book Successfully Added to Reading List"))
    else:
        click.echo("Invalid, please enter valid Book ID.")

@main.command()
@click.argument('sortby', default='')
def readinglist(sortby):
    "Lists all Book Titles in Reading List"
    if os.path.exists('readinglist.json'):
        jsonFile = open('readinglist.json', 'r') # Opens and Reads the JSON File
        data = json.load(jsonFile) # Loads JSON File
        jsonFile.close()
        if not sortby:
            newlist = data
        else:
            newlist = sorted(data, key=lambda e: e.get('volumeInfo', {}).get(sortby))
        for response in newlist: # traversal of your Reading List
            click.echo("Book Title: "+ response['volumeInfo']['title'])
    else:
        click.echo("There are no Books in your Reading List.")

if __name__ == "__main__":
    main()
