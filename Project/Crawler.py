__author__ = 'Raphael'

def getLink(page):
    """
    Soumaya and Frank
    function takes in a html  string and returns first link
    :param page: html string
    :return: first link
    """
    return page


def get_all_links(page):
    """


    :rtype : list of all links in a page
    :param page: html content of the page
    """
    return page


def get_page(url):
    """
    Hassane and Tolu
    :rtype : html conten of paget
    :param url of page to return:
    """
    return url

def crawl_web(seed):
    """


    :rtype : a a list of crawled pagest
    :param seed: the starting linkk for crawling
    """
    to_crawl = [seed]
    crawled = []
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            to_crawl.union(get_all_links(get_page(page)))
            crawled.append(page)

    return crawled