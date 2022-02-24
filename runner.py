import sorter
import http_request_log_reader

FILE_PATH = "programming-task-example-data.log"
TOP_X = 3

def main(file_path, top_x):
    parsed_logs = http_request_log_reader.log_file(file_path)

    # Print the number of unique IP addresses 
    print(f"Number of unique IP addresses is {len(parsed_logs.IP_freq_dict)}")

    # Print the top x active IPs
    sorted_IPs = sorter.by_occurrance_then_name(parsed_logs.IP_freq_dict)
    print(f"The most common IPs are {', '.join(sorted_IPs[0:top_x])}")

    # Print the top x visited URLs
    sorted_URLs = sorter.by_occurrance_then_name(parsed_logs.URL_freq_dict)
    print(f"The most common URLs are {', '.join(sorted_URLs[0:top_x])}")

main(FILE_PATH, TOP_X)