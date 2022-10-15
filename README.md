# UT Blockchain Class 
This repo includes a mixture of in-class assignments and exercises from Jimmy Song's book "Programming Bitcoin".  All the code under "personal" represents my solutions from the exercises in Jimmy Song's book but I used the secp256k1 and digital signature libraries from those exercises in some of the in-class assignments.  The in-class assignments are organized by month:

## Table of Contents:
1. [Month1](#month-1)
2. [Month2](#month-2)

## Month 1

The following directories hold month 1 assignments:

- **01smartcontract** - This was developed from SuperTestnet's workshop.  The ScriptPubKey is designed to take one ScriptSig element and plug it into the equation `3x^2+2x-14`. Any result that matches the hash of the number `42` unlocks the output.   
- **02rpc_examples** - I started with exercise 5 from chapter 7 of Jimmy Song's book and replaced all the web calls with rpc commands to my bitcoin client.  I obtained some testnet coins from a testnet faucet and configured my client to use the test chain.  For completeness, the `python` directory holds slightly modified versions of the in-class examples but `JeffCustom\send_pct_all_utxos.py` represents the bulk of my work.  That program makes separate rpc connections to a "send" wallet and a "receive" wallet.  I create a signed transaction with all utxos from the send wallet and send 80% of those amounts to a newly created address in the receive wallet.  The rest go to fees and a newly created address in the send wallet. Here is an [example transaction](https://blockstream.info/testnet/tx/d86bacf2231fa30ba6350c00d4679cab3c1bed61f4bc9fa3f4c30db6fbeed2a2) from that program: 

## Month 2


## Contributors
- [Jeff Tipps](https://github.com/jag2k2) jt45679
