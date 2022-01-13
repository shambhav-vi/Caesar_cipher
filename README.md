# Caesar_cipher

The idea of the Caesar Cipher is to pick a key (integer) and shift every letter of message by that integer. In other words, suppose the shift is k . Then, all instances of the i-th letter of the alphabet that appear in the plaintext should become the (i + k)-th letter of the alphabet in the ciphertext. In case of i + k > 26 (the length of the alphabet)
we take modulus of i + k w.r.t 26 ( i.e (i + k) % 26 ). <br />
**Numbers and symbols remain unaffected.**

| Plain Text | shift key | Cipher Text  | 
| -----------| ----------| ------------ |
| abcdef     |    3      | defghi       |
| zombie     |    2      | bqodkg       |
| "91 days"  |    8      | "91 liga"    |

In case of decryption, all instances of the i-th letter of the alphabet that appear in the ciphertext should become the (i - k)-th letter of the alphabet in the plaintext.

| Cipher Text | shift key | Plain Text  | 
| ------------|-----------| ------------|
|  wgwia      |    4      | akame       |

