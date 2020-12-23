
<img src="doc/bglapi.png" width="350">


## BGLAPI Server

### Introduction

BGLAPI Server is based on [BTCAPI Server](https://github.com/bitaps-com/btcapiserver)

BGLAPI Server is a server platform for working with Bitgesell blockchain and the network. 
This project is free and open source and can be used to build various services, 
both non-commercial and commercial, without any legal restrictions.

BGLAPI can be used as a backend for wallets, block explorers, payment processing and analytical platforms.

You can run BGLAPI as a self-hosted solution, or use a third-party public host.


### Software is still under development, first release will be soon!

### Requirements

* Python 3.3.3+
* https://github.com/bitaps-com/pybgl
* https://github.com/bitaps-com/aiojsonrpc
* BGL Core 0.1.2+
* Docker

### Installation

chapter will be added soon ...

### API Modules

* **Transaction** store and provide information about all bitcoin transactions
* **Merkle proof** store and provide cryptographic proofs of the existence of a transactions in a blocks
* **Transaction history** store and provide historical transactions data for addresses 
* **Address state** store and provide state of addresses
* ~~**Address timeline** store and provide addresses state changes over time by transaction, day and month~~
* ~~**Blockchain analytica** store and provide blockchain analytic~~
* **Mempool analytica** store and provide unconfirmed transactions set analytic
* **Transaction fee analytica** store and provide transactions fee estimation data
* ~~**Nodes discovery** discover and provide list of available bitcoin nodes~~
* ~~**Market data** fetch and provide markets data~~
* ~~**Deterministic wallet** store and provide HD wallets state and historical data~~
* ~~**Payment forwarding** engine for payments forwarding service~~
* ~~**Hot wallet** engine for wallet service~~

### API documentation

Please see full [API documentation](https://github.com/bitaps-com/bglapiserver/tree/master/api)

### API examples

API implementation is available at the endpoint https://api.bitaps.com/bgl/v1/blockchain

##### Block information

``` bash
$ curl --request GET \
>     --url https://api.bitaps.com/bgl/v1/blockchain/block/37258 \
>     --header 'Content-Type: application/json'


{"data": {"height": 37258,
          "hash": "0000000000000a6124e6e73baac0a001767bdcdd2b9c38de3b128fe894886037",
          "header": "AAAAIFujfyl1GmRWL2Zn6UC3T/L6cPEtlq8bnWYEAAAAAAAAyNExW/1GYxdvS3K3wfpg/lQysPFB1aamUZUKUp5w3VL2idNfNHsOGmBuiW8C",
          "version": 536870912,
          "previousBlockHash": "00000000000004669d1baf962df170faf24fb740e967662f56641a75297fa35b", 
          "merkleRoot": "52dd709e520a9551a6a6d541f1b03254fe60fac1b7724b6f176346fd5b31d1c8",
          "bits": 437156660, 
          "nonce": 1871277664,
          "weight": 3917,
          "size": 1730, 
          "strippedSize": 729,
          "amount": 199999987238,
          "target": "0000000000000e7b340000000000000000000000000000000000000000000000",
          "miner": null,
          "medianBlockTime": 1607697176,
          "blockTime": 1607698934,
          "receivedTimestamp": 1607698943,
          "adjustedTimestamp": 1607698934,
          "bitsHex": "1a0e7b34",
          "nonceHex": "6f896e60",
          "versionHex": "20000000", 
          "difficulty": 1158528.8464602274,
          "blockDifficulty": 1616360.0919962383,
          "nextBlockHash": "000000000000073e1fe6830068349b9fc84e834e354fdaf83c1b4fb94891548b",
          "estimatedBlockReward": 20000000000,
          "blockReward": 20000000000,
          "blockFeeReward": 1707,
          "confirmations": 1691,
          "transactionsCount": 2,
          "coinbase": "038a910004f689d35f08fabe6d6d000000000000000000000000000000000000000000000000000000000000000001000000000000000800b170d6fad5090f2f4d696e696e672d4475746368322f"},
 "time": 0.0011}
```

##### Transaction information

``` bash
$ curl --request GET \
>     --url https://api.bitaps.com/bgl/v1/blockchain/transaction/b68b508031ceb03130a749d490ce09ac31afb2d5ba8f28d85f5688b799bd5723 \
>     --header 'Content-Type: application/json'

{"data": {"segwit": true,
          "rbf": false, 
          "txId": "998835c72dc30a9169bdc6d7837dd2ed881a13f506a668e9217c448282b30bb1",
          "hash": "b68b508031ceb03130a749d490ce09ac31afb2d5ba8f28d85f5688b799bd5723",
          "version": 2, 
          "size": 222,
          "vSize": 141,
          "bSize": 113,
          "lockTime": 0,
          "vIn":  {"0": {"txId": "eabbd66d5b41e4a60264b87c3905491a9aeac3a8ff7872f48a582b0c8fc79846",
                         "vOut": 1,
                         "scriptSig": "",
                         "sequence": 4294967295,
                         "txInWitness": ["3044022033fb6bcf12954da53a76226854ca961083b2a45eb47733de4b785633611391cf02200082b37770b5fbef4ffc35fcbe1655ee293608494aebd5e903ffb5b9d0f50a3401", "03f51be54fa8cbb51f16834ba976f8e71653c2700c7af9151f80e8d6475109c848"], 
                         "scriptSigOpcodes": "",
                         "scriptSigAsm": "",
                         "type": "P2WPKH",
                         "amount": 13677157503,
                         "blockHeight": 37222,
                         "confirmations": 1725,
                         "address": "bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y", 
                         "scriptPubKey": "00145c659e6fcd37d706910bc4f080c033247d473804", 
                         "scriptPubKeyOpcodes": "OP_0 [20]",
                         "scriptPubKeyAsm": "OP_0 OP_PUSHBYTES[20] 5c659e6fcd37d706910bc4f080c033247d473804"}},
          "vOut":  {"0": {"value": 54350000,
                          "scriptPubKey": "001437dc0a14a04e3f182da33e01adcdd036642fca5e", 
                          "nType": 5, 
                          "type": "P2WPKH", 
                          "addressHash": "37dc0a14a04e3f182da33e01adcdd036642fca5e", 
                          "reqSigs": 1, 
                          "address": "bgl1qxlwq599qfcl3stdr8cq6mnwsxejzljj7tf8ugc", 
                          "scriptPubKeyOpcodes": "OP_0 [20]", 
                          "scriptPubKeyAsm": "OP_0 OP_PUSHBYTES[20] 37dc0a14a04e3f182da33e01adcdd036642fca5e", 
                          "spent": []}, 
                    "1": {"value": 13622807221, 
                          "scriptPubKey": "00145c659e6fcd37d706910bc4f080c033247d473804", 
                          "nType": 5, 
                          "type": "P2WPKH", 
                          "addressHash": "5c659e6fcd37d706910bc4f080c033247d473804", 
                          "reqSigs": 1, 
                          "address": "bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y", 
                          "scriptPubKeyOpcodes": "OP_0 [20]", 
                          "scriptPubKeyAsm": "OP_0 OP_PUSHBYTES[20] 5c659e6fcd37d706910bc4f080c033247d473804", 
                          "spent": []}},
          "confirmations": 1707,
          "blockHash": "00000000000001e273c2e54c27e947ae74c19df95770074827c8effd84833a07",
          "blockHeight": 37240, 
          "coinbase": false,
          "data": null,       
          "amount": 13677157221,
          "fee": 282,   
          "time": 1607689608, 
          "blockTime": 1607690070, 
          "blockIndex": 1, 
          "flag": "01",
          "weight": 561,
          "merkleProof": "8XO6W6VoG6mhb0pBO6K+zeICkdzBswW6UODI8knWp/w=",
          "inputsAmount": 13677157503,
          "outputsAmount": 13677157221,
          "adjustedTimestamp": 1607690070,
          "valid": true,
          "feeRate": 2.0},
 "time": 0.0038}
```

##### Unspend Transaction Outputs for address

```bash
$ curl --request GET \
>     --url https://api.bitaps.com/bgl/v1/blockchain/address/utxo/bgl1qt3jeum7dxltsdygtcncgpspny375wwqyvap65y \
>     --header 'Content-Type: application/json'

{"data": [{"txId": "998835c72dc30a9169bdc6d7837dd2ed881a13f506a668e9217c448282b30bb1",
           "vOut": 1,
           "block": 37240,
           "txIndex": 1,
           "amount": 13622807221}],
 "time": 0.0022}
```





 