## https://github.com/paritytech/parity-scale-codec

For storage values:
xxhash128(bytes("ModuleName" + " " + "StorageItem"))
For storage maps:
blake256hash(bytes("ModuleName" + " " + "StorageItem") + bytes(scale("StorageItemKey")))
For storage double maps:
blake256hash(bytes("ModuleName" + " " + "StorageItem") + bytes(scale("FirstStorageItemKey")))
+ blake256hash(bytes(scale("SecondStorageItemKey")))


