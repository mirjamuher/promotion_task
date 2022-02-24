import sorter
import http_request_log_reader
import argparse

def main(file_path, top_N):
    parsed_logs = http_request_log_reader.log_file(file_path)

    # Print the number of unique IP addresses 
    print(f"Number of unique IP addresses is {len(parsed_logs.IP_freq_dict)}")

    # Print the top x active IPs
    sorted_IPs = sorter.by_occurrance_then_name(parsed_logs.IP_freq_dict)
    print(f"The most common IPs are {', '.join(sorted_IPs[0:top_N])}")

    # Print the top x visited URLs
    sorted_URLs = sorter.by_occurrance_then_name(parsed_logs.URL_freq_dict)
    print(f"The most common URLs are {', '.join(sorted_URLs[0:top_N])}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="how many of the top items to print out", default=3, type=int)
    parser.add_argument("-f", help="log file path", default="programming-task-example-data.log", type=str)
    args = parser.parse_args()

    main(args.f, args.n)