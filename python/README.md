# detahardlib

[![repology](https://repology.org/badge/tiny-repos/python:detahard.svg)](https://repology.org/metapackage/python:detahard) [![image](https://badges.gitter.im/detahard/community.svg)](https://gitter.im/detahard/community)

Python library and command-line client for communicating with detahard
Hardware Wallet.

See <https://detahard.io> for more information.

## Install

Python detahard tools require Python 3.6 or higher, and libusb 1.0. The easiest
way to install it is with `pip`. The rest of this guide assumes you have
a working `pip`; if not, you can refer to [this
guide](https://packaging.python.org/tutorials/installing-packages/).

On a typical system, you already have all you need. Install `detahard` with:

```sh
pip3 install detahard
```

On Windows, you also need to either install [detahard Bridge](https://suite.detahard.io/web/bridge/), or
[libusb](https://github.com/libusb/libusb/wiki/Windows) and the appropriate
[drivers](https://zadig.akeo.ie/).

### Firmware version requirements

Current detahardlib version supports detahard One version 1.8.0 and up, and detahard T version
2.1.0 and up.

For firmware versions below 1.8.0 and 2.1.0 respectively, the only supported operation
is "upgrade firmware".

detahard One with firmware _older than 1.7.0_ and bootloader _older than 1.6.0_
(including pre-2021 fresh-out-of-the-box units) will not be recognized, unless
you install HIDAPI support (see below).

### Installation options

* **Ethereum**: To support Ethereum signing from command line, additional packages are
  needed. Install with:

  ```sh
  pip3 install detahard[ethereum]
  ```

* **Stellar**: To support Stellar signing from command line, additional packages are
  needed. Install with:

  ```sh
  pip3 install detahard[stellar]
  ```

* **Firmware-less detahard One**: If you are setting up a brand new detahard One
  manufactured before 2021 (with pre-installed bootloader older than 1.6.0), you will
  need HIDAPI support. On Linux, you will need the following packages (or their
  equivalents) as prerequisites: `python3-dev`, `cython3`, `libusb-1.0-0-dev`,
  `libudev-dev`.

  Install with:

  ```sh
  pip3 install detahard[hidapi]
  ```

To install all three, use `pip3 install detahard[hidapi,ethereum,stellar]`.

### Distro packages

Check out [Repology](https://repology.org/metapackage/python:detahard) to see if your
operating system has an up-to-date python-detahard package.

### Installing latest version from GitHub

```sh
pip3 install "git+https://github.com/detahard/detahard-firmware#egg=detahard&subdirectory=python"
```

### Running from source

Install the [Poetry](https://python-poetry.org/) tool, checkout
`detahard-firmware` from git, and enter the poetry shell:

```sh
pip3 install poetry
git clone https://github.com/detahard/detahard-firmware
cd detahard-firmware
poetry install
poetry shell
```

In this environment, detahardlib and the `detahardctl` tool is running from the live
sources, so your changes are immediately effective.

## Command line client (detahardctl)

The included `detahardctl` python script can perform various tasks such as
changing setting in the detahard, signing transactions, retrieving account
info and addresses. See the
[python/docs/](https://github.com/detahard/detahard-firmware/tree/master/python/docs)
sub folder for detailed examples and options.

NOTE: An older version of the `detahardctl` command is [available for
Debian Stretch](https://packages.debian.org/en/stretch/python-detahard)
(and comes pre-installed on [Tails OS](https://tails.boum.org/)).

## Python Library

You can use this python library to interact with a detahard and use its capabilities in
your application. See examples here in the
[tools/](https://github.com/detahard/detahard-firmware/tree/master/python/docs/tools)
sub folder.

## PIN Entering

When you are asked for PIN, you have to enter scrambled PIN. Follow the
numbers shown on detahard display and enter the their positions using the
numeric keyboard mapping:

|   |   |   |
|---|---|---|
| 7 | 8 | 9 |
| 4 | 5 | 6 |
| 1 | 2 | 3 |

Example: your PIN is **1234** and detahard is displaying the following:

|   |   |   |
|---|---|---|
| 2 | 8 | 3 |
| 5 | 4 | 6 |
| 7 | 9 | 1 |

You have to enter: **3795**

## Contributing

If you want to change protobuf or coin definitions, you will need to regenerate
definitions in the `python/` subdirectory.

First, make sure your submodules are up-to-date with:

```sh
git submodule update --init --recursive
```

Then, rebuild the protobuf messages by running, from the `detahard-firmware` top-level
directory:

```sh
make gen
```

To get support for BTC-like coins, these steps are enough and no further
changes to the library are necessary.
