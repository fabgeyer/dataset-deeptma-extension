#!/usr/bin/env python3

import pbzlib
import argparse


def main(filename):
    # Open a .pbz file containing the networks
    for network in pbzlib.open_pbz(filename):
        # Print all the servers of the network
        for server in network.server:
            print(server)

        # Print all the flows in the network
        for flow in network.flow:
            print(flow)

        # Stop the loop to only display the first network
        break


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("input")
    args = p.parse_args()
    main(args.input)
