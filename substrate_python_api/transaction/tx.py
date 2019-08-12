
constructor (data) {
		super('author_submitAndWatchExtrinsic', ['0x' + bytesToHex(data)], null, {sending: true})
	}



## code copy from js. how to build a tx.
composeTransaction(sender, call, index, era, checkpoint, senderAccount, compact)
{
return new
Promise((resolve, reject) = > {
if (typeof sender == 'string')
{
    sender = ss58Decode(sender)
}
if (sender instanceof Uint8Array & & sender.length == 32) {
senderAccount = sender
} else if (!senderAccount) {
reject(`Invalid senderAccount when sender is account index`)
}
console.log("composing transaction", senderAccount, index, call, era, checkpoint);
let e = encode([
index, call, era, checkpoint
], [
'Compact<Index>', 'Call', 'TransactionEra', 'Hash'
])

let legacy = runtime.version.isReady() & & (
runtime.version._value.specName == 'node' & & runtime.version._value.specVersion < 17
| | runtime.version._value.specName == 'polkadot' & & runtime.version._value.specVersion < 107
)
if (!legacy & & e.length > 256) {
console.log(`Oversize transaction (length ${e.length} bytes).Hashing.`)
e = blake2b(e, null, 32)
}

let signature = secretStore().sign(senderAccount, e)
console.log("encoding transaction", sender, index, era, call);
let signedData = encode(encode({
_type: 'Transaction',
       version: 0x81,
sender,
signature,
index,
era,
call
}), 'Vec<u8>')
console.log("signed:", bytesToHex(signedData))
setTimeout(() = > resolve(signedData), 1000)
})
}



void CPolkaApi::signAndSendTransfer(string sender, string privateKey, string recipient, unsigned __int128 amount,
                                    std::function<void(string)> callback) {

    _logger->info("=== Starting a Transfer Extrinsic ===");

    // Get account Nonce
    unsigned long nonce = getAccountNonce(sender);
    _logger->info(string("sender nonce: ") + to_string(nonce));

    // Format transaction
    TransferExtrinsic te;
    memset(&te, 0, sizeof(te));
    te.method.moduleIndex = _protocolPrm.BalanceModuleIndex;
    te.method.methodIndex = _protocolPrm.TransferMethodIndex;
    auto recipientPK = AddressUtils::getPublicKeyFromAddr(recipient);
    memcpy(te.method.receiverPublicKey, recipientPK.bytes, PUBLIC_KEY_LENGTH);
    te.method.amount = amount;
    te.signature.version = SIGNATURE_VERSION;
    auto senderPK = AddressUtils::getPublicKeyFromAddr(sender);
    memcpy(te.signature.signerPublicKey, senderPK.bytes, PUBLIC_KEY_LENGTH);
    te.signature.nonce = nonce;
    te.signature.era = IMMORTAL_ERA;

    // Format signature payload
    SignaturePayload sp;
    sp.nonce = nonce;
    uint8_t methodBytes[MAX_METHOD_BYTES_SZ];
    sp.methodBytesLength = te.serializeMethodBinary(methodBytes);
    sp.methodBytes = methodBytes;
    sp.era = IMMORTAL_ERA;
    memcpy(sp.authoringBlockHash, _protocolPrm.GenesisBlockHash, BLOCK_HASH_SIZE);

    // Serialize and Sign payload
    uint8_t signaturePayloadBytes[MAX_METHOD_BYTES_SZ];
    long payloadLength = sp.serializeBinary(signaturePayloadBytes);

    vector<uint8_t> secretKeyVec = fromHex<vector<uint8_t>>(privateKey);
    uint8_t sig[SR25519_SIGNATURE_SIZE] = {0};
    sr25519_sign(sig, te.signature.signerPublicKey, secretKeyVec.data(), signaturePayloadBytes, payloadLength);

    // Copy signature bytes to transaction
    memcpy(te.signature.sr25519Signature, sig, SR25519_SIGNATURE_SIZE);

    // Serialize and send transaction
    uint8_t teBytes[MAX_METHOD_BYTES_SZ];
    long teByteLength = te.serializeBinary(teBytes);
    string teStr("0x");
    for (int i = 0; i < teByteLength; ++i) {
        char b[3] = {0};
        sprintf(b, "%02X", teBytes[i]);
        teStr += b;
    }

    Json query = Json::object{{"method", "author_submitAndWatchExtrinsic"}, {"params", Json::array{teStr}}};

    // Send == Subscribe callback to completion
    _transactionCompletionSubscriber = callback;
    _transactionCompletionSubscriptionId = _jsonRpc->subscribeWs(query, this);
}