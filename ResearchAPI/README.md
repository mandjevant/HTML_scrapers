ResearchAPI scrapes from https://ieeexplore.ieee.org

Currently you can only use the scraper from editing the sh.py file. This is because the scrapers were originally made for a bigger project.
If help making different accessing method is desired, I invite you to open an issue.

Functions of this scraper include;
- Research; The user is asked to input the word or sentence to be research and the number of searches. This function returns the url, title and abstract of the desired amount of searches.

Prerequisites;
- requests (pip install requests)
- bs4 (pip install beautifulsoup4)
- selenium (pip install selenium)
- GoogleDriver (included in Applications folder)
