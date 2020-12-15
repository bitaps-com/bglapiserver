import requests
from pybgl import *



"""
address transactions records

stxo

"""

import requests
from pybgl import *


def test_get_transaction_extended(conf):
    if not conf["option_transaction_history"]:
        return

    r = requests.get(conf["base_url"] +
                     "/rest/transaction/8b162e5db25da4b506e8c96c16f16d9ed106c143502fd20a10e5230ca30939cb")
    assert r.status_code == 200
    d_1 = r.json()["data"]


    r = requests.get(conf["base_url"] + "/rest/transaction/37230:1")
    assert r.status_code == 200
    d_2 = r.json()["data"]

    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/"
                     "8b162e5db25da4b506e8c96c16f16d9ed106c143502fd20a10e5230ca30939cb")
    assert r.status_code == 200
    t = r.json()["data"]


    for d in [d_1, d_2]:
        assert t["txId"] == d["txId"]
        assert t["hash"] == d["hash"]
        assert t["version"] == d["version"]
        assert t["size"] == d["size"]
        assert t["vSize"] == d["vSize"]
        assert t["bSize"] == d["bSize"]
        assert t["lockTime"] == d["lockTime"]
        assert t["weight"] == d["weight"]
        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]
        assert t["segwit"] == d["segwit"]
        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
            assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
            assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
            assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
            assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
            assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
            if "address" in t["vIn"][i]:
                assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]
    r = requests.get(conf["base_url"] + "/rest/transaction/37230:55555")
    assert r.status_code == 404
    r = requests.get(conf["base_url"] + "/rest/transaction/372305555")
    assert r.status_code == 400


def test_get_coinbase_transaction_extended(conf):
    if not conf["option_transaction_history"]:
        return

    r = requests.get(conf["base_url"] +
                     "/rest/transaction/ce0139174e95e72a0be50b8d02ff9e3145e0289538117b1209174043f0a4c1b9")
    assert r.status_code == 200
    d_1 = r.json()["data"]


    r = requests.get(conf["base_url"] + "/rest/transaction/37230:0")
    assert r.status_code == 200
    d_2 = r.json()["data"]

    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/"
                     "ce0139174e95e72a0be50b8d02ff9e3145e0289538117b1209174043f0a4c1b9")
    assert r.status_code == 200
    t = r.json()["data"]


    for d in [d_1, d_2]:
        assert t["txId"] == d["txId"]
        # assert t["hash"] == d["hash"]
        assert t["version"] == d["version"]
        # assert t["size"] == d["size"]
        # assert t["vSize"] == d["vSize"]
        # assert t["bSize"] == d["bSize"]
        assert t["lockTime"] == d["lockTime"]
        # assert t["weight"] == d["weight"]
        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]
        # assert t["segwit"] == d["segwit"]
        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]
    r = requests.get(conf["base_url"] + "/rest/transaction/621860:55555")
    assert r.status_code == 404
    r = requests.get(conf["base_url"] + "/rest/transaction/6218605555")
    assert r.status_code == 400



def test_get_transaction_extended_list(conf):
    if not conf["option_transaction_history"]:
        return
    l = ["8b162e5db25da4b506e8c96c16f16d9ed106c143502fd20a10e5230ca30939cb",
         "ce0139174e95e72a0be50b8d02ff9e3145e0289538117b1209174043f0a4c1b9"]
    for h in l:
        r = requests.get(conf["base_url"] + "/rest/transaction/" + h)
        assert r.status_code == 200
        d = r.json()["data"]


        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" + h )
        assert r.status_code == 200
        t = r.json()["data"]

        assert t["txId"] == d["txId"]
        if not t["coinbase"]:
            assert t["hash"] == d["hash"]
            assert t["size"] == d["size"]
            assert t["vSize"] == d["vSize"]
            assert t["bSize"] == d["bSize"]
            assert t["weight"] == d["weight"]
            assert t["segwit"] == d["segwit"]
        assert t["version"] == d["version"]

        assert t["lockTime"] == d["lockTime"]

        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]

        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            if t["coinbase"]:
                continue
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
            assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
            assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
            assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
            if t["vIn"][i]["blockHeight"] != -1:
                assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
                assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
            if "address" in t["vIn"][i]:
                assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]





def test_get_unconfirmed_transaction_extended(conf):
    if not conf["option_transaction_history"]:
        return

    r = requests.get("https://api.bitaps.com/bgl/v1/mempool/transactions")
    assert r.status_code == 200
    t = r.json()["data"]["transactions"]
    tx_list = [i["txId"] for i in t]
    counter = 0
    for tx in tx_list:
        time.sleep(0.4)

        r = requests.get(conf["base_url"] +
                         "/rest/transaction/" + tx)
        if r.status_code == 404:
            continue
        counter += 1
        assert r.status_code == 200
        d = r.json()["data"]

        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" + tx)
        assert r.status_code == 200
        t = r.json()["data"]

        assert t["txId"] == d["txId"]
        assert t["hash"] == d["hash"]
        assert t["version"] == d["version"]
        assert t["size"] == d["size"]
        assert t["vSize"] == d["vSize"]
        assert t["bSize"] == d["bSize"]
        assert t["lockTime"] == d["lockTime"]
        assert t["weight"] == d["weight"]
        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]
        assert t["segwit"] == d["segwit"]
        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
            assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
            assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
            assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
            if t["vIn"][i]["blockHeight"] != -1:
                assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
                assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
            if "address" in t["vIn"][i]:
                assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]
    assert counter > 0

def test_get_transaction_by_pointer_list_extended(conf):
    if not conf["option_transaction_history"]:
        return

    tl = ["8b162e5db25da4b506e8c96c16f16d9ed106c143502fd20a10e5230ca30939cb",
          "ce0139174e95e72a0be50b8d02ff9e3145e0289538117b1209174043f0a4c1b9"]

    r = requests.post(conf["base_url"] + "/rest/transactions/by/pointer/list",
                      data= json.dumps(tl).encode())
    assert r.status_code == 200
    dl = r.json()["data"]

    for tx in tl:
        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/"+tx)
        assert r.status_code == 200
        t = r.json()["data"]

        for d in [dl[t["txId"]]]:
            assert t["txId"] == d["txId"]
            assert t["hash"] == d["hash"]
            assert t["version"] == d["version"]
            assert t["size"] == d["size"]
            assert t["vSize"] == d["vSize"]
            assert t["bSize"] == d["bSize"]
            assert t["lockTime"] == d["lockTime"]
            assert t["weight"] == d["weight"]
            assert t["data"] == d["data"]
            assert t["coinbase"] == d["coinbase"]
            assert t["segwit"] == d["segwit"]
            assert t["amount"] == d["amount"]
            for i in t["vIn"]:
                assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
                assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
                assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
                assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
                assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
                assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
                assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
                assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
                assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
                if "address" in t["vIn"][i]:
                    assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
                assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
                assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
                if "txInWitness" in t["vIn"][i]:
                    assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
                if not t["coinbase"]:
                    assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                    assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
            for i in t["vOut"]:
                assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
                assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
                assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
                assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
                if "addressHash" in t["vOut"][i]:
                    assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                    assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
                assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
                assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
                assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]

def test_get_unconfirmed_transaction_by_pointer_list_extended(conf):
    if not conf["option_transaction_history"]:
        return
    tms = int(time.time())
    r = requests.get("https://api.bitaps.com/bgl/v1/mempool/transactions")
    assert r.status_code == 200
    t = r.json()["data"]["transactions"]
    tx_list = [i["txId"] for i in t]


    q = time.time()
    r = requests.post(conf["base_url"] + "/rest/transactions/by/pointer/list",
                      data= json.dumps(tx_list).encode())
    assert r.status_code == 200
    dl = r.json()["data"]
    assert time.time() - q < 1


    counter = 0
    for tx in tx_list:
        time.sleep(0.35)
        d = dl[tx]

        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" + tx)
        assert r.status_code == 200
        t = r.json()["data"]
        if d is None:
            continue
        counter += 1
        assert t["txId"] == d["txId"]
        assert t["hash"] == d["hash"]
        assert t["version"] == d["version"]
        assert t["size"] == d["size"]
        assert t["vSize"] == d["vSize"]
        assert t["bSize"] == d["bSize"]
        assert t["lockTime"] == d["lockTime"]
        assert t["weight"] == d["weight"]
        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]
        assert t["segwit"] == d["segwit"]
        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
            assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
            assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
            assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
            if t["vIn"][i]["blockHeight"] != -1:
                assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
                assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
            if "address" in t["vIn"][i]:
                assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]

            if t["vOut"][i]["spent"] != d["vOut"][str(i)]["spent"]:
                r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" +
                                 t["vOut"][i]["spent"][0]["txId"])
                assert r.status_code == 200
                st = r.json()["data"]
                if not ((st["time"] - tms >= 0) or (st["time"] - t["time"])):
                    assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]

    assert counter > 0

def test_get_confirmed_transaction_by_pointer_list_extended(conf):
    if not conf["option_transaction_history"]:
        return

    r = requests.get("https://api.bitaps.com/bgl/v1/mempool/transactions")
    assert r.status_code == 200
    t = r.json()["data"]["transactions"]
    tx_list = [i["txId"] for i in t][:30]


    q = time.time()
    r = requests.post(conf["base_url"] + "/rest/transactions/by/pointer/list",
                      data= json.dumps(tx_list).encode())
    assert r.status_code == 200
    dl = r.json()["data"]
    assert time.time() - q < 2
    tx_conf = []

    counter = 0
    for tx in tx_list:
        d = dl[tx]
        if d is None:
            continue
        for i in d["vIn"]:
            if d["vIn"][i]["blockHeight"] is not None:
                tx_conf.append(d["vIn"][i]["txId"])

    q = time.time()
    tx_conf = tx_conf[:80]
    r = requests.post(conf["base_url"] + "/rest/transactions/by/pointer/list",
                      data= json.dumps(tx_conf).encode())
    tms = int(time.time())
    assert r.status_code == 200
    dl = r.json()["data"]
    assert time.time() - q < 2
    counter = 0


    for tx in tx_conf:

        time.sleep(0.4)

        d = dl[tx]

        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" + tx)
        assert r.status_code == 200
        t = r.json()["data"]
        if d is None:
            continue
        counter += 1
        assert t["txId"] == d["txId"]

        assert t["version"] == d["version"]
        if not t["coinbase"]:
            assert t["hash"] == d["hash"]
            assert t["size"] == d["size"]
            assert t["vSize"] == d["vSize"]
            assert t["bSize"] == d["bSize"]
            assert t["weight"] == d["weight"]
            assert t["segwit"] == d["segwit"]
        assert t["lockTime"] == d["lockTime"]
        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]

        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            if t["coinbase"]:
                continue
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
            assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
            assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
            assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
            if t["vIn"][i]["blockHeight"] != -1:
                assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
                assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
            if "address" in t["vIn"][i]:
                assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]

            if t["vOut"][i]["spent"] != d["vOut"][str(i)]["spent"]:
                time.sleep(1)
                if t["vOut"][i]["spent"]:
                    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" +
                                     t["vOut"][i]["spent"][0]["txId"])
                    assert r.status_code == 200
                    st = r.json()["data"]
                    if not ((st["time"] - tms >= 0) or (st["time"] - t["time"])):
                        assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]


    assert counter > 0



    assert tx_conf




