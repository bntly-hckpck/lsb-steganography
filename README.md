# lsb-steganography
Hide secret messages within images by using LSB manipulation.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

- [X] Convert text to binary (characters -> ASCII -> 8-bit binary strings)
- [x] LSB modification without visual impact (3 bits per pixel, rgb)
- [x] Append delimiter for decoding
- [x] Remove alpha channel to ensure 3-channel compatibility
- [ ] Decoder
- [ ] Error handling
- [ ] CLI instead of hardcode
- [ ] *TBD*

## About

This is a personal project in which I'm implementing the Least Significant Bit steganography for learning purposes. It is not intended for production or security-critical applications.

### Encoder

See [`encoder.py`](encoder.py) for the current implementation.

### Decoder

(*TBD*)
