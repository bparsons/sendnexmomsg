# Send Message via Nexmo

A python script to send a message via Nexmo API. You must have a Nexmo account to use this script. 

I use this as an alert script for Zabbix. 

## Requirements

* A Nexmo account http://www.nexmo.com
* libpynexmo - https://github.com/marcuz/libpynexmo

## Configuration

Edit the script to set up your credentials:

* nexmouser - Your Nexmo API user name
* nexmopass - Your Nexmo API password
* nexmosendnumber - Your Nexmo sending number

## Usage

    $ ./sendnexmomsg.py <number> <message>