def test_get_mixed_transaction_by_pointer_list_extended(conf):
    if not conf["option_transaction_history"]:
        return
    tms = int(time.time())
    r = requests.get("https://api.bitaps.com/bgl/v1/mempool/transactions")
    assert r.status_code == 200
    t = r.json()["data"]["transactions"]
    tx_list = [i["txId"] for i in t][:5]
    tx_list.append("8b162e5db25da4b506e8c96c16f16d9ed106c143502fd20a10e5230ca30939cb")
    tx_list.append("ce0139174e95e72a0be50b8d02ff9e3145e0289538117b1209174043f0a4c1b9") # coinbase

    q = time.time()
    r = requests.post(conf["base_url"] + "/rest/transactions/by/pointer/list",
                      data= json.dumps(tx_list).encode())
    assert r.status_code == 200
    dl = r.json()["data"]
    assert time.time() - q < 1


    counter = 0
    for tx in tx_list:
        time.sleep(0.4)
        d = dl[tx]

        r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" + tx)
        assert r.status_code == 200
        t = r.json()["data"]
        if d is None:
            continue
        counter += 1
        assert t["txId"] == d["txId"]

        assert t["version"] == d["version"]
        if not t["coinbase"]:
            assert t["hash"] == d["hash"]
            assert t["size"] == d["size"]
            assert t["vSize"] == d["vSize"]
            assert t["bSize"] == d["bSize"]
            assert t["weight"] == d["weight"]
            assert t["segwit"] == d["segwit"]
        assert t["lockTime"] == d["lockTime"]
        assert t["data"] == d["data"]
        assert t["coinbase"] == d["coinbase"]

        assert t["amount"] == d["amount"]
        for i in t["vIn"]:
            if t["coinbase"]:
                continue
            assert t["vIn"][i]["txId"] == d["vIn"][str(i)]["txId"]
            assert t["vIn"][i]["vOut"] == d["vIn"][str(i)]["vOut"]
            assert t["vIn"][i]["type"] == d["vIn"][str(i)]["type"]
            assert t["vIn"][i]["amount"] == d["vIn"][str(i)]["amount"]
            assert t["vIn"][i]["scriptPubKey"] == d["vIn"][str(i)]["scriptPubKey"]
            assert t["vIn"][i]["scriptPubKeyOpcodes"] == d["vIn"][str(i)]["scriptPubKeyOpcodes"]
            assert t["vIn"][i]["scriptPubKeyAsm"] == d["vIn"][str(i)]["scriptPubKeyAsm"]
            if t["vIn"][i]["blockHeight"] != -1:
                assert t["vIn"][i]["blockHeight"] == d["vIn"][str(i)]["blockHeight"]
                assert t["vIn"][i]["confirmations"] == d["vIn"][str(i)]["confirmations"]
            if "address" in t["vIn"][i]:
                assert t["vIn"][i]["address"] == d["vIn"][str(i)]["address"]
            assert t["vIn"][i]["scriptSig"] == d["vIn"][str(i)]["scriptSig"]
            assert t["vIn"][i]["sequence"] == d["vIn"][str(i)]["sequence"]
            if "txInWitness" in t["vIn"][i]:
                assert t["vIn"][i]["txInWitness"] == d["vIn"][str(i)]["txInWitness"]
            if not t["coinbase"]:
                assert t["vIn"][i]["scriptSigOpcodes"] == d["vIn"][str(i)]["scriptSigOpcodes"]
                assert t["vIn"][i]["scriptSigAsm"] == d["vIn"][str(i)]["scriptSigAsm"]
        for i in t["vOut"]:
            assert t["vOut"][i]["value"] == d["vOut"][str(i)]["value"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["nType"] == d["vOut"][str(i)]["nType"]
            assert t["vOut"][i]["type"] == d["vOut"][str(i)]["type"]
            if "addressHash" in t["vOut"][i]:
                assert t["vOut"][i]["addressHash"] == d["vOut"][str(i)]["addressHash"]
                assert t["vOut"][i]["address"] == d["vOut"][str(i)]["address"]
            assert t["vOut"][i]["scriptPubKey"] == d["vOut"][str(i)]["scriptPubKey"]
            assert t["vOut"][i]["scriptPubKeyAsm"] == d["vOut"][str(i)]["scriptPubKeyAsm"]
            assert t["vOut"][i]["scriptPubKeyOpcodes"] == d["vOut"][str(i)]["scriptPubKeyOpcodes"]

            if t["vOut"][i]["spent"] != d["vOut"][str(i)]["spent"]:
                time.sleep(1)
                r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/transaction/" +
                                 t["vOut"][i]["spent"][0]["txId"])
                assert r.status_code == 200
                st = r.json()["data"]
                if not ((st["time"] - tms >= 0) or (st["time"] - t["time"])):
                    assert t["vOut"][i]["spent"] == d["vOut"][str(i)]["spent"]

    assert counter > 0
