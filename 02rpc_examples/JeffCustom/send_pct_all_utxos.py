from lib.rpc import RpcSocket
from shared.Tx import Tx

if __name__ == '__main__':
    from_rpc = RpcSocket({'wallet':'tn_wallet'})
    to_rpc = RpcSocket({'wallet':'alice_wallet'})

    all_txins = from_rpc.get_all_utxos()
    all_amount = from_rpc.get_total_unspent_sats()
    fee = 500
    send_amount = int(all_amount * 0.8)
    change_amount = all_amount - send_amount - fee
    #address = 'mquczSS7Dz82TeG4Z1sDp23TEi4jR6ApTg'
    address = None
    tx_out = to_rpc.get_txout(send_amount, address)
    tx_out_change = from_rpc.get_txout(change_amount)

    transaction = Tx(1, all_txins, [tx_out, tx_out_change], 0, True)  
    transaction.sign()
    print(transaction)

    tx_id = from_rpc.send_transaction(transaction)
    print(tx_id)