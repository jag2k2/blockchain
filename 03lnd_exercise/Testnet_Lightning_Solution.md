# Assignment 3 Lightning Network
In this assignment I copied the class [lndemo](https://github.com/cmdruid/bitcoin-programming/tree/master/lnd-demo) and renamed the `bob` directory to `jeff`. In both the `jeff` and `alice` directories I updated the `lnd.conf` file to use `testnet` instead of `regtest`.  Finally I edited all references of `regtest` in `lcli` to be `testnet`.  From there I basically followed the provided demo script with some extra commands to verify things were working as I went.  My full workflow is provided below.

## Table of Contents:
1. [Create New Address in Jeff's Node](#create-new-address-in-jeffs-node)
2. [Fund Address via Bitcoin Core](#fund-address-via-bitcoin-core)
3. [Verify Funds with lcli](#verify-funds-with-lcli)
4. [Get Node Pubkeys](#get-node-pubkeys)
5. [Alice Creates Peer Connection with Jeff](#alice-creates-peer-connection-with-jeff)
6. [Alice Verifies Peer Connection](#alice-verifies-peer-connection)
7. [Jeff Also Verifies Peer Connection](#jeff-also-verifies-peer-connection)
8. [Jeff Opens Channel](#jeff-opens-channel)
9. [Alice Creates Invoice](#alice-creates-invoice)
10. [Jeff Sends Payment](#jeff-sends-payment)
11. [Jeff Channel Balance](#jeff-channel-balance)
12. [Alice Channel Balance](#alice-channel-balance)
13. [Alice Closes Channel](#alice-closes-channel)
14. [Alice Wallet Balance](#alice-wallet-balance)
15. [Jeff Wallet Balance](#jeff-wallet-balance)
16. [Summary of Transactions](#summary-of-transactions)


## Create New Address in Jeffs Node
`./lcli newaddress p2wkh`
```
{
    "address": "tb1q8rac5z30csyydljctl4tvsl4kafvwdakzag7q2"
}
```

## Fund Address via Bitcoin Core
https://blockstream.info/testnet/tx/df40d76fc6df7cb2c2ad94635dbd508cc9846d0d75c0da6c3004b602c26b5e5c

## Verify Funds with lcli
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli walletbalance
{
    "total_balance": "200000",
    "confirmed_balance": "200000",
    "unconfirmed_balance": "0",
    "locked_balance": "0",
    "reserved_balance_anchor_chan": "0",
    "account_balance": {
        "default": {
            "confirmed_balance": "200000",
            "unconfirmed_balance": "0"
        }
    }
}
```

## Get Node Pubkeys
```
./lcli getinfo
```
- alice pubkey: `02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc`
- jeff pubkey: `03ddf75e980bf777ef930a9df298c9b5252ee6389910a4c1b65f79bb4426b3133c`

## Alice Creates Peer Connection with Jeff
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli connect 03ddf75e980bf777ef930a9df298c9b5252ee6389910a4c1b65f79bb4426b3133c@localhost:9737
{

}
```
## Alice Verifies Peer Connection
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli listpeers
{
    "peers": [
        {
            "pub_key": "03ddf75e980bf777ef930a9df298c9b5252ee6389910a4c1b65f79bb4426b3133c",
            "address": "127.0.0.1:9737",
            ...
```
## Jeff Also Verifies Peer Connection
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli listpeers
{
    "peers": [
        {
            "pub_key": "02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc",
            "address": "127.0.0.1:51844",
            ...
```

## Jeff Opens Channel
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli openchannel --node_key=02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc --local_amt=50000
{
        "funding_txid": "c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d"
}
```
https://blockstream.info/testnet/tx/c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d

## Alice Creates Invoice
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli addinvoice --amt=10000
{
    "r_hash": "c20814061f7c605157c45dcc5b186a72508647c5f41897504bdfc79a2209a107",
    "payment_request": "lntb100u1p3hq88fpp5cgypgpsl03s9z47ythx9kxr2wfggv3797svfw5ztmlre5gsf5yrsdqqcqzpgxqyz5vqsp532q2nr22fle4upcflej26fx6gke7r8laxxs3a2rmqnkaftnyln7q9qyyssqga6fmnxa3vlym8qpgu0ec93luuvtt3f2lntwfrp0f53xneee2un5kem53k2j5uf4aalt4fy6m9ww7f06n6p4y36gw9adakvecxnklvcq9v59za",
    "add_index": "1",
    "payment_addr": "8a80a98d4a4ff35e0709fe64ad24da45b3e19ffd31a11ea87b04edd4ae64fcfc"
}
```
## Jeff Sends Payment
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli sendpayment --pay_req=lntb100u1p3hq88fpp5cgypgpsl03s9z47ythx9kxr2wfggv3797svfw5ztmlre5gsf5yrsdqqcqzpgxqyz5vqsp532q2nr22fle4upcflej26fx6gke7r8laxxs3a2rmqnkaftnyln7q9qyyssqga6fmnxa3vlym8qpgu0ec93luuvtt3f2lntwfrp0f53xneee2un5kem53k2j5uf4aalt4fy6m9ww7f06n6p4y36gw9adakvecxnklvcq9v59za
Payment hash: c20814061f7c605157c45dcc5b186a72508647c5f41897504bdfc79a2209a107
Description:
Amount (in satoshis): 10000
Fee limit (in satoshis): 500
Destination: 02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc
Confirm payment (yes/no): yes
+------------+--------------+--------------+--------------+-----+----------+---------------------+-------+
| HTLC_STATE | ATTEMPT_TIME | RESOLVE_TIME | RECEIVER_AMT | FEE | TIMELOCK | CHAN_OUT            | ROUTE |
+------------+--------------+--------------+--------------+-----+----------+---------------------+-------+
| SUCCEEDED  |        0.047 |        0.450 | 10000        | 0   |  2406030 | 2645408483755032576 |       |
+------------+--------------+--------------+--------------+-----+----------+---------------------+-------+
Amount + fee:   10000 + 0 sat
Payment hash:   c20814061f7c605157c45dcc5b186a72508647c5f41897504bdfc79a2209a107
Payment status: SUCCEEDED, preimage: e853f4f2562c6ab515a33d333ea1527c4057ea0410c4984a54512254379c7096
```
## Jeff Channel Balance
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli channelbalance
{
    "balance": "39056",
    "pending_open_balance": "0",
    "local_balance": {
        "sat": "39056",
        "msat": "39056000"
    },
    "remote_balance": {
        "sat": "10000",
        "msat": "10000000"
    },
    "unsettled_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "unsettled_remote_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_remote_balance": {
        "sat": "0",
        "msat": "0"
    }
}
```
## Alice Channel Balance
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli channelbalance
{
    "balance": "10000",
    "pending_open_balance": "0",
    "local_balance": {
        "sat": "10000",
        "msat": "10000000"
    },
    "remote_balance": {
        "sat": "39056",
        "msat": "39056000"
    },
    "unsettled_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "unsettled_remote_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_local_balance": {
        "sat": "0",
        "msat": "0"
    },
    "pending_open_remote_balance": {
        "sat": "0",
        "msat": "0"
    }
}
```
## Alice Closes Channel
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli closechannel c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d
{
        "closing_txid": "b0f3a506af2a12298071b237a2578de34cbe0c4816b54eca6a6f97aa5345a760"
}
```
https://blockstream.info/testnet/tx/b0f3a506af2a12298071b237a2578de34cbe0c4816b54eca6a6f97aa5345a760

## Alice Wallet Balance
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli walletbalance
{
    "total_balance": "10000",
    "confirmed_balance": "10000",
    "unconfirmed_balance": "0",
    "locked_balance": "0",
    "reserved_balance_anchor_chan": "0",
    "account_balance": {
        "default": {
            "confirmed_balance": "10000",
            "unconfirmed_balance": "0"
        }
    }
}
```
## Jeff Wallet Balance
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli walletbalance
{
    "total_balance": "189639",
    "confirmed_balance": "189639",
    "unconfirmed_balance": "0",
    "locked_balance": "0",
    "reserved_balance_anchor_chan": "0",
    "account_balance": {
        "default": {
            "confirmed_balance": "189639",
            "unconfirmed_balance": "0"
        }
    }
}
```
## Summary of Transactions
- [Testnet transaction to fund jeff lightning node](https://blockstream.info/testnet/tx/df40d76fc6df7cb2c2ad94635dbd508cc9846d0d75c0da6c3004b602c26b5e5c)
- [Open channel testnet transaction](https://blockstream.info/testnet/tx/c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d)
- [Close channel testnet transaction](https://blockstream.info/testnet/tx/b0f3a506af2a12298071b237a2578de34cbe0c4816b54eca6a6f97aa5345a760)