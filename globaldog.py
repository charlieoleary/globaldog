#!/usr/bin/env python
import json
import argparse
import os

try:
    from datadog import initialize, api
except ImportError:
    print(
        "The `datadog` module is not installed. Install it with `pip install datadog`."
    )
    exit(1)


def handleErrors(datadogResponse):
    """ returns a list of datadog errors for the user to correct
    """
    if datadogResponse.get("errors"):
        print("One or more errors occurred:")
        for error in datadogResponse.get("errors"):
            print("- %s" % error)
        exit(1)


datadogCredentials = {
    "api_key": os.environ.get("DATADOG_API_KEY"),
    "app_key": os.environ.get("DATADOG_APP_KEY"),
}

initialize(**datadogCredentials)

parser = argparse.ArgumentParser(
    description="A simple script that converts all widgets to use global time."
)

parser.add_argument(
    "-s",
    "--screenboard",
    required=True,
    help="The screenboard ID that you wish to convert.",
)

args = parser.parse_args()

print("Starting conversion of screenboard %s..." % args.screenboard)

screenboard = api.Screenboard.get(args.screenboard)

handleErrors(screenboard)

# iterate over all widgets in the dashboard and set the `time` key to an empty dictionary.
for widget in screenboard["widgets"]:
    if widget.get("time"):
        widget["time"] = {}
        print("+ Updated '%s' widget..." % widget["title_text"])

# append the global time remark to the dashboard title.
screenboard["board_title"] = "{} {}".format(screenboard["board_title"], "(Global Time)")

print("Sending updated screenboard to Datadog...")

update_screenboard = api.Screenboard.update(
    args.screenboard,
    board_title=screenboard["board_title"],
    widgets=screenboard["widgets"],
    template_variables=screenboard["template_variables"],
)

handleErrors(update_screenboard)

print("Your screenboard has been updated! You can view it here:")
print("https://app.datadoghq.com/screen/%s" % args.screenboard)
exit()
