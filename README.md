# On the Robustness of Deep Learning-predicted Contention Models for Network Calculus

This repository contains the dataset used for the article [_"Graph-based Deep Learning for Fast and Tight Network Calculus Analyses"_](https://doi.org/10.1109/TNSE.2020.3025806) published in IEEE Transactions on Network Science and Engineering, and the paper [_"On the Robustness of Deep Learning-predicted Contention Models for Network Calculus"_](https://doi.org/10.1109/ISCC50000.2020.9219693) published at the 2020 IEEE Symposium on Computers and Communications and its [arXiv version]((https://arxiv.org/abs/1911.10522). We refer to the article and paper for a full explanation of the methodology used for generating the dataset.


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
@article{GeyerBondorf_TNSE2021,
	author        = {Geyer, Fabien and Bondorf, Steffen},
	journal       = {IEEE Transactions on Network Science and Engineering},
	title         = {Graph-Based Deep Learning for Fast and Tight Network Calculus Analyses},
	year          = {2021},
	volume        = {8},
	number        = {1},
	pages         = {75--88},
	doi           = {10.1109/TNSE.2020.3025806},
}
```

## License

The data in this repository is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
