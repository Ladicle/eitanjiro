# Eitanjiro

scraping words list for eijiro pro

## Preparing

### Install dependency packages

1. Setup virtualenv
   ```
   $ virtualenv .venv
   $ source .venv/bin/activate
   ```

2. Install packages
   ```
   $ pip install -r requirements.txt
   ```

### Install Chrome Driver

1. Check path of Chrome
   ```
   $ ls /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
   ```
   
2. Download ChromeDriver from this [site][0]
   ```
   $ curl -L -O http://chromedriver.storage.googleapis.com/2.23/chromedriver_mac64.zip
   ```
   
3. Unarchive ChromeDriver and Move to `/usr/local/bin`
   ```
   $ unzip chromedriver_mac64.zip
   Archive:  chromedriver_mac64.zip
   inflating: chromedriver
   
   $ mv chromedriver /usr/local/bin
   ```


## Usage

```
$ export ALC_USERNAME='YOUR_ALC_USERNAME'
$ export ALC_PASSWORD='YOUR_ALC_PASSWORD'
$ python eitanjiro.py
```

[0]: https://sites.google.com/a/chromium.org/chromedriver/downloads
