# bib2md
[![Python]](https://www.python.org "Python")
> **Note**\
> The program given as is, no warranty given. \
> You can use and modify this program freely.
## Description
>Have you wonder how to put you refferences from `.bib`
>to `.md` files with IEEE format? <br>
Well this program is for you.

## Usecase
You need to quickly format `.bib` file to IEEE standard in `.md` <br>
Converting:
```bib
@article{Polus2021,
   author = {Manhal Elias Polus and Thekra Abbas},
   issue = {2},
   journal = {Eastern-European Journal of Enterprise Technologies},
   pages = {109},
   title = {Development for performance of Porter Stemmer algorithm},
   volume = {1},
   year = {2021},
}
```
Into :

><a id="1">[1]</a> M. E. Polus and T. Abbas, "Development for performance of Porter Stemmer algorithm," Eastern-European Journal of Enterprise Technologies, vol. 1, no. 2, 2021.

The program made considering `.bib` export from mendeley refference manager.<br>
Only in `@book, @article `and` @inproceedings` is currently implemented

## Requirement
> - Python 3.10.x

## Showcase
Running `main.py` as is, will take export.bib
and return `output.md`

```sh
python main.py
```

Having different `.bib` filename you need to change it in `main.py` file


[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&labelColor=FFD43B&logoColor=3776AB&logo=python