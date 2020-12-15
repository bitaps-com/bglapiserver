
<img src="doc/btcapi.png" width="350">


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





 