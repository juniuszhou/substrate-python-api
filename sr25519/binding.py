from ctypes import *
import ctypes
import random

so_path = '/home/junius/code/src/github.com/juniuszhou/sr25519-crust/build/release/libsr25519crust.so'
dummy_keypair = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dummy_public_key = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
dummy_signature = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# SR25519_CHAINCODE_SIZE 32
# SR25519_KEYPAIR_SIZE 96
# SR25519_PUBLIC_SIZE 32
# SR25519_SECRET_SIZE 64
# SR25519_SEED_SIZE 32
# SR25519_SIGNATURE_SIZE 64
# SR25519_VRF_OUTPUT_SIZE 32
# SR25519_VRF_PROOF_SIZE 64

class Sr25519:
    def __init__(self):
        self.lib = cdll.LoadLibrary(so_path)

    # /**
    #  * Perform a derivation on a secret
    #  *  keypair_out: pre-allocated output buffer of SR25519_KEYPAIR_SIZE bytes
    #  *  pair_ptr: existing keypair - input buffer of SR25519_KEYPAIR_SIZE bytes
    #  *  cc_ptr: chaincode - input buffer of SR25519_CHAINCODE_SIZE bytes
    #  */
    def sr25519_derive_keypair_hard(self, key_pair, chain_code):
        output = ctypes.c_char_p()
        output.value = dummy_keypair
        self.lib.sr25519_derive_keypair_hard(output, key_pair, chain_code)
        return output.value

    # /**
    #  * Perform a derivation on a secret
    #  *  keypair_out: pre-allocated output buffer of SR25519_KEYPAIR_SIZE bytes
    #  *  pair_ptr: existing keypair - input buffer of SR25519_KEYPAIR_SIZE bytes
    #  *  cc_ptr: chaincode - input buffer of SR25519_CHAINCODE_SIZE bytes
    #  */
    def sr25519_derive_keypair_soft(self, key_pair, chain_code):
        output = ctypes.c_char_p()
        output.value = dummy_keypair
        self.lib.sr25519_derive_keypair_soft(output, key_pair, chain_code)
        return output.value

    # /**
    #  * Perform a derivation on a publicKey
    #  *  pubkey_out: pre-allocated output buffer of SR25519_PUBLIC_SIZE bytes
    #  *  public_ptr: public key - input buffer of SR25519_PUBLIC_SIZE bytes
    #  *  cc_ptr: chaincode - input buffer of SR25519_CHAINCODE_SIZE bytes
    #  */
    def sr25519_derive_public_soft(self, key_pair, chain_code):
            output = ctypes.c_char_p()
            output.value = dummy_public_key
            self.lib.sr25519_derive_public_soft(output, key_pair, chain_code)
            return output.value

    # /**
    #  * Generate a key pair.
    #  *  keypair_out: keypair [32b key | 32b nonce | 32b public], pre-allocated output buffer of SR25519_KEYPAIR_SIZE bytes
    #  *  seed: generation seed - input buffer of SR25519_SEED_SIZE bytes
    #  */
    def sr25519_keypair_from_seed(self, seed):
        output = ctypes.c_char_p()
        output.value = dummy_keypair
        self.lib.sr25519_keypair_from_seed(output, seed)
        return output.value

    # /**
    #  * Sign a message
    #  * The combination of both public and private key must be provided.
    #  * This is effectively equivalent to a keypair.
    #  *  signature_out: output buffer of ED25519_SIGNATURE_SIZE bytes
    #  *  public_ptr: public key - input buffer of SR25519_PUBLIC_SIZE bytes
    #  *  secret_ptr: private key (secret) - input buffer of SR25519_SECRET_SIZE bytes
    #  *  message_ptr: Arbitrary message; input buffer of size message_length
    #  *  message_length: Length of a message
    #  */
    def sr25519_sign(self, public_key, private_key, message, message_length):
        output = ctypes.c_char_p()
        output.value = dummy_signature
        self.lib.sr25519_sign(output, private_key, message, message_length)
        return output.value

    # /**
    #  * Verify a message and its corresponding against a public key;
    #  *  signature_ptr: verify this signature
    #  *  message_ptr: Arbitrary message; input buffer of message_length bytes
    #  *  message_length: Message size
    #  *  public_ptr: verify with this public key; input buffer of SR25519_PUBLIC_SIZE bytes
    #  *  returned true if signature is valid, false otherwise
    #  */
    def sr25519_verify(self, signature, message, message_length, public_key):
        result = self.lib.sr25519_sign(signature, message, message_length, public_key)
        return result

    # /**
    #  * Sign the provided message using a Verifiable Random Function and
    #  * if the result is less than \param limit provide the proof
    #  * @param out_and_proof_ptr pointer to output array, where the VRF out and proof will be written
    #  * @param keypair_ptr byte representation of the keypair that will be used during signing
    #  * @param message_ptr byte array to be signed
    #  * @param limit_ptr byte array, must be 32 bytes long
    #  */
    def sr25519_vrf_sign_if_less(self, keypair, message, message_length, limit):
        output = ctypes.c_char_p()
        output.value = dummy_public_key
        self.lib.sr25519_vrf_sign_if_less(output, keypair, message, message_length, limit)
        return output.value

    # /**
    #  * Verify a signature produced by a VRF with its original input and the corresponding proof
    #  * @param public_key_ptr byte representation of the public key that was used to sign the message
    #  * @param message_ptr the orignal signed message
    #  * @param output_ptr the signature
    #  * @param proof_ptr the proof of the signature
    #  */
    def sr25519_vrf_verify(const uint8_t *public_key_ptr,
                                          const uint8_t *message_ptr,
                                          unsigned long message_length,
                                          const uint8_t *output_ptr,
                                          const uint8_t *proof_ptr)
        output = ctypes.c_char_p()
        output.value = dummy_public_key
        self.lib.sr25519_vrf_sign_if_less(output, keypair, message, message_length, limit)
        return output.value



