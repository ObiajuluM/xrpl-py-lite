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

It will support the following and more in the future:
1. Payment channels
2. Token creation and management
3. NFT creation and management
4. Account Set transactions
5. Rekeying
etc

`accounts`
```
wallet = xLiteWallet("https://s.altnet.rippletest.net:51234","https://testnet.xrpl.org/accounts/", "https://testnet.xrpl.org/transactions/")

wallet.generate_xrp_wallet(name="my test wallet")

wallet.restore_wallet(name="test", seed="your xrpl seed")

wallet.spendable_xrp_balance(wallet_addr="rWalletgoesHEre")

wallet.xrp_transactions(wallet_addr="")

wallet.asset_transactions(wallet_addr="")

wallet.send_xrp()

wallet.send_currency()

wallet.account_assets(wallet_addr="")

```



note: test haven't been run on this package
