change cli and ln.conf to use testnet instead of regtest

- tab 1: ./bitcoind
- tab 2: ./lnd --configfile=lnd.conf
- tab 3: ./lcli create

## Create new address in Jeff's node: 
`./lcli newaddress p2wkh`
```
{
    "address": "tb1q8rac5z30csyydljctl4tvsl4kafvwdakzag7q2"
}
```

## Fund address via bitcoincore
https://blockstream.info/testnet/tx/df40d76fc6df7cb2c2ad94635dbd508cc9846d0d75c0da6c3004b602c26b5e5c

## Verify funds with lnd
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

## Get node pubkeys
```
./lcli getinfo
```
- alice pubkey: `02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc`
- jeff pubkey: `03ddf75e980bf777ef930a9df298c9b5252ee6389910a4c1b65f79bb4426b3133c`

## Alice creates peer connection with Jeff
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli connect 03ddf75e980bf777ef930a9df298c9b5252ee6389910a4c1b65f79bb4426b3133c@localhost:9737
{

}
```
## Alice verifies peer connection:
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli listpeers
{
    "peers": [
        {
            "pub_key": "03ddf75e980bf777ef930a9df298c9b5252ee6389910a4c1b65f79bb4426b3133c",
            "address": "127.0.0.1:9737",
            ...
```
## Bob also verifies peer connection:
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli listpeers
{
    "peers": [
        {
            "pub_key": "02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc",
            "address": "127.0.0.1:51844",
            ...
```

## Jeff opens channel:
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/jeff$ ./lcli openchannel --node_key=02dbf1b1b906d6934ef64ec4e25b1abf15e5cfad8675933e57585d48d1f51ec0cc --local_amt=50000
{
        "funding_txid": "c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d"
}
```

https://blockstream.info/testnet/tx/c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d

## Alice creates invoice
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli addinvoice --amt=10000
{
    "r_hash": "c20814061f7c605157c45dcc5b186a72508647c5f41897504bdfc79a2209a107",
    "payment_request": "lntb100u1p3hq88fpp5cgypgpsl03s9z47ythx9kxr2wfggv3797svfw5ztmlre5gsf5yrsdqqcqzpgxqyz5vqsp532q2nr22fle4upcflej26fx6gke7r8laxxs3a2rmqnkaftnyln7q9qyyssqga6fmnxa3vlym8qpgu0ec93luuvtt3f2lntwfrp0f53xneee2un5kem53k2j5uf4aalt4fy6m9ww7f06n6p4y36gw9adakvecxnklvcq9v59za",
    "add_index": "1",
    "payment_addr": "8a80a98d4a4ff35e0709fe64ad24da45b3e19ffd31a11ea87b04edd4ae64fcfc"
}
```
## Jeff sends payment
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
## Jeff channel balance
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
## Alice channel balance
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
## Alice closes channel
```
jtipps@DESKTOP-J69RTBS:~/GitRepos/ut-blockchain/03lnd_exercise/lnd-demo/alice$ ./lcli closechannel c8e3cb56760f9525264999e9d6f626010331e8df5a9d0708476425c863939c8d
{
        "closing_txid": "b0f3a506af2a12298071b237a2578de34cbe0c4816b54eca6a6f97aa5345a760"
}
```
https://blockstream.info/testnet/tx/b0f3a506af2a12298071b237a2578de34cbe0c4816b54eca6a6f97aa5345a760

## Alice wallet balance
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
## Jeff wallet balance
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

## Defund Lightning Nodes
https://blockstream.info/testnet/tx/3fe906ded977225b87deaaca031a122c9ed814450e9d947135be828f9f3e61f9
https://blockstream.info/testnet/tx/0e7973f286f1a0e1b6ea7078e0640e7c801bc02ff8e85190effa596fdea9758f