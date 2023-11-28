### 01. tao thu muc rieng cho project
mkdir scrapy_projects && cd scrapy_projects

### 02. tao moi truong ao cho project
python3 -m venv venv
source venv/bin/activate

### 03. cai dat scrapy
pip install scrapy

### 04. bat dau 1 project voi scrapy
scrapy startproject <project_name>

### 05. di chuyen vao thu muc co file .cfg
cd <project_name>

### 06. tao 1 spider de crawl
scrapy genspider <spider_name> <url_main>

### 07. kiem tra thu voi CLI scrapy
scrapy shell <url_main>

### 08. thuc hien lenh crawl va luu data
scrapy crawl <spider_name> -o <datasets.json>
scrapy crawl fetchnews -o datasets.json

### shutdown robot
=> settings => ROBOTSTXT_OBEY = False

###
Crawled 1780 pages (at 186 pages/min), scraped 1712 items (at 175 items/min)

