import atheris

with atheris.instrument_imports():
  from html.parser import HTMLParser
  import sys

def TestOneInput(data):
    try:
        string = data.decode('utf-8')
        parser = HTMLParser()
        parser.feed(string)
    except UnicodeDecodeError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()