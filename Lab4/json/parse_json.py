import json

# ```
# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
# ```

print("Interface Status\n")
print("================================================================================")
print("{:<50} {:<20} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("-------------------------------------------------- --------------------  ------  ------")

with open("sample-data.json", 'r') as f:
    data = json.load(f)
    for item in data["imdata"]:
        dn = item["l1PhysIf"]["attributes"]["dn"]
        desc = item["l1PhysIf"]["attributes"]["descr"]
        speed = item["l1PhysIf"]["attributes"]["speed"]
        mtu = item["l1PhysIf"]["attributes"]["mtu"]
        print("{:<50} {:<20} {:<8} {:<8}".format(dn, desc, speed, mtu))
