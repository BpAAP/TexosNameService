# Backend for Tezos based Name Resolution

Files for deploying a name resolving smart contract on the Tezos blockchain.

In this folder:
1. `michelson-code` contains the compiled Michelson code of the smartcontract. This is to be used when deploying the contract.
2. `NameService.py` is the python file from which the michelson code was compiled using SmartPy. Upload this file to `https://smartpy.io/dev/` to conveniently view it or test it. This example is geared towards resolving IPFS Content IDs, but this is only relevant for the python file.

## Smartcontract functionality
When the smart contract is created it is provided with the address of tezos account from which it will be controlled (such as `tz1...`), let this be the `OWNERACCOUNT`.

Once created the contract will only accept commands if the address requesting these is `OWNERACCOUNT`.

Requests from anyone else will not throw an error, but no changes will be made.

Two functions are available.:

1. `setCID` is called with a key and a new value for that key. It replaces the current value with the new value, or creates an entry if it doesn't yet exist with the new value. In the IPFS context it would be given `myKey` which is just some handle for the frontend to use, and `MyWebsiteCID` the CID for the website on IPFS.

2. `removeEntry` is called with a key and removes that key and its associated value from the contract storage.

There is no hardcoded limit to how many entries can be made. (To my knowledge)

## Deployment
NOTE: It is strongly recommended that you experiment on the Testnet. For more detailed instructions do a google search.

For deployment and control I've found the Galleon wallet to be user friendly and sufficient.

To deploy the contract, here are some overarching steps for setting up Galleon:
1. Get a test account for the testnet, instructions for this can be found online.
2. Install Galleon wallet.
3. In settings, under Choose a different node, pick the testnet
4. In Galleon click 'Create new wallet'
5. Specify a location to store the wallet file (it should have the file extension `.tezwallet`)
6. Enter a password, whatever you like, this is completly your choice, it has nothing to do with the test accound you've acquired.
7. Go to the restore from backup tab and enter the private key of the test account you've chosen.
8. Click through the next steps until you see the main page of the wallet.

Now for deploying the contract:
1. On the left, click the "+" button next to interacting with contracts.
2. Understand the dialogue and click proceed, go the the "Deploy a new contract" tab.
3. Fill in as follows:
Format : `Michelson`
Parameters : `Pair {} "OWNERADDRESS"`
Storage Limit : `1000`
Gas Limit : `50000`
Amount : `0` ***
4. Pick a fee, higher fee => faster deployment
5. Paste the smartcontract code into the box.
6. Enter your password and click Deploy

*** NOTE: IF YOU SEND TEZ TO THE CONTRACT THERE IS NO WAY TO GET IT BACK. THE CONTRACT DOES !NOT! NEED A BALANCE TO WORK.

## To add or change an entry:
1. Select your contract form the left side. Go to the Invoke tab.
2. Fill in as follows:
Format : `Michelson`
Parameters : `Right (Pair "KEY" "VALUE")`
Entry Point : `default`
Storage Limit : `1000`
Gas Limit : `50000`
Amount : `0` ***
3. Pick a fee, enter password, click Invoke

## To remove and entry:
1. Select your contract form the left side. Go to the Invoke tab.
2. Fill in as follows:
Format : `Michelson`
Parameters : `Left "KEY"`
Entry Point : `default`
Storage Limit : `1000`
Gas Limit : `50000`
Amount : `0` ***
3. Pick a fee, enter password, click Invoke

## Deploying for real:
Deploying to the Mainnet works very similarly, without the free money and some self-evident changes to the steps above.