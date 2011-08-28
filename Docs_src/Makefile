
html: index.html ex1.html

index.html: index.txt
	asciidoc -a icons -a theme=flask -o ../html/index.html index.txt

ex1.html: ex1.txt
	asciidoc -a icons -a theme=flask -o ../html/ex1.html ex1.txt

clean:
	rm -f ../html/index.html
	rm -f ../html/ex1.html

