
html: index.html ex1.html ex2.html resources.html all.html

pdf: all.txt index.txt ex1.txt ex2.txt resources.txt
	a2x all.txt

index.html: index.txt
	asciidoc -a icons -a theme=flask -o ../html/index.html index.txt

ex1.html: ex1.txt
	asciidoc -a icons -a theme=flask -o ../html/ex1.html ex1.txt

ex2.html: ex2.txt
	asciidoc -a icons -a theme=flask -o ../html/ex2.html ex2.txt

resources.html: resources.txt
	asciidoc -a icons -a theme=flask -o ../html/resources.html resources.txt

all.html: all.txt index.txt ex1.txt resources.txt
	asciidoc -a icons -a theme=flask -o ../html/all.html all.txt


clean:
	rm -f ../html/index.html
	rm -f ../html/ex1.html
	rm -f ../html/ex2.html

