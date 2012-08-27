RomanNumerals
=============

Decimal and Roman Numeral Converter

This converts modern roman numerals to integers and integers to
modern roman numerals.

This does not make use of the overbar or pipe symbol to indicate 
multiplication by 1,000 or 100 and therefor the largest number 
that can be represented is:

MMMCMXCIX or 3,999

Command Line Installation
=========================

Download the tar or clone the git repo, then run.

    $ python setup.py install

Or via pip.
    
    $ pip install git+git://github.com/tmackenzie/roman.git

pip through requirements.txt
============================

    Add the following to your requirements.txt.

    git+git://github.com/tmackenzie/roman.git

    $ pip install -r requirements.txt

Running Tests
=============

    $ python tests/roman_tests.py
