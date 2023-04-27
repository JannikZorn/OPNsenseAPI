#!/usr/bin/env python3.7
# for opnsense_api: pip install python-opnsense==1.0.4
# for requests: pip install requests
import requests
import json

import self as self
from opnsense_api import Opnsense
from opnsense_api.util import AliasType

"""
# key + secret from downloaded apikey.txt
api_key = "rr7NnVDAjyWvDOsoQ6tAD7LfuyM6CjdDWvBUimwGopS4ycxMdnIAlCFi3td47GrKCX9Kf9ADWddGf8IU"
api_secret = "rcayD4XHVTVgLHvK/DWeQhxV5iKujsOuvIsG8K30Krz1CL6ZiGv07KtzDWloJmdKdSq8iD+0EL1SExYI"
"""

# Create an instance of the Opnsense class
# reference downloaded cert
opnsense = Opnsense(api_key="rr7NnVDAjyWvDOsoQ6tAD7LfuyM6CjdDWvBUimwGopS4ycxMdnIAlCFi3td47GrKCX9Kf9ADWddGf8IU",
                    api_secret="rcayD4XHVTVgLHvK/DWeQhxV5iKujsOuvIsG8K30Krz1CL6ZiGv07KtzDWloJmdKdSq8iD+0EL1SExYI",
                    host="10.250.7.122",
                    ca_path="C:\\Users\\zorn\\PycharmProjects\\CTB_JF_OPNsense\\cert\\Web+GUI+TLS+certificate.crt")

# Get the alias controller
alias = opnsense.firewall.alias_controller
# define the basics, hostname to use and description used to identify our test rule
rule_description = 'OPNsense_fw_api_testrule_1'



# The values for the example alias
example_alias_name = "test_alias"
example_alias_description = "This is the description for test_alias"
example_alias_type = AliasType.PORT


# Add a new alias to the Opnsense device
# This will return an object that represents the new alias.
print("ADD ALIAS")
add_output = alias.add(name=example_alias_name, description=example_alias_description, alias_type=example_alias_type)
print(json.dumps(add_output))




# Get the filter controller
# filter = opnsense.firewall.filter_controller
# filter_rule = filter.match_rule_by_attributes({"description": rule_description})

"""
remote_uri = "https://10.250.7.122"

# search for rule
r = requests.get("%s/api/firewall/filter/searchRule?current=1&rowCount=7&searchPhrase=%s" % (remote_uri, rule_description), auth=(api_key, api_secret))


if r.status_code == 200:
    response = json.loads(r.text)
    if len(response['rows']) > 0:
        rule_uuid = response['rows'][0]['uuid']
        r = requests.post("%s/api/firewall/filter/savepoint" % remote_uri, auth=(api_key, api_secret))
        if r.status_code == 200:
            sp_response = json.loads(r.text)
            # disable rule
            r = requests.post("%s/api/firewall/filter/toggleRule/%s/0" % (remote_uri, rule_uuid),
                              auth=(api_key, api_secret)
            )
            # apply changes, revert to sp_response['revision'] after 60 seconds
            r = requests.post("%s/api/firewall/filter/apply/%s" % (remote_uri, sp_response['revision']),
                              auth=(api_key, api_secret)
            )
            print("revert to revision %s in 60 seconds (%s changed)" % (sp_response['revision'], rule_uuid))
    else:
        print("rule %s not found" % rule_description)
"""
