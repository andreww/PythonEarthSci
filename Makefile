
default: clean html tarfiles

html: index.html ex1.html ex2.html ex3.html ex4.html resources.html install.html all.html images slides

pdf: Docs/all.txt Docs/index.txt Docs/ex1.txt Docs/ex2.txt Docs/ex3.txt Docs/ex4.txt Docs/resources.txt
	a2x Docs/all.txt
	mv all.pdf ../html

index.html: Docs/index.txt
	asciidoc -a icons -a theme=flask -o ../html/index.html Docs/index.txt

ex1.html: Docs/ex1.txt
	asciidoc -a icons -a theme=flask -o ../html/ex1.html Docs/ex1.txt

ex2.html: Docs/ex2.txt
	asciidoc -a latexmath -a icons -a theme=flask -o ../html/ex2.html Docs/ex2.txt

ex3.html: Docs/ex3.txt
	asciidoc -a icons -a theme=flask -o ../html/ex3.html Docs/ex3.txt

ex4.html: Docs/ex4.txt
	asciidoc -a latexmath -a icons -a theme=flask -o ../html/ex4.html Docs/ex4.txt

resources.html: Docs/resources.txt
	asciidoc -a icons -a theme=flask -o ../html/resources.html Docs/resources.txt

install.html: Docs/install.txt
	asciidoc -a icons -a theme=flask -o ../html/install.html Docs/install.txt

all.html: Docs/all.txt Docs/index.txt Docs/ex1.txt Docs/ex2.txt Docs/ex3.txt Docs/ex4.txt Docs/install.txt Docs/resources.txt
	asciidoc -a latexmath -a icons -a theme=flask -o ../html/all.html Docs/all.txt

images: 
	mkdir ../html/images
	cp -r Docs/images/* ../html/images

slides:
	cp Keynote/*.key ../html
	cp Keynote/*.pdf ../html

tarfiles:
	git clean -x -n Practical1 Practical2 Practical3 Practical4 Practical1_solutions Practical2_solutions Practical3_solutions Practical4_solutions
	echo "Or ^C in the next 15 seconds"
	sleep 10
	git clean -x -n Practical1 Practical2 Practical3 Practical4 Practical1_solutions Practical2_solutions Practical3_solutions Practical4_solutions
	tar -czf Practical1.tgz Practical1
	tar -czf Practical2.tgz Practical2
	tar -czf Practical3.tgz Practical3
	tar -czf Practical4.tgz Practical4
	tar -czf Practical1_solutions.tgz Practical1_solutions
	tar -czf Practical2_solutions.tgz Practical2_solutions
	tar -czf Practical3_solutions.tgz Practical3_solutions
	tar -czf Practical4_solutions.tgz Practical4_solutions
	mv *.tgz ../html

clean:
	rm -rf ../html/*
