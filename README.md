# Basic Authentication Python for Wireshark
Simple Python Flask server with a single unsecured `/login` route implementing Basic Authentication for testing with Wireshark and sniffing HTTP headers.

#### Setup
1. `git clone https://github.com/devleague/basic-authentication-python`
1. `python http-auth-demo.py`
1. Visit `http://xxx.xxx.xxx.xxx/login` (replace xxx with your IP)

Packets should be capturable and HTTP Authorization headers visible in plain text.
