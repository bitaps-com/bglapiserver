import requests
from pybgl import *
import base64


def test_get_block_data_pointer(conf):
    r = requests.get(conf["base_url"] + "/rest/block/data/32751")
    assert r.status_code == 200
    d = r.json()["data"]
    assert 'height' in d
    assert 'hash' in d
    assert 'header' in d
    assert 'adjustedTimestamp' in d

    assert d['height'] ==32751
    assert d['hash'] == "0000000000000494dd490cadaa9862f112a40eb89c6fb096f810b52364ff03c4"
    assert d['header'] == "AAAAIIWsx99LgjiFdoRjnFWnSh4cyPmopej3DIgLAAAAAAAA1LrkJgStopyo4pRqz5ASs7fJN9IK2pDo54X31jJDJyD4WqhfmrAPGkYT6Aw2"
    assert d['adjustedTimestamp'] == 1604868856
    assert d["previousBlockHash"] == "0000000000000b880cf7e8a5a8f9c81c1e4aa7559c6384768538824bdfc7ac85"
    assert d["nextBlockHash"] == "000000000000096efde435ed8fc3ff0be91263f3c5cccd5359c854a5d2ca67a1"
    assert d["merkleRoot"] == "20274332d6f785e7e890da0ad237c9b7b31290cf6a94e2a89ca2ad0426e4bad4"
    assert d["medianBlockTime"] == 1604865535
    assert d["blockTime"] == 1604868856
    assert d["size"] == 21855
    assert d["strippedSize"] == 8982
    assert d["weight"] == 48801
    assert d["bits"] == 437235866
    assert d["bitsHex"] == "1a0fb09a"
    assert d["nonce"] == 216535878
    assert d["nonceHex"] == "0ce81346"
    assert d["version"] == 536870912
    assert d["versionHex"] == "20000000"
    assert d["difficulty"] == 1069287.4792706054
    assert d["blockDifficulty"] == 3661891.1572588184
    assert d["blockReward"] == 20000000000
    assert d["blockFeeReward"] == 29840
    assert d["coinbase"] == "02ef7f04f85aa85f08fabe6d6d000000000000000000000000000000000000000000000000000000000000000001000000000000000800659a4af847040f2f4d696e696e672d4475746368302f"
    assert d["transactionsCount"] == 54

def test_get_data_last_n_blocks(conf):
    r = requests.get(conf["base_url"] + "/rest/blocks/data/last/16")
    assert r.status_code == 200
    rd = r.json()["data"]
    for d in rd:
        assert 'height' in d
        assert 'hash' in d
        assert 'header' in d
        assert 'adjustedTimestamp' in d
        assert d['hash'] == rh2s(sha3_256(base64.b64decode(d["header"])[:80], hex=False))
    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/blocks/last/16")
    rd_1 = r.json()["data"]
    for i in range(16):
        assert rd_1[i]["height"] == rd[i]["height"]
        assert rd_1[i]["hash"] == rd[i]["hash"]
        # assert rd_1[i]["header"] == rd[i]["header"]
        # assert rd_1[i]["adjustedTimestamp"] == rd[i]["adjustedTimestamp"]
        assert rd_1[i]["previousBlockHash"] == rd[i]["previousBlockHash"]
        assert rd_1[i]["nextBlockHash"] == rd[i]["nextBlockHash"]
        assert rd_1[i]["merkleRoot"] == rd[i]["merkleRoot"]
        # assert rd_1[i]["medianBlockTime"] == rd[i]["medianBlockTime"]

        assert rd_1[i]["blockTime"] == rd[i]["blockTime"]
        assert rd_1[i]["size"] == rd[i]["size"]
        assert rd_1[i]["strippedSize"] == rd[i]["strippedSize"]
        assert rd_1[i]["weight"] == rd[i]["weight"]
        assert rd_1[i]["bits"] == rd[i]["bits"]
        assert rd_1[i]["bitsHex"] == rd[i]["bitsHex"]
        assert rd_1[i]["nonce"] == rd[i]["nonce"]
        assert rd_1[i]["nonceHex"] == rd[i]["nonceHex"]
        assert rd_1[i]["version"] == rd[i]["version"]
        assert rd_1[i]["versionHex"] == rd[i]["versionHex"]
        assert rd_1[i]["difficulty"] == rd[i]["difficulty"]
        assert rd_1[i]["blockDifficulty"] == rd[i]["blockDifficulty"]
        assert rd_1[i]["blockReward"] == rd[i]["blockReward"]
        assert rd_1[i]["blockFeeReward"] == rd[i]["blockFeeReward"]
        # assert rd_1[i]["coinbase"] == rd[i]["coinbase"]
        assert rd_1[i]["transactionsCount"] == rd[i]["transactionsCount"]
        # assert rd_1[i]["miner"] == rd[i]["miner"]


