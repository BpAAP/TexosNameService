import smartpy as sp

class NameService(sp.Contract):
    def __init__(self,givenOwner):
        self.init(owner = givenOwner,
                  keyToCID = sp.map(tkey = sp.TString))
    
    @sp.entry_point
    def setCID(self,params):
        sp.if (self.data.owner == sp.sender):
            self.data.keyToCID[sp.set_type_expr(params.key,sp.TString)] = sp.set_type_expr(params.newCID,sp.TString)
    
    @sp.entry_point
    def removeEntry(self,params):
        sp.if (self.data.owner == sp.sender):
            del self.data.keyToCID[sp.set_type_expr(params.key,sp.TString)]
        
        


@add_test(name = "GeneralTest")
def test():
    scenario = sp.test_scenario()
    
    trueOwner = sp.address("tz1-trueOwner-1234")
    falseOwner = sp.address("tz1-falseOwner-1234")
    nonce  = 0
    
    
    c1 = NameService(trueOwner)
    scenario += c1
    scenario.h1("Creating Smart Contract, passing true owner address.")
    
    scenario.p("Adding first new entry")
    scenario += c1.setCID(key = "TestKey"+str(nonce),newCID="CIDNo"+str(nonce)).run(sender=trueOwner)
    nonce +=1
    
    scenario.p("Adding second new entry")
    scenario += c1.setCID(key = "TestKey"+str(nonce),newCID="CIDNo"+str(nonce)).run(sender=trueOwner)
    nonce +=1
    
    scenario.p("Changing first entry")
    scenario += c1.setCID(key = "TestKey"+str(0),newCID="AlteredCIDNo"+str(0)).run(sender=trueOwner)
    
    scenario.p("Not the owner, trying to change the 2nd entry ")
    scenario += c1.setCID(key = "TestKey1",newCID="MaliciousCID").run(sender=falseOwner)
    
    scenario.p("Not the owner, trying to remove 1st entry")
    scenario += c1.removeEntry(key="TestKey0").run(sender=falseOwner)
    
    scenario.p("True, trying to remove 1st entry")
    scenario += c1.removeEntry(key="TestKey0").run(sender=trueOwner)
    
    