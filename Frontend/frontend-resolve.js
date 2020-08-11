//Specify the address of the smart contract.
contractAddress = "KT1G8DBxfyuokvuuBM7ftCohqm3RfrW2TBef"
//Specify the key that needs to be resolved.
entryKey = "MyKey"

//Function responsible for getting CID
async function resolve(contractAddress,entryKey){
    Tezos = window.taquito.Tezos
    //NOTE: USING TESTNET
    Tezos.setProvider({rpc: 'https://carthagenet.SmartPy.io'})
    
    //Get contract
    const contract = await Tezos.contract.at(contractAddress)
    //Get storage of contract
    const storage = await contract.storage()
    //Get value associated with entryKey, from the map keyToCID
    const value = await storage.keyToCID.get(entryKey)
    //Return value
    return value
}

//Start resolving when window is loaded
window.addEventListener('load', function() {
    resolve(contractAddress,entryKey).then(value => {
        //If resolution succeded, redirect to that file
        /// on IPFS through cloudflare gateway
        console.log("Resolution success, attempting navigation to:" + value + "using cloudflare gateway.")
        window.location.href = "https://cloudflare-ipfs.com/ipfs/" + value
    }, reason => {
        //Resolution failed, log why
        console.log("Resolution failed, reason:")
        console.log(reason)
    })
})