def test_get_data_today_blocks(conf):
    r = requests.get(conf["base_url"] + "/rest/blocks/data/today")
    assert r.status_code == 200
    rd = r.json()["data"]
    for d in rd:
        assert 'height' in d
        assert 'hash' in d
        assert 'header' in d
        assert 'adjustedTimestamp' in d
        assert d['hash'] == rh2s(sha3_256(base64.b64decode(d["header"])[:80], hex=False))
    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/blocks/today")
    rd_1 = r.json()["data"]
    for i in range(len(rd_1)):
        assert rd_1[i]["height"] == rd[i]["height"]
        assert rd_1[i]["hash"] == rd[i]["hash"]
        # assert rd_1[i]["header"] == rd[i]["header"]
        # assert rd_1[i]["adjustedTimestamp"] == rd[i]["adjustedTimestamp"]
        assert rd_1[i]["previousBlockHash"] == rd[i]["previousBlockHash"]
        assert rd_1[i]["nextBlockHash"] == rd[i]["nextBlockHash"]
        assert rd_1[i]["merkleRoot"] == rd[i]["merkleRoot"]
        # assert rd_1[i]["medianBlockTime"] == rd[i]["medianBlockTime"]

        assert rd_1[i]["blockTime"] == rd[i]["blockTime"]
        assert rd_1[i]["size"] == rd[i]["size"]
        assert rd_1[i]["strippedSize"] == rd[i]["strippedSize"]
        assert rd_1[i]["weight"] == rd[i]["weight"]
        assert rd_1[i]["bits"] == rd[i]["bits"]
        assert rd_1[i]["bitsHex"] == rd[i]["bitsHex"]
        assert rd_1[i]["nonce"] == rd[i]["nonce"]
        assert rd_1[i]["nonceHex"] == rd[i]["nonceHex"]
        assert rd_1[i]["version"] == rd[i]["version"]
        assert rd_1[i]["versionHex"] == rd[i]["versionHex"]
        assert rd_1[i]["difficulty"] == rd[i]["difficulty"]
        assert rd_1[i]["blockDifficulty"] == rd[i]["blockDifficulty"]
        assert rd_1[i]["blockReward"] == rd[i]["blockReward"]
        assert rd_1[i]["blockFeeReward"] == rd[i]["blockFeeReward"]
        # assert rd_1[i]["coinbase"] == rd[i]["coinbase"]
        assert rd_1[i]["transactionsCount"] == rd[i]["transactionsCount"]
        # assert rd_1[i]["miner"] == rd[i]["miner"]


