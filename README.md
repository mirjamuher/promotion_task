# promotion_task

This is my solution for Digio's technical interview task

## What does it do?

This code will take a .log file and parse out the IP addresses and URLs. It will then sort these first by occurance, then by name, and print the top x common ones. 

The file path and the top x can be supplied from outside; for this example, the function defaults to supplied global variables. 

## How to run it

### How to set your computer up with Python

1. Download a good IDE (I recommend VSCode)
2. Donwload Python (follow instructions on https://www.python.org/downloads/)
3. Ensure you have all necessary extensions installed in your IDE (e.g. Python in VSCode)

### How to run this program to check the solution

Navigate to `runner.py` and run the file to see the output for the supplied example logs

### How to use this library with your own log file

You can update the `FILE_PATH` with an alternative path to run your logs, or call `main()` with the file path and top_x integer you want to try out

## How to test it

Run helper files like `sorter.py` or `http_request_log_reader.py` and `doctest` will automatically run all tests

## Assumptions

URLS:
1. Full URLs and URL paths are treated equally by my code. To only parse full URLs, update the regex to "GET (https?:\/\/.*?) HTTP". To only parse url paths, update regex to "GET (\/.*?) HTTP". You will have to update the tests accordingly
2. In line with the supplied example file, my code scans for GET requests only. If you want to also scan for other types, you can do so by updating the regex (and tests)

Error Handling:
1. As this is a standalon program and I time-boxed my solution, no error-handling has been implemented. This should be added if this was to be used as a component in a larger project
2. If less than x logs are provided, the program will just return what is there. If that is not-desired behaviour, the code would need fitting amendment

Other improvements:
- add linting and type-checking
- add further type of file readers to `http_request_log_reader` if necessary
- IP addresses are currently not validated, would be a good addition
- doctests can be transformed into unit tests with more time and in a bigger project