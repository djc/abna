from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import *
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
import requests

BASE = 'https://www.abnamro.nl'
START = BASE + '/portalserver/mijn-abnamro/mijn-overzicht/overzicht/index.html'
SERVICE_VERSION = {'x-aab-serviceversion': 'v3'}

class Session(object):
    def __init__(self, iban):
        self.iban = iban
        self.session = requests.Session()

    def login(self, card, token):
        card = int(card)
        token = str(token)

        self.session.get(START)
        rsp = self.session.get(BASE + '/session/loginchallenge', params={
            'accessToolUsage': 'SOFTTOKEN',
            'accountNumber': self.iban[8:],
            'appId': 'SIMPLE_BANKING',
            'cardNumber': card,
        })

        challenge = rsp.json()['loginChallenge']
        response = calculate_response(challenge['challenge'], challenge['userId'], token)
        payload = {
            'accountNumber': int(self.iban[8:]),
            'cardNumber': card,
            'accessToolUsage': 'SOFTTOKEN',
            'appId': 'SIMPLE_BANKING',
            'response': response,
        }
        for k in {'challengeHandle', 'challengeDeviceDetails'}:
            payload[k] = challenge[k]

        url = BASE + '/session/loginresponse'
        rsp = self.session.put(url, json=payload, headers=SERVICE_VERSION)
        if not rsp.ok:
            raise Exception(rsp.text)

    def mutations(self, last_key=None):
        params = {
            'accountNumber': self.iban,
            'includeActions': 'EXTENDED',
        }
        if last_key is not None:
            params['lastMutationKey'] = last_key

        url = BASE + '/mutations/' + self.iban
        rsp = self.session.get(url, headers=SERVICE_VERSION, params=params)
        return rsp.json()

def calculate_response(challenge, user_id, password):
    obj = decode(challenge)
    out = {
        1: [49],
        2: obj[2],
        3: obj[3],
        8: [ord(c) for c in user_id],
        9: [ord(c) for c in password],
    }
    encoded = encode(out)
    pub_key = RSAPublicNumbers(ba2num(obj[5]), ba2num(obj[4])).public_key(default_backend())
    encrypted = pub_key.encrypt(''.join(chr(i) for i in encoded), PKCS1v15())
    return encrypted.encode('hex')

def ba2num(v):
    res = 0
    size = len(v) - 1
    for (i, v) in enumerate(v):
        res += v << ((size - i) * 8)
    return res

def decode(challenge):
    bytes = [ord(c) for c in challenge.decode('hex')]
    res = {}
    cur = 0
    while cur < len(bytes):
        key = bytes[cur]
        size = (bytes[cur + 1] << 8) + bytes[cur + 2]
        res[key] = bytes[cur + 3:cur + 3 + size]
        cur += 3 + size
    return res

def encode(obj):
    res = []
    for k, v in sorted(obj.iteritems()):
        res.append(k)
        res.append((len(v) >> 8) & 255)
        res.append(len(v) & 255)
        res += v
    res += [0, 0, 0]
    return res
