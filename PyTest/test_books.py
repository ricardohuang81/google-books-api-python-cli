import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import books

def test_const_types():
  assert type(books.URL) is str
  assert type(books.ID_URL) is str
  assert type(books.VOLUME_INFO) is str
  assert type(books.TITLE) is str
  assert type(books.JSON_LIST) is str

def test_search():
  assert callable(books.search)

def test_add():
  assert callable(books.add)

def test_readinglist():
  assert callable(books.readinglist)