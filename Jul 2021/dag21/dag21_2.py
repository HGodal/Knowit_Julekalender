
def parse_data(ordliste, encode_string, tegn_til_tall):
    decoding = dict()
    for line in ordliste:
        encoded = "".join([str(tegn_til_tall[c]) for c in line])
        if encoded in encode_string:
            decoding[encoded] = line
    return decoding


def decode_data(encoded_string, decoding):
    if not encoded_string:
        return ""
    for word in decoding:
        if encoded_string[: len(word)] == word:
            decoded = decoding[word]
            res = decode_data(encoded_string[len(word):], decoding)
            if res is not None:
                return decoded + res
    return None


alfabet = "abcdefghijklmnopqrstuvwxyzæøå"
tegn_til_tall = dict(zip(alfabet, range(1, 30)))

ordliste = open('wordlist.txt').read().splitlines()
encoded_string = (
    "452051451920510572814191151813572091210211251812015161619112520"
    + "91475141221011351923522729182181222718192919149121210211251491919514"
)
decoding = parse_data(ordliste, encoded_string, tegn_til_tall)
print(decode_data(encoded_string, decoding))
