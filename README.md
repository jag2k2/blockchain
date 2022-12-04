# UT Blockchain Class 
This repo includes a mixture of in-class assignments and exercises from Jimmy Song's book "Programming Bitcoin".  All the code under "personal" represents my solutions to the exercises in Jimmy Song's book but I used the secp256k1 and digital signature libraries from those exercises in some of the in-class assignments.  The in-class assignments are organized by month:

## Table of Contents:
1. [Assignment 1](#assignment-1)
2. [Assignment 2](#assignment-2)
3. [Assignment 3](#assignment-3)

## Assignment 1 
**01smartcontract** - This script was developed from SuperTestnet's workshop.  The ScriptPubKey is designed to take one ScriptSig element and plug it into the equation `3x^2+2x-14`. Any result that matches the hash of the number `42` unlocks the output.   

## Assignment 2
**02rpc_examples** - I started with exercise 5 from chapter 7 of Jimmy Song's book and replaced all the web calls with rpc commands to my bitcoin client.  I obtained some testnet coins from a testnet faucet and configured my client to use the test chain.  For completeness, the `python` directory holds slightly modified versions of the in-class examples but `.\JeffCustom\send_pct_all_utxos.py` represents the bulk of my work.  That program makes separate rpc connections to a "send" wallet and a "receive" wallet.  I create a signed transaction with all utxos from the send wallet and send 80% of those amounts to a newly created address in the receive wallet.  The rest go to fees and a newly created address in the send wallet. Here is an [example transaction](https://blockstream.info/testnet/tx/d86bacf2231fa30ba6350c00d4679cab3c1bed61f4bc9fa3f4c30db6fbeed2a2) from that program: 

## Assignment 3
**03lnd_exercise** - `Testnet_Lightning_Solution.md` documents all the steps I used to create a lightning channel and use it to satisfy an invoice.  That file also holds the links to all the testnet transactions used to fund and close the channel.  

## Contributors
- [Jeff Tipps](https://github.com/jag2k2) jt45679
