from lib.rpc import RpcSocket
from shared.Tx import Tx

if __name__ == '__main__':
    from_rpc = RpcSocket({'wallet':'alice_wallet'})
    to_rpc = RpcSocket({'wallet':'bob_wallet'})

    all_txins = from_rpc.get_all_utxos()
    all_amount = from_rpc.get_total_unspent_sats()
    fee = 500
    tx_out = to_rpc.get_txout(all_amount - fee)

    transaction = Tx(1, all_txins, [tx_out], 0, True)  
    transaction.sign()
    print(transaction)

    tx_id = from_rpc.send_transaction(transaction)
    print(tx_id)