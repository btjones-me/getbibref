import urllib.request

doi = "10.1038/ngeo2248"

x = urllib.request.urlopen('http://api.crossref.org/works/'+doi+'/transform/application/x-bibtex')
data = x.read()
print(data.decode("utf-8"))