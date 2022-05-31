import Custom_Modules.threat_feed_puller_functions as tfpf
from Custom_Modules import script_config
import time

# Used to measure script run time
startTime = time.time()
timestamp = script_config.timestamp


# pull threat feed urls
threat_feeds_lines = open("threat_feeds.txt", "r")
threat_feeds = (threat_feeds_lines.readlines())

# make request to urls to pull content
print("\n==================")
total_ips = []
for feed in threat_feeds:
    feed = feed.strip("\n")
    print(f"Pulling Feed: {feed}")
    feed_content = tfpf.request_feed_content(feed)
    for element in feed_content:
        element = element.strip("\n")
        element = element.strip("\\r")
        element = element.strip("b'")
        # checks if element has a "#" (comment) or if there is an IPv6 address
        comment_check = element.__contains__('#') or element.__contains__(':')
        if comment_check == False:
            total_ips.append(element)

print("\n==================\nMain pull complete")

# get unique IPs
print("Parsing unique IP addresses...")
unique_ips = []
for ip in total_ips:
    if ip not in unique_ips:
        unique_ips.append(ip)

total_ips = len(unique_ips)
total_ips = str(total_ips)
print(f"{total_ips} unique IP addresses parsed.")

print(f"Writing output to {script_config.ip_output_file}")
with open(script_config.ip_output_file, "w") as output_file:    
    for ip in unique_ips:
        output_file.write(f"{ip}\n")
output_file.close()

with open(script_config.logfile, "a") as log_file:
    log_file.write(f"[{timestamp}] {total_ips} addresses pulled\n")
log_file.close()

executionTime = (time.time() - startTime)
executionTime = round(executionTime,2)
executionTime = str(executionTime)
print(f"\n\nDone!\nScript execution time: {executionTime} seconds.\nSaved log at {script_config.logfile}")