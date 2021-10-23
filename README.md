# scrapy
The project contains 3 example scrapy projects written in Python that demonstrate 3 concepts.

**Handling single request & response** by extracting a city's weather from a weather site - weather.com

**Handling multiple request & response** by extracting book details from a dummy online book store - books.toscrape.com 

**Image scraping** - imagescraper

**Installing Scrapy**

Scrapy can be installed either through anaconda or pip.

*conda install -c conda-forge scrapy*

or

*pip install Scrapy*

For installing on other OS or any other installation queries, please click here.

To create a new project, you run

*scrapy startproject tutorial*

Spider templates can be created using the below commands

*scrapy genspider [-t template] {name} {domain}*

There are 4 templates available i.e. 4 types of spiders: basic, crawl, csvfeed, xmlfeed. 
The <name> parameter is set as the spider’s name and the <domain> parameter is used to 
generate allowed_domains and start_urls spider attributes. Both these <name> and <domain> parameters are mandatory.

*scrapy genspider -t basic example_basic_spider example.com*
