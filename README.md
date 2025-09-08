# Create Pydantic Class Definitions from JSON or YAML

## Usage

1. Install dependencies

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Modify `input.json` with you own JSON data

3. Run the script

```shell
python3 main.py
```

4. Output will be printed to console as well as written to a file called `output.py`

5. After it outputs the code, you can test it out with

```shell
python3 output.py
```

6. (Optional): To use with YAML, simply uncomment the relevant lines in the script.
