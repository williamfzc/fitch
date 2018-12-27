# fitch

> UI automation based on opencv

## Usage

### As `unittest.TestCase` (recommend)

can be easily merged into other framework.

view [sample_testcase.py](sample_testcase.py) for detail.

### Freestyle

or, you can use it directly, as your wish.

view [sample_standalone.py](sample_standalone.py) for detail.

## What it will do

- get screen shot
- detect target picture, and get its location
- check it or operate it

## Installation

Please use python3.

```
pip install fitch
```

## Dependencies

- [pyminitouch](https://github.com/williamfzc/pyminitouch): ui operator
- [findit](https://github.com/williamfzc/findit): detect target picture on screen
- [fastcap](https://github.com/williamfzc/fastcap): screen shot
- [pyatool](https://github.com/williamfzc/pyatool): adb operator

## License

[MIT](LICENSE)
