# Columbia College Chicago Scraper

Columbia College Chicago EngageColumbia scraper is a student directory scraper which scrapes information for all students within the college's directory. Disclaimer: I am not responsible for the use of the code in this repository by third-party memebers. I have discussed with faculty at the institution about the contents in this repository. This project was for educational purposes. I encourage to not use this code for bad.

## Getting Started

### Requirements

To run the program, you will first need to create virtual enviornment:

```console
$ python3 -m venv venv
```

### Install requirements:

```console
$ pip install -r requirements.txt
```

NOTE: Before your run the scraper, navigative to `locals.py` and add your own email and password to `EMAIL` and `PASSWORD`.

```python
# locals.py
EMAIL = "username@colum.edu"
PASSWORD = "password"
```

### Running the scraper

To run the scraper, simply:

```console
$ python3 scraper.py
```

### Running tests

```console
$ pytest
```
