# Website checker script

If you have some websites and want to check them in a routine, which one is online, you could use this script:

```bash
pipenv install
pipenv shell
python checker.py
```

You should put the list of website name `googl.com` in a file named `website_list.txt` besides `checker.py` file.

```text
google.com
github.com
```

The script creates a log file `website_statu.log` and you could add your timezone to see the `website_statu.log` in your timezone:

```python
log_tz = pytz.timezone('Asia/Tehran')
```

You could define a cronjob to run it daily in specific time (e.g. 9:50 am)

```cron
50 9 * * * /path-to-pipnv/bin/python3 /path/to/script/check_websites.py >> ~/logs/website_status.log 2>&1
```
