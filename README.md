
# English - Central Kurdish Sentence Pairs [WIP]

This is a Python project that downloads and processes sentence pairs in English and Central Kurdish (Soranî) from the [Tatoeba](https://tatoeba.org/en/downloads) project. The Tatoeba project is a large database of sentences and translations. This project uses the [pandas](https://pandas.pydata.org/) library to manipulate the data and the [streamlit](https://streamlit.io/) library to create a web app for reviewing the sentence pairs.

## Installation

To install this project, you need to have Python 3.6 or higher and pip installed on your system. You can then clone this repository and install the required dependencies using the following commands:

```bash
git clone https://github.com/abdulbaseet-zahir/eng-ckb-pairs.git
cd eng-ckb-pairs
pip install -r requirements.txt
```

## Usage

To run the web app, you can use the following command:

```bash
streamlit run interface.py
```

This will open a browser window where you can see the sentence pairs and navigate through them using the buttons. You can also filter the sentences by username or search for a specific word or phrase.

To use the Tatoeba class in your own Python scripts, you can import it from the tatoeba module and create an instance of it. For example, you can use the following code to get a pandas dataframe of the sentence pairs:

```python
from tatoeba.tatoeba import Tatoeba

tb = Tatoeba()
data = tb.get_data()
print(data.head())
```

The Tatoeba class has the following methods:

- `bz2url_to_df(url)`: This method takes a URL of a bz2-compressed TSV file from the Tatoeba project and returns a pandas dataframe of its contents.
- `download_eng_ckb_data_from_tatoeba()`: This method downloads the sentence pairs in English and Central Kurdish from the Tatoeba project and saves them as a TSV file in the data folder.
- `get_data(data_path="data", source="eng_ckb_tatoeba")`: This method returns a pandas dataframe of the sentence pairs. It takes two optional parameters: data_path, which is the path to the data folder, and source, which is the name of the data source. The only valid source for now is "eng_ckb_tatoeba".
- `get_data_sources()`: This method returns a list of the available data sources.

## License

This project is in the public domain under the Unlicense license. See the [LICENSE](LICENSE) file for details.

