Smart contract was made using SmartPy and compiled to michelson.

Galleon Wallet is used for interacting with the Tezos Blockchain. 

## Deploy the contract:
Go to `contract -> deploy new contract` -> enter these:
1. Format : `Michelson`
2. Parameters : `Pair {} "OWNERADDRESS"`
3. No Entry Point argument
4. All the same stuff as below

## Create new/set new value:
Go to `contract -> invoke contract` -> enter these:
1. Format : Michelson
2. Parameters : `Right (Pair "KEY" "ADDRESS")`
3. Entry Point : `default`
4. Storage Limit : `1000`
5. Gas Limit : `50000`
6. Amount : `0` <---Really important, if you transfer tez to the contract, there is no way to get it back.
7. Fee : Pick one
8. Enter wallet password
9. Click Invoke

## Remove entry
Go to `contracts -> invoke contract` -> enter these:
1. Format : Michelson
2. Parameters : 'Left "SecondTest"`
3. Entry Point : `default`
4. All others as for 'Create new/set new value' above.

