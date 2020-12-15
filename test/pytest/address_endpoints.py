import unittest
import configparser
from pybgl import *
import requests
import zlib
from pprint import pprint
import psycopg2
config_file =   "../config/bglapi-server.conf"
config = configparser.ConfigParser()
config.read(config_file)

postgres_dsn = config["POSTGRESQL"]["dsn"]
option_transaction = True if config["OPTIONS"]["transaction"] == "on" else False
option_merkle_proof = True if config["OPTIONS"]["merkle_proof"] == "on" else False
option_address_state = True if config["OPTIONS"]["address_state"] == "on" else False
option_address_timeline = True if config["OPTIONS"]["address_timeline"] == "on" else False
option_blockchain_analytica = True if config["OPTIONS"]["blockchain_analytica"] == "on" else False
option_transaction_history = True if config["OPTIONS"]["transaction_history"] == "on" else False
base_url = config["SERVER"]["api_endpoint_test_base_url"]

class AddressAPIEndpointsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nTesting Address API endpoints:\n")

    def test_address_state(self):
        print("/rest/address/state/{address}:\n")

        r = requests.get(base_url + "/rest/address/state/bgl1qs6pce5xnxa58pthahz977m2hxpxyehthd2ax7r")
        self.assertEqual(r.status_code, 200)
        d_1 = r.json()["data"]
        pprint(d_1)
        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/address/state/bgl1qs6pce5xnxa58pthahz977m2hxpxyehthd2ax7r")
        d = r.json()["data"]
        self.assertEqual(d_1["balance"]["confirmed"], d["receivedAmount"] - d["sentAmount"])
        print("OK\n")


    def test_get_address_by_list(self):
        print("/rest/addresses/state/by/address/list:\n")
        r = requests.post(base_url + "/rest/addresses/state/by/address/list",
                          json=["bgl1qs6pce5xnxa58pthahz977m2hxpxyehthd2ax7r",
                                "bgl1qshphrzd0ahu9u36e654ypd5yzjgr78m5lzytsq"])
        self.assertEqual(r.status_code, 200)
        pprint(r.json())
        print("OK\n")


    def test_get_address_utxo(self):
        print("/rest/address/utxo/{address}:\n")

        r = requests.get(base_url + "/rest/address/utxo/bgl1qs6pce5xnxa58pthahz977m2hxpxyehthd2ax7r")
        self.assertEqual(r.status_code, 200)
        d_1 = r.json()["data"]
        # pprint(d_1)
        a = 0
        for k in d_1:
            a += k["amount"]

        r = requests.get(base_url + "/rest/address/state/bgl1qs6pce5xnxa58pthahz977m2hxpxyehthd2ax7r")
        self.assertEqual(r.status_code, 200)
        d_1 = r.json()["data"]
        self.assertEqual(a, d_1["balance"]["confirmed"])

        print("OK\n")
