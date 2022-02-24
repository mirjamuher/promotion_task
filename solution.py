from collections import defaultdict
import re

###
# Task
###
def main(file_path):
    urls, IP_dict = read_file(file_path)
    print_no_of_unique_IP_addresses(IP_dict)
    print_top_3_IP_addresses(IP_dict)
    print_top_3_visited_URLs(urls)

###
# Main Functions
###

def read_file(file_path):
    logs = []
    IP_dict = defaultdict(int)

    with open(file_path) as f:
        for line in f:
            logs.append(line)
            ip = line.split()[0]
            IP_dict[ip] += 1
    
    return URL_dict, IP_dict

def print_no_of_unique_IP_addresses(IP_dict):
    """
    TEST: one entry with one occurance is counted correctly 
    >>> print_no_of_unique_IP_addresses({"155.55.555.55": 1})
    The number of unique IP addresses is... 1

    TEST: multiple entries with one occurance are counted correctly
    >>> print_no_of_unique_IP_addresses({"155.55.555.55": 1, "255.55.555.55": 1, "355.55.555.55": 1})
    The number of unique IP addresses is... 3

    TEST: multiple entries with multiple occurances are counted correctly
    >>> print_no_of_unique_IP_addresses({"555.55.555.55": 20, "255.55.555.55": 10})
    The number of unique IP addresses is... 2

    TET: empty dictionary is counted correctly
    >>> print_no_of_unique_IP_addresses({})
    The number of unique IP addresses is... 0
    """
    print(f"The number of unique IP addresses is... {len(IP_dict)}")

def print_top_3_IP_addresses(IP_dict):
    """
    TEST: IP addresses are sorted decendingly by occurance
    >>> print_top_3_IP_addresses({'177.71.128.21': 3, '168.41.191.40': 4, '168.41.191.9': 2, '168.41.191.34': 1})
    The three most active IP addresses are... 168.41.191.40, 177.71.128.21, 168.41.191.9
    
    TEST: IP addresses are sorted decendingly by occurance, then by name
    >>> print_top_3_IP_addresses({'177.71.128.21': 3, '168.41.191.40': 3, '168.41.191.9': 3}) 
    The three most active IP addresses are... 168.41.191.40, 168.41.191.9, 177.71.128.21

    TEST: empty dictionary does not throw error
    >>> print_top_3_IP_addresses({})
    The three most active IP addresses are... 

    TEST: one entry in dictionary is counted correctly 
    >>> print_top_3_IP_addresses({'177.71.128.21': 3})
    The three most active IP addresses are... 177.71.128.21
    """
    sorted_IPs = items_sorted_by_occurrance_and_address(IP_dict)
    print(f"The three most active IP addresses are... {', '.join(sorted_IPs[0:3])}")

def print_top_3_visited_URLs(logs):
    """
    TEST: url paths are parsed & sorted correctly
    >>> print_top_3_visited_URLs([
    ... '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /example/1 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:11:30 +0200] "GET /example/2/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.41 - - [11/Jul/2018:17:41:30 +0200] "GET /example/2/ HTTP/1.1" 404 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:10:38 +0200] "GET /example/3 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"\\n'
    ... ])
    The three most visited URLs are... /example/2/, /example/1, /example/3
   
    TEST: full urls are parsed & sorted correctly
    >>> print_top_3_visited_URLs([
    ... '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET http://example.net/1/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:11:30 +0200] "GET http://example.net/2/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.41 - - [11/Jul/2018:17:41:30 +0200] "GET http://example.net/2/ HTTP/1.1" 404 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:10:38 +0200] "GET http://example.net/3 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"\\n'
    ... ])
    The three most visited URLs are... http://example.net/2/, http://example.net/1/, http://example.net/3
    
    TEST: mixed logs of full urls and url paths are parsed & sorted equally
    >>> print_top_3_visited_URLs([
    ... '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET http://example.net/1/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:11:30 +0200] "GET /example/2/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.41 - - [11/Jul/2018:17:41:30 +0200] "GET /example/2/ HTTP/1.1" 404 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:10:38 +0200] "GET http://example.net/3 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"\\n'
    ... ])
    The three most visited URLs are... /example/2/, http://example.net/1/, http://example.net/3

    TEST: URLs are sorted first by occurance, then by name
    >>> print_top_3_visited_URLs([
    ... '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /a/2 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n',
    ... '168.41.191.40 - - [09/Jul/2018:10:11:30 +0200] "GET /a/2 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.41 - - [11/Jul/2018:17:41:30 +0200] "GET /c/2 HTTP/1.1" 404 3574 "-" "Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"\\n',
    ... '168.41.191.43 - - [09/Jul/2018:10:10:38 +0200] "GET /c/2 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"\\n',
    ... '168.41.191.45 - - [09/Jul/2018:10:10:38 +0200] "GET /b/1 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24"\\n'
    ... ])
    The three most visited URLs are... /a/2, /c/2, /b/1

    TEST: empty URls dict doesn't throw an error
    >>> print_top_3_visited_URLs([])
    The three most visited URLs are... 
    
    TEST: dict with one item handled correctly
    >>> print_top_3_visited_URLs([
    ... '177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /example/1 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n',
    ... ])
    The three most visited URLs are... /example/1
    """
    # to parse out only full urls, use re.compile("GET (https??:\/\/.*?) HTTP")
    # to parse only url paths, use re.compile("GET (\/.*?) HTTP")

     # parse URLS by pattern
    pattern = re.compile("GET (.*?) HTTP")
    URLs = defaultdict(int)

    for log in logs:
        result = pattern.search(log)
        if result:
            URLs[result.group(1)] += 1

    # sort URLS by occurance then string 
    sorted_urls = items_sorted_by_occurrance_and_address(URLs)
    print(f"The three most visited URLs are... {', '.join(sorted_urls[0:3])}")

###
# Helper Function
###

def items_sorted_by_occurrance_and_address(item_dict):
    # short version: sorted_items = [k for k, _ in sorted(item_dict.items(), key = lambda item: (-item[1], item[0]))]
    def sort_by_occurrance_and_name(item):
        return ((-item[1], item[0])) 
    full_sorted_list = sorted(item_dict.items(), key = sort_by_occurrance_and_name)
    sorted_items = [k for k, _ in full_sorted_list]
    return sorted_items

###
# TESTING
###
if __name__ == "__main__":
    import doctest
    doctest.testmod()