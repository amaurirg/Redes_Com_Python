#!/usr/bin/env python3
# Decodificando bytes de entrada e codificando caracteres paa saída

if __name__ == '__main__':
    # Conversão de bytes do ambiente externo em caracteres Unicode
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_caracters = input_bytes.decode('utf-16')
    print(input_caracters)
    print(repr(input_caracters))

    # Conversão de caracteres em bytes antes do envio
    output_caracters = 'We copy you down, Eagle.\n'
    output_bytes = output_caracters.encode('utf-8')
    with open('eagle.txt', 'wb') as f:
        f.write(output_bytes)
