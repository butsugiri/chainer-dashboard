![](./images/dashboard.gif)

## About
This is a dashboard-like app for visualizing `log` file that is dumped by chainer's `training.extensions.LogReport` method.

## Requirements
* Python 3.4 (or newer)
* Flask (and its dependencies)
* matplotlib
* pandas
* seaborn

I strongly recommend installing these requirements by anaconda.

## Installation
Clone this repo

```
git clone https://github.com/butsugiri/chainer-dashboard.git
```

Cd to the cloned dir and run

```
python setup.py install
```

Make sure you have proper directory structure (as described below) and run

```
runserver
```

Finally, open `http://localhost:5555/`

## Directory Structure
This app assumes that the result of the experiment is organized by the following manner.

When executing `runserver`, the app automatically detects results dir and displays the log files inside.

```
result/
　├ YYYYMMDD_HH_mm_ss/
　│　├ log  # dumped by chainer
　│　└ setttings.json  # create this by yourself
　├ YYYYMMDD_HH_mm_ss/
　└ YYYYMMDD_HH_mm_ss/
```

Here, `settings.json` is a dictionary object that contains hyperparamers.
Typically this is obtained by saving all the arguments that are provided to `argparse` module.
For example,

```python
### set hyperparameters ###
parser.add_argument('--gpu  ', dest='gpu', type=int,
                    default=-1, help='GPU ID (Negative value indicates CPU)')
parser.add_argument('--epoch', dest='epoch', type=int,
                    default=72, help='Number of times to iterate through the dataset')
parser.add_argument('--batchsize', dest='batchsize', type=int,
                    default=20, help='Minibatch size')
args = parser.parse_args()

### save hyperparameters ###
json.dumps(vars(args), sort_keys=True)
```

`log` is the file dumped by chainer's `training.extensions.LogReport` method.
