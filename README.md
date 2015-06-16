## killprocess

This is a simple python script that takes program names and kills them if exist.
- Works on Windows, Mac, and Linux

## Requirements
python 2.7
pustil https://pythonhosted.org/psutil/

## Install psutil
You can download 'psutil' at https://pypi.python.org/pypi/psutil
(link may change. You can google 'psutil'.)

```
tar zxvf psutil.x.y.z.tar.gz

```
where x.y.z is a version number.

```
python setup.py install

```

Or use 'pip'

```
pip install psutil

```

## Usage

```
python killprocess.py prog1 prog2 ... prog_n

```
## Example

```
python killprocess.py musicagent.exe movieagent.exe

```
This command will kill "musicagent.exe" and "movieagent.exe" if they exist.
