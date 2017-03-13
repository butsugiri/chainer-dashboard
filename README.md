![](./images/dashboard.gif)

## About
This is a dashboard-like app for visualizing `log` file that is dumped by chainer's `training.extensions.LogReport` module.

## Requirements
* Flask (and its dependencies)

## Directory Structure
This app assumes that the result of the experiment is organized by following manner.

```
result/
　├ YYYYMMDD_HH_mm_ss/
　│　└ log
　│　└ setttings.json
　├ YYYYMMDD_HH_mm_ss/
　└ YYYYMMDD_HH_mm_ss/
```

Here, `settings.json` is typically obtained by saving all the arguments provided to `argparse` module.
For example,
```python
parser.add_argument('--gpu  ', dest='gpu', type=int,
                    default=-1, help='GPU ID (Negative value indicates CPU)')
parser.add_argument('--epoch', dest='epoch', type=int,
                    default=72, help='Number of times to iterate through the dataset')
parser.add_argument('--batchsize', dest='batchsize', type=int,
                    default=20, help='Minibatch size')
args = parser.parse_args()
json.dumps(vars(args), sort_keys=True) ## save this as settings.json
```

`log` is the file dumped by chainer's `training.extensions.LogReport` module.

## Usage
`runserver`
