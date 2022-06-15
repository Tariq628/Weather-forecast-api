# Weather Forecast Json API
## This is weather forecast api built with django.

[![REDIS](https://cldup.com/dTxpPi9lDf.thumb.png)](https://redis.io/)



How can we run this project on 
First of all we need to make virtual environment then activate that.
Install all the required packages
```sh
pip install -r requirements.txt
```

Make sure your REDIS is running on this port 
redis://127.0.0.1:6379/

You can search your query like 
```sh
http://127.0.0.1:8000/mater/data/?search=ABBN
```
You can search any file name in capital letters on the place of **ABBN**
For Example:
```sh
http://127.0.0.1:8000/mater/data/?search=AGGG
```


