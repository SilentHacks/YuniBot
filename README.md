# YuniBot

YuniBot is a Discord bot that gives users an on/off campus role, depending on where they should be according to their personal timetable.

## Installation

Pip install the requirements.txt. 
You also need an SSL certificate which you can self-sign with something like this:

```bash
pip install -r requirements.txt
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout domain_srv.key -out domain_srv.crt
```

## Usage

```bash
python bot.py
```

## Contributing
Feel free to make a PR if there's something that you think needs changing.
