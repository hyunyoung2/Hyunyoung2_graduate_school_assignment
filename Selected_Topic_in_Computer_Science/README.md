# Selected Topic in Computer Science


I used Jupyter Notebook for assignment of this class.


So, I had to convert jupyter notebook to PDF. 

It was annoying me for some configuration of it.

So here I write to remember it. 

First, How to convert jupyter notebook to PDF 

jupyter nbconvert --to pdf file_name.ipynb

when I typed in it, I got this error like the following:

> OSError: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.

Just visit the solution URL and install TeX

typing in thing below

> sudo apt-get install texlive-xetex

Then, type in it once again as follows

> jupyter nbconvert --to pdf file_name.ipynb

But if encoding of Korean language appears, fit configuation file, **base.tplx**, on the location which is python3.5/site-packages/nbconvert/templates/latex under /usr/lib or .local/lib as follows

\\usepackage{kotex}
%\usepackage[T1]{fontenc}












# Reference 

 - [installing Tex](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex)
