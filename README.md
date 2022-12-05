# Source code for "Force-directed graph layouts revisited: a new force based on the t-Distribution". 👋

> Here is the t-FDP source code under clean up. If you want to find experimental data and analysis code, please refer to this [repo](https://github.com/Ideas-Laboratory/t-fdp).

## Environments
The code is tested under ubuntu 20.04.
#### Requires: Anaconda3, python3.8, gcc

#### cmd for conda install:
```
conda install cupy numba scikit-learn
pip install pyfftw numba_kdtree pytorch torchvision pandas dask[dataframe]
pip install numpy==1.20.3
```

#### Setup for BH method.
```
cd bh_tforce
python setup.py build
python setup.py install
```

#### Run the example:

```
python example.py
```


---
If you have any problem, please submit an issue or [email](zhongfahai@gmail.com) us.