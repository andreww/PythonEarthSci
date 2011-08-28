
html: index.html ex1.html resources.html

pdf: index.txt
	a2x index.txt

index.html: index.txt
	asciidoc -a icons -a theme=flask -o ../html/index.html index.txt

ex1.html: ex1.txt
	asciidoc -a icons -a theme=flask -o ../html/ex1.html ex1.txt

resources.html: resources.txt
	asciidoc -a icons -a theme=flask -o ../html/resources.html resources.txt

clean:
	rm -f ../html/index.html
	rm -f ../html/ex1.html

