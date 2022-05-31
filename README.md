# Simple Threat Intelligence Feed Puller

## About
This script is a simple and easy way to pull some free and open-source threat intel feeds.

This script will just output a simple .txt with the data that you can use as the need fits.

At this moment it just pulls IPv4 data, and uses 6 free and open-source threat feeds, you can add more or remove the URLs as needed.

## Requirements
* Python 3.10.X+
* Requests Library
* threat_feed_puller_functions.py & script_config.py; Comes with this repo.

You can also run:
    `pip install -r requirements.txt`

## Usage
* Make sure you have the requirements installed
* Add or remove URLs from `threat_feeds.txt`
  * One URL per line
* Run:
  * On Windows - `python.exe .\simple_threat_intel_feed_puller.py`
  * On *nix - `python3 ./simple_threat_intel_feed_puller.py`

## Config
There is a config file located at `Custom_Modules\script_config.py` where you can change some of the variables as needed.
### Output File Paths
* Default - Relative to main script
* If you do set this up as a Cronjob or a Scheduled Task
    * This is recommended to change the output file paths to exact file paths, or you can just `cd` into the script directory from the cronjob\scheduled task.
### Time Stamp Date Format
* Default - UTC ISO 8601
* You can change the log time stamp format to what ever is wanted.


## Feedback
* Any type of feedback is encouraged, please send me an [Email](mailto:angel.alvarez@alva.systems) or DM me on [Twitter](https://twitter.com/aztekxyz)