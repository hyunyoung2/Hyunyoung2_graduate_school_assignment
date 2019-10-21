# Selected Topic in Computer Science2


If you want to jupyte notebook file and it doesn't work, visit below.

 - [assigment1](https://nbviewer.jupyter.org/github/hyunyoung2/Hyunyoung2_graduate_school_assignment/blob/master/Selected_Topic_in_Computer_Science/Assignment1/Assignment1.ipynb)
 
 - [assigment2](https://nbviewer.jupyter.org/github/hyunyoung2/Hyunyoung2_graduate_school_assignment/blob/master/Selected_Topic_in_Computer_Science/Assignment2/Assignment2.ipynb)



# How to Change ipynb to pdf

I used Jupyter Notebook for assignment of this class.

So, I had to convert jupyter notebook to PDF for report. 

When I did it, I need some configuration to convert from ipynb to PDF

The following is the process of the configuration for report

First, How to convert jupyter notebook to PDF on command line 

> jupyter nbconvert --to pdf file_name.ipynb

And If you use some template, type in like the folowing 

> jupyter nbconvert --to pdf --template what_you_want_to_use file_name.ipynb


The following is text cited in help message of jupyter nbconvert

```
Both HTML and LaTeX support multiple output templates. LaTeX includes
    'base', 'article' and 'report'.  HTML includes 'basic' and 'full'. You
    can specify the flavor of the format used.
    
    > jupyter nbconvert --to html --template basic mynotebook.ipynb
```

Above all,  check if the packages were installed 

1. nbconvert 

> pip3 install nbconvert 

2. Pandoc

For converting markdown to formats other than HTML, nbconvert uses [Pandoc](http://pandoc.org/)(1.12.1 or later)

> sudp apt-get install pandoc

After finishing the process above, convert ipynb to other format,in particular, PDF

BUT IF you get error below, continuouslly read the following

when I typed in it, I got this error like the following:

> OSError: xelatex not found on PATH, if you have not installed xelatex you may need to do so. Find further instructions at https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex.

Just visit the solution URL and install TeX

typing in thing below

> sudo apt-get install texlive-xetex

Then, type in it once again as follows

> jupyter nbconvert --to pdf file_name.ipynb

But if encoding of Korean language appears, fit configuation file, **base.tplx**, on the location which is python3.5/site-packages/nbconvert/templates/latex under /usr/lib or .local/lib as follows

```
\\usepackage{kotex}
%\usepackage[T1]{fontenc}
```











# Reference 

 - [installing Tex](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex)
