# Article Extraction and Analysis
This repository contains code for extracting and analyzing articles using both the Newspaper library and a custom web scraper. The project leverages natural language processing to summarize and analyze articles from various websites.

## Documentation
For reference:  
[Click here](https://towardsdatascience.com/scrape-and-summarize-news-articles-in-5-lines-of-python-code-175f0e5c7dfc?gi=9e8922afc18b)

## In simple terms:

### How it Works
The project employs two methods for extracting article content: the Newspaper library and a custom web scraper. The extracted content includes the title, publication date, summary, image URLs, video URLs, and the source URL.

## Usage
**Extracting Articles:**  
Users can extract articles by running the provided script. The script performs a Google search for a specified term, extracts articles using both methods, and prints the extracted information.

## Screenshots
## Example output of extracted article details.
![Example Output](https://github.com/RupankarGarai2003/Article-Finder/blob/main/images/article.jpg)
![Example Output](https://github.com/RupankarGarai2003/Article-Finder/blob/main/images/article_2.jpg)
                        

## Installation
To import the libraries:
- import requests
- from bs4 import BeautifulSoup
- from googlesearch import search
- import newspaper
- from newspaper import Article
- import nltk
- from datetime import datetime
- import re

Installation method for the libraries are:

- To install the proper version that I have installed, use the `requirements.txt` file to make it easy for you to install the same.

```bash
pip install -r requirements.txt
```

Or install the required packages individually:
```bash
pip install requests beautifulsoup4 google newspaper3k nltk
```

- Or you can just git clone the code but please change the path files according to your local machine:
```bash
git clone https://github.com/Sayan-Maity-Code/article_finder
```

- Install with npm:
```bash
npm install git+https://github.com/Sayan-Maity-Code/article_finder
```

## Contributing
Contributions are always welcome!

See `README.md` for ways to get started.

Please adhere to this project's contribution guidelines. During your interaction with the project, make sure to maintain respectful communication, collaborate positively with other contributors (if applicable), and follow any contribution guidelines provided by the project maintainers. If you encounter any issues or have questions, consider reaching out to the project maintainers for guidance.

## Developers interested in contributing to the project can follow these steps:
- Fork the repository.
- Clone the forked repository to your local machine.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request to the main repository.

## Known Issues
- **Parsing Errors:** The custom scraper may encounter parsing errors on websites with complex or dynamic content.
- **Date Extraction:** Date extraction may fail for non-standard date formats.

## Future Update
We are continuously working to improve the article extraction and analysis project. Future updates may include enhancements to the extraction methods, optimization of data processing, and integration of additional analysis features.

## Contact
For any questions, feedback, or suggestions, please contact [rupankargarai55@gmail.com].