def test_get_data_date_blocks(conf):
    r = requests.get(conf["base_url"] + "/rest/blocks/data/date/20201111")
    assert r.status_code == 200
    rd = r.json()["data"]
    for d in rd:
        assert 'height' in d
        assert 'hash' in d
        assert 'header' in d
        assert 'adjustedTimestamp' in d
        assert d['hash'] == rh2s(sha3_256(base64.b64decode(d["header"])[:80], hex=False))
    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/blocks/date/20201111")
    rd_1 = r.json()["data"]
    assert len(rd_1) == 149
    for i in range(len(rd_1)):
        assert rd_1[i]["height"] == rd[i]["height"]
        assert rd_1[i]["hash"] == rd[i]["hash"]
        # assert rd_1[i]["header"] == rd[i]["header"]
        # assert rd_1[i]["adjustedTimestamp"] == rd[i]["adjustedTimestamp"]
        assert rd_1[i]["previousBlockHash"] == rd[i]["previousBlockHash"]
        assert rd_1[i]["nextBlockHash"] == rd[i]["nextBlockHash"]
        assert rd_1[i]["merkleRoot"] == rd[i]["merkleRoot"]
        # assert rd_1[i]["medianBlockTime"] == rd[i]["medianBlockTime"]

        assert rd_1[i]["blockTime"] == rd[i]["blockTime"]
        assert rd_1[i]["size"] == rd[i]["size"]
        assert rd_1[i]["strippedSize"] == rd[i]["strippedSize"]
        assert rd_1[i]["weight"] == rd[i]["weight"]
        assert rd_1[i]["bits"] == rd[i]["bits"]
        assert rd_1[i]["bitsHex"] == rd[i]["bitsHex"]
        assert rd_1[i]["nonce"] == rd[i]["nonce"]
        assert rd_1[i]["nonceHex"] == rd[i]["nonceHex"]
        assert rd_1[i]["version"] == rd[i]["version"]
        assert rd_1[i]["versionHex"] == rd[i]["versionHex"]
        assert round(rd_1[i]["difficulty"]) == round(rd[i]["difficulty"])
        assert rd_1[i]["blockDifficulty"] == rd[i]["blockDifficulty"]
        assert rd_1[i]["blockReward"] == rd[i]["blockReward"]
        assert rd_1[i]["blockFeeReward"] == rd[i]["blockFeeReward"]
        # assert rd_1[i]["coinbase"] == rd[i]["coinbase"]
        assert rd_1[i]["transactionsCount"] == rd[i]["transactionsCount"]
        # assert rd_1[i]["miner"] == rd[i]["miner"]

def test_get_data_last_n_hours_blocks(conf):
    r = requests.get(conf["base_url"] + "/rest/blocks/data/last/10/hours")
    assert r.status_code == 200
    rd = r.json()["data"]
    for d in rd:
        assert 'height' in d
        assert 'hash' in d
        assert 'header' in d
        assert 'adjustedTimestamp' in d
        assert d['hash'] == rh2s(sha3_256(base64.b64decode(d["header"])[:80], hex=False))
    r = requests.get("https://api.bitaps.com/bgl/v1/blockchain/blocks/last/16/hours")
    rd_1 = r.json()["data"]
    for i in range(16):
        assert rd_1[i]["height"] == rd[i]["height"]
        assert rd_1[i]["hash"] == rd[i]["hash"]
        # assert rd_1[i]["header"] == rd[i]["header"]
        # assert rd_1[i]["adjustedTimestamp"] == rd[i]["adjustedTimestamp"]
        assert rd_1[i]["previousBlockHash"] == rd[i]["previousBlockHash"]
        assert rd_1[i]["nextBlockHash"] == rd[i]["nextBlockHash"]
        assert rd_1[i]["merkleRoot"] == rd[i]["merkleRoot"]
        # assert rd_1[i]["medianBlockTime"] == rd[i]["medianBlockTime"]

        assert rd_1[i]["blockTime"] == rd[i]["blockTime"]
        assert rd_1[i]["size"] == rd[i]["size"]
        assert rd_1[i]["strippedSize"] == rd[i]["strippedSize"]
        assert rd_1[i]["weight"] == rd[i]["weight"]
        assert rd_1[i]["bits"] == rd[i]["bits"]
        assert rd_1[i]["bitsHex"] == rd[i]["bitsHex"]
        assert rd_1[i]["nonce"] == rd[i]["nonce"]
        assert rd_1[i]["nonceHex"] == rd[i]["nonceHex"]
        assert rd_1[i]["version"] == rd[i]["version"]
        assert rd_1[i]["versionHex"] == rd[i]["versionHex"]
        assert rd_1[i]["difficulty"] == rd[i]["difficulty"]
        assert rd_1[i]["blockDifficulty"] == rd[i]["blockDifficulty"]
        assert rd_1[i]["blockReward"] == rd[i]["blockReward"]
        assert rd_1[i]["blockFeeReward"] == rd[i]["blockFeeReward"]
        # assert rd_1[i]["coinbase"] == rd[i]["coinbase"]
        assert rd_1[i]["transactionsCount"] == rd[i]["transactionsCount"]
        # assert rd_1[i]["miner"] == rd[i]["miner"]



