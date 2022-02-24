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
    URL_dict = defaultdict(int)
    IP_dict = defaultdict(int)

    with open(file_path) as f:
        for line in f:
            # store urls in table
            url = parse_url(line)
            if url:
                URL_dict[url] += 1

            # store IPs in dictionary
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
    sorted_IPs = items_sorted_by_occurrance_and_name(IP_dict)
    print(f"The three most active IP addresses are... {', '.join(sorted_IPs[0:3])}")

def print_top_3_visited_URLs(urls):
    """
    TEST: url paths are sorted correctly
    >>> print_top_3_visited_URLs({'/example/1': 1, '/example/2/': 2, '/example/3': 1})
    The three most visited URLs are... /example/2/, /example/1, /example/3

    TEST: URLs are sorted first by occurance, then by name
    >>> print_top_3_visited_URLs({'/a/2': 2, '/c/2': 2, '/b/1': 1})
    The three most visited URLs are... /a/2, /c/2, /b/1

    TEST: empty dict doesn't throw an error
    >>> print_top_3_visited_URLs({})
    The three most visited URLs are... 
    
    TEST: dict with one item handled correctly
    >>> print_top_3_visited_URLs({'/example/1': 1})
    The three most visited URLs are... /example/1
    """
    # sort URLS by occurance then string 
    sorted_urls = items_sorted_by_occurrance_and_name(urls)
    print(f"The three most visited URLs are... {', '.join(sorted_urls[0:3])}")

###
# Helper Function
###

def parse_url(line):
    """
    TEST: url paths is prased correctly
    >>> parse_url('177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /example/1 HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n')
    '/example/1'
   
    TEST: full http url is parsed correctly
    >>> parse_url('177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET http://example.net/1/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n')
    'http://example.net/1/'

    TEST: full https url is parsed correctly 
    >>> parse_url('177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET https://example.net/1/ HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Epiphany/2.30.6 Safari/534.7"\\n')
    'https://example.net/1/'

    TEST: string without valid url returns nil
    >>> parse_url("test-string 1234 http: https: url.com")
    

    TEST: empty string returns nil
    >>> parse_url('')
    """
    # to parse out only full urls, use re.compile("GET (https?:\/\/.*?) HTTP")
    # to parse only url paths, use re.compile("GET (\/.*?) HTTP")

    # parse full urls & url paths
    pattern = re.compile("GET (.*?) HTTP")
    result = pattern.search(line)
    if result:
        return result.group(1)
    return

def items_sorted_by_occurrance_and_name(item_dict):
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