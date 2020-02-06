# On the Robustness of Deep Learning-predicted Contention Models for Network Calculus

This repository contains the dataset used for the paper [_"On the Robustness of Deep Learning-predicted Contention Models for Network Calculus"_](https://arxiv.org/abs/1911.10522). We refer to the paper for a full explanation of the methodology used for generating the dataset.


## Getting the dataset

The raw dataset can be accessed via the DOI: [10.14459/2019mp1524892](https://doi.org/10.14459/2019mp1524892).
The following command can be used to download the full dataset via FTP:
```
$ wget -r ftp://m1524892:m1524892@dataserv.ub.tum.de/
```


## Reading the dataset

The dataset is stored as serialized protobuf messages using [pbzlib](https://github.com/fabgeyer/pbzlib-py).

This repository contains an [example python script](https://github.com/fabgeyer/dataset-deeptma-extension/blob/master/example.py) for parsing the files.
To get it and execute it:
```
$ git clone https://github.com/fabgeyer/dataset-deeptma-extension.git
$ cd dataset-deeptma-extension
$ pip3 install -r requirements.txt
$ python3 example.py path/to/dataset.train0.pbz
```

Alternative programming languages may be used with `pbzlib` (e.g. [Java](https://github.com/fabgeyer/pbzlib-java), [Go](https://github.com/fabgeyer/pbzlib-go)).


## Citation

If you use this dataset for your research, please include the following reference in any resulting publication:

```bibtex
@misc{GeyerBondorf_1911.10522,
	author        = {Geyer, Fabien and Bondorf, Steffen},
	title         = {On the Robustness of Deep Learning-predicted Contention Models for Network Calculus},
	year          = {2019},
	month         = nov,
	eprint        = {1911.10522},
	archivePrefix = {arXiv},
}
```
