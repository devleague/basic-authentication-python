# Basic Authentication Python for Wireshark
Simple Python Flask server with a single unsecured `/login` route implementing Basic Authentication for testing with Wireshark and sniffing HTTP headers.

#### Setup
1. `git clone https://github.com/devleague/basic-authentication-python`
1. `pip install -r requirements.txt`
1. `python http-auth-demo.py`
1. Visit `http://xxx.xxx.xxx.xxx:5000/login` (replace xxx with your IP)

#### Customization
If you want to customize IP address and port number modify the `app.run` statement with the following settings:

`app.run(host='xx.xx.xx.xx', 80)`

#### Analysis
Packets should be capturable and HTTP Authorization headers visible in plain text.
