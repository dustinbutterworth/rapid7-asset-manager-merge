# rapid7-asset-manager-merge

I've been having an issue where Rapid7 doesn't match the DNS names our internal DNS server
gives our hostnames and the csv's I generate typically will have the default AWS DNS name.

For example, I might see this in my report:
```
ip-10-0-0-0.ec2.internal
```
But what I want to see is my internal DNS name for this, something like:
```
host.example.com
```

I already have an internal asset management system I can use to see that information matched to the
IP address as well as various tags that we've added for each asset, too.  

How nifty would it be if I could merge the rapid7 csv export of all assets affected by a vulnerability
with a csv generatedy by my asset management tool so I could correlate the data and give out reports
or use to upload to tickets and such?  Well, I managed to do just that with pandas in python.

## Getting Started

First, you'll need python 3.7
As of the creatin of this document I'm using Python 3.7.3.

### Prerequisites

You'll need to pip install pandas.

```
pip install pandas
```

Next I export the csv from Rapid7, save it to your local directory.

Then I provide the url to my asset management tool's csv of all assets. I have this generated periodically
with a cron job and served up on a webserver, so I used pandas read_csv to grab it remotely, but you can 
just put it locally with some minor changes if you wanted to.

You also will need to choose what headers you want to keep from both csvs for the new csv that will be
generated.  For instance, I use the following:
```
header = ['Asset','Name_y','Proof', 'Lifecycle', 'Platform', 'Purpose', 'Contact']
```
Customize this to your liking. 

I also choose to sort my assets by Lifecycle. This is how I prefer to look at the report, you can customize
this to your liking as well by tweaking this:
```
sorted_df = merge_df.sort_values(by="Lifecycle")
```

### Running

Once you have those ready, just add your vars to rapid7-asset-manager-merge.py and run it.

```
python rapid7-asset-manager-merge.py
```

new.csv will be generated in the working directory.

## Authors

* **Dustin Butterworth**



