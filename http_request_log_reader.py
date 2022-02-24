from collections import defaultdict
import re

class Parsed_Logs:
    def __init__(self, URL_freq_dict, IP_freq_dict):
        self.URL_freq_dict = URL_freq_dict
        self.IP_freq_dict = IP_freq_dict

def txt_file(file_path):
    URL_freq_dict = defaultdict(int)
    IP_freq_dict = defaultdict(int)

    with open(file_path) as f:
        for line in f:
            # store urls in table
            url = parse_url(line)
            if url:
                URL_freq_dict[url] += 1

            # store IPs in dictionary
            ip = parse_IP_address(line)
            IP_freq_dict[ip] += 1
    
    return Parsed_Logs(URL_freq_dict, IP_freq_dict)

def parse_IP_address(line):
    return line.split()[0]

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
    return None

###
# TESTING
###
if __name__ == "__main__":
    import doctest
    doctest.testmod()