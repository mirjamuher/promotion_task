# promotion_task

This is my solution for Digio's technical interview task

## What does it do?

This code will take a .log file and parse out the IP addresses and URLs. It will then sort these first by occurance, then by name, and print the top N common ones.

## How to run it

### How to set your computer up with Python

I recommend following this tutorial on how to install VS Code and set your computer up for Python: https://code.visualstudio.com/docs/python/python-tutorial

### How to run this program to check the solution for the technical interview task

Navigate to `runner.py` and run the file 
OR run `$ python3 runner.py` to see the output for the supplied example logs
OR run `$ python3 runner.py -f [log_file_path] -n [top_n]`

### How to use this library with your own log file

You can call `main()` from your program with the file path and top_N integer.

## How to test it

Run helper files like `sorter.py` or `http_request_log_reader.py` and `doctest` will automatically run all tests.

## Assumptions

URLS:
1. Full URLs and URL paths are treated equally by my code. To only parse full URLs, update the regex to `\"[A-Z]+ (https?:\/\/.*?) HTTP`. To only parse url paths, update regex to `\"[A-Z]+ (\/.*?) HTTP`. You will have to update the tests accordingly

Error Handling:
1. As this is a standalon program and I time-boxed my solution, no error-handling has been implemented. This should be added if this was to be used as a component in a larger project
2. If less than N valid log lines are provided, the program will just return what is there. If that is not-desired behaviour, the code would need fitting amendment

`main()`:
To easily show the code working for the questions posed in the technical interview, `main()` currently prints the answers to the three posed questions. If this library was to be used as a component in a bigger project, it would be sensible to change `main()` to just return the `ParsedLogs` object, and add methods to it (such as checking the length of all IP addresses, or the top N URLs)

Other recommended improvements:
- add linting and type-checking
- add further type of file readers to `http_request_log_reader` if necessary
- IP addresses are currently not validated, would be a good addition
- doctests can be transformed into unit tests with more time and in a bigger project