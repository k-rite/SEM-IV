import requests
import sys
import logging
logging.basicConfig(level=logging.INFO, filename='DNS_log.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
url = "https://dns-lookup-by-api-ninjas.p.rapidapi.com/v1/dnslookup"
newvalue = {}  # example.com: "certid", certvalue=""
oldvalue = {}
headers = {
    "X-RapidAPI-Key": "27121ea794msh7d3cf3cc8d5ff86p1511ddjsnd0ee0e980351",
    "X-RapidAPI-Host": "dns-lookup-by-api-ninjas.p.rapidapi.com"}
key_record = []
key_value = []
with open("domain.txt", "r") as file:
    domain = file.read().split("\n")
while True:
    for i in domain:
        logging.info(f"Checking domain:{i}")
        querystring = {"domain": i}
        try:
            response = requests.request(
                "GET", url, headers=headers, params=querystring)
            for a in response.json():
                key_record.append(str(a["record_type"]))
                try:
                    key_value.append(str(a["value"]))
                except:
                    key_value.append(str(a))
        except Exception as e:
            logging.warning(f"API conflict found")
            logging.warning(f"{response.json()}")
            logging.warning(f"{e}")
        newvalue[i] = {}
        newvalue[i]["Record_id"] = key_record
        newvalue[i]["Record_value"] = key_value
        if i not in oldvalue.keys():
            oldvalue[i] = {}
            oldvalue[i]["Record_id"] = key_record
            oldvalue[i]["Record_value"] = key_value
            logging.info("Running First time")
        if oldvalue[i]["Record_id"] == newvalue[i]["Record_id"] and oldvalue[i]["Record_value"] == newvalue[i]["Record_value"]:
            logging.info("they're same")
        elif oldvalue[i]["Record_id"] != newvalue[i]["Record_id"] or oldvalue[i]["Record_value"] != newvalue[i]["Record_value"]:
            logging.info("There's a diff")
            for d in newvalue[i]["Record_value"]:
                if d not in oldvalue[i]["Record_value"]:
                    certificate_key = key_record[key_value.index(d)]
            data = {"domain": i, "cert_id": certificate_key,
                    "old_value": oldvalue[i]["Record_value"], "new_value": newvalue[i]["Record_value"]}
            logging.warning(f"API has called, Payload: {data}")
            api_post = requests.post(
                "https://hooks.airtable.com/workflows/v1/genericWebhook/app4yC29zNt3oTOgc/wfl06cDVjkaNzKXL4/wtrDyxH8XexpvTBJJ", data=data)
            logging.warning(f"{api_post.json()}")
        else:
            logging.info("something went wrong")
