# 🌎🐶globaldog

Ever want to convert an existing Datadog screenboard to use the new global time option? This script
will make it a much easier task.

### Installing

Simply clone the repository, run `pip install -r requirements.txt`, then issue the command below.

## Getting Started

First, visit the [Datadog API page](https://app.datadoghq.com/account/settings#api) and generate or
grab an existing API and application key. Once you have that, you can set the following environment
variables:

```shell
export DATADOG_API_KEY=<YOUR_API_KEY>
export DATADOG_APP_KEY=<YOUR_APP_KEY>
```

Next, open a Datadog screenboard that you wish to use global time with. Take note of the ID in the
URL as shown below. If this is an integration dashboard included with Datadog, you'll need to clone
it, then copy the new ID.

```shell
https://app.datadoghq.com/screen/<SCREENBOARD_ID>/title-of-your-dashboard?page=0&is_auto=false&from_ts=1547592360000&to_ts=1547595960000&live=true
```

Once you have your ID simply run:

```shell
python globaldog.py --screenboard <SCREENBOARD_ID>
```

The script will fetch the board, update all widgets with the `time` key, then push the modified
dashboard back up to your Datadog account.

## Authors

* **Charlie O'Leary** - [charlieoleary](https://github.com/charlieoleary)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
