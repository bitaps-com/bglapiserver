import requests
from pybgl import *


def test_address_state_basic(conf):
    r = requests.get(conf["base_url"] + "/rest/address/state/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/address/state/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y")
    d = r.json()["data"]
    if  conf["option_transaction_history"]:
        assert d_1["receivedAmount"] == d["receivedAmount"]
        assert d_1["sentAmount"] == d["sentAmount"]
    else:
        assert d_1["confirmed"] == d["receivedAmount"] - d["sentAmount"]


def test_get_address_by_list_basic(conf):
    r = requests.post(conf["base_url"] + "/rest/addresses/state/by/address/list",
                      json=["bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y"])
    assert r.status_code == 200
    dl = r.json()["data"]

    r = requests.get(conf["base_url"] + "/rest/address/state/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    if  conf["option_transaction_history"]:
        assert dl["bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y"]["confirmed"] == d_1["receivedAmount"] - d_1["sentAmount"]
    else:
        assert dl["bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y"]["confirmed"] == d_1["confirmed"]



def test_get_address_utxo(conf):
    r = requests.get(conf["base_url"] + "/rest/address/utxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    a = 0
    for k in d_1:
        a += k["amount"]
    assert a  > 6830321573

    r = requests.get(conf["base_url"] + "/rest/address/utxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=2")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    assert len(d_1) == 2
    r = requests.get(conf["base_url"] + "/rest/address/utxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=0")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    assert len(d_1) > 10

    r = requests.get(conf["base_url"] + "/rest/address/utxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=1&order=asc")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    assert d_1[0]["block"] == 0


    r = requests.get(conf["base_url"] + "/rest/address/utxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?from_block=32897")
    assert r.status_code == 200
    d_1 = r.json()["data"]
    assert d_1[0]["block"]  == 32897



    r = requests.get(conf["base_url"] + "/rest/address/uutxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y")
    assert r.status_code == 200

    r = requests.get(conf["base_url"] + "/rest/address/uutxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=2")
    assert r.status_code == 200

    r = requests.get(conf["base_url"] + "/rest/address/uutxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=0")
    assert r.status_code == 200


    r = requests.get(conf["base_url"] + "/rest/address/uutxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=1&order=dsc")
    assert r.status_code == 200

    r = requests.get(conf["base_url"] + "/rest/address/uutxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?limit=1&order=asc")
    assert r.status_code == 200

    r = requests.get(conf["base_url"] + "/rest/address/uutxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y?"
                                        "order_by_amount=1&order=dsc")
    assert r.status_code == 200
