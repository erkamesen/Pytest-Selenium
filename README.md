##

*Test for: https://demowebshop.tricentis.com/*


## Install & Usage:

- *Clone the repository:*
```
git clone https://github.com/erkamesen/Pytest-Selenium.git
```

- *Change Directory*
```
cd Pytest-Selenium/
```

- *Set virtual environment and install dependencies*
```
python3 -m venv venv
```

```
pip3 install -r requirements.txt
```

- *Simple test example*
```
pytest
```

#### *Optionals*
- Browser choice:
```
pytest --browser <chrome> & <firefox>
```
- Headless mode:
```
pytest --headless 
```

- env choice:
```
pytest --env <dev> <qa> <test> <prod> 
```

| *After the tests run, you can get the report as HTML in reports/ folder*
