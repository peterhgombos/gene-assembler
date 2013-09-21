import sys
import glob
from assembler import assemble


def main():

    if len(sys.argv) == 1:
        print "USAGE: gene-as [-d] source.gas [source2.gas ...]"
        return

    debug = '-d' in sys.argv

    paths = filter(lambda x: x[0] != '-',
                   [item for sublist in map(glob.glob, sys.argv[1:])
                    for item in sublist])

    for path in paths:
        with open(path, 'r') as f:
            assembly = [line for line in f]
        assembled = assemble(assembly)

        address = 0
        binary = []
        for line in assembled:
            binary.append(line.toBinary())
            if debug:
                print 'Address: %s' % address
                print 'text: ' + str(line)
                print line.toBinary(debug=debug)
                print
            address += 1

        binary = ''.join(binary)

        with open(path + '.out', 'w') as f:
            f.write(
                ''.join(
                    [chr(int('0b'+binary[i:i+8], 2))
                        for i in range(0, len(binary), 8)]
                )
            )


if __name__ == '__main__':
    main()
