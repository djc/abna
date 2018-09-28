# ABN Amro mutations retrieval

This Python library enables retrieval of mutations from the Dutch ABN Amro
banking site using the "soft token" (5-digit pass code).

Requirements:

- Python 2.7 or 3 (tested with 3.5)
- requests (tested with 2.15.1)
- cryptography (tested with 1.4)

This library was created by and is maintained by Dirkjan Ochtman. If you are
in a position to support ongoing maintenance and further development or use it
in a for-profit context, please consider supporting my open source work on
[Patreon](https://www.patreon.com/dochtman).

## Example

Here is a minimal example demonstrating how to use the library:

```python
import abna, json

sess = abna.Session('NL01ABNA0123456789')
sess.login(123, '12345')
print(json.dumps(sess.mutations('NL01ABNA0123456789'), indent=2))
```

## Change log

### 0.2 (2018-07-15)

- Allow retrieval of mutations from different accounts
  ([#1](https://github.com/djc/abna/pull/1), thanks to
  [@ivasic](https://github.com/ivasic)). Note that this changes the signature
  of the `Session.mutations()` method to take the account IBAN as a mandatory
  first argument.

## Alternatives

[abnamro-tx](https://github.com/mkrcah/abnamro-tx) is a docker-based solution
to run a headless Chrome instance that can download mutation files for you.
