# xrpl-py-lite
A lite XRPL SDK for python devs, to focus on developing real world applications, while keeping out the ambiguity

LiteXrpl is a light weight python SDK for developing real world software solutions with the XRP Ledger.

It was built to focus on the important stuff and do them simply and precisely like creating and managing an account, creation and management of xrpl assets and objects.

it currently supports:

1. Account creation
2. XRPL and Asset transfer
3. Xrpl and asset management
4. Creation and management of Escrows, with support for conditions 
5. Creation and management of Checks
6. Creation and mangement of Offers
7. Token creation and management
8. NFT creation and management
etc


```
wallet = xLiteWallet("https://s.altnet.rippletest.net:51234","https://testnet.xrpl.org/accounts/", "https://testnet.xrpl.org/transactions/")

eng = xLiteToolSet("https://s.altnet.rippletest.net:51234","https://testnet.xrpl.org/accounts/", "https://testnet.xrpl.org/transactions/")

[TOOLSET]
eng.toTestnet()
eng.toMainnet()
eng.holding_currencies()
eng.created_assets_cold_addr()
eng.created_assets_hot_addr()
eng.add_asset()
eng.modify_ripple_status()
eng.remove_asset()
eng.delete_account()
eng.merge_account()
eng.create_xrp_check()
eng.account_xrp_checks()
eng.account_xrp_checks()
eng.cash_xrp_check()
eng.cancel_check()
eng.create_asset_check()
eng.cash_asset_check()
eng.account_asset_checks()
eng.create_offer()
eng.account_offers()
eng.cancel_offer()
eng.all_offers()
eng.create_escrow() # Misc.genCondition_Fulfillment()
eng.schedule_xrp()
eng.account_escrows()
eng.cancel_escrow()
eng.finish_escrow()

[WALLET]
wallet.toTestnet()
wallet.toMainnet()
wallet.show_account_in_explorer()
wallet.show_transaction_in_explorer()
wallet.generate_xrp_wallet()
wallet.restore_wallet()
wallet.spendable_xrp_balance()
wallet.xrp_balance()
wallet.get_network_fee()
wallet.get_account_next_seq_number()
wallet.account_exists()
wallet.xrp_transactions()
wallet.asset_transactions()
wallet.send_xrp()
wallet.send_currency()
wallet.account_assets()

```



note: test haven't been run on this package
