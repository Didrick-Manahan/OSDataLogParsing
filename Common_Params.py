# "regex":"token" formatted common parameters
common_params = {
    r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b" : "<IP>",
    r"(?<=[ =])(/[^/ ]+)+/?" : "<FILEPATH>",
    r"\b(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)\b" : "<URL>",
    r"\b(2[0-3]|[01]?[0-9]):([0-5]?[0-9]):([0-5]?[0-9])\b" : "<TIME>",
    r"\b(1[0-2]|0?[1-9]):([0-5]?[0-9]):([0-5]?[0-9])(●?[AP]M)?\b" : "<TIME>",
    r"\b(2[0-3]|[01]?[0-9]):([0-5]?[0-9])\b" : "<TIME>",
    r"\b(1[0-2]|0?[1-9]):([0-5]?[0-9])(●?[AP]M)?\b" : "<TIME>",
    r"\b(?:(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])|(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9]))/(?:[0-9]{2})?[0-9]{2}\b" : "<DATE>",
    r"\b[0-9]+\.[0-9]+\b" : "<DECIMAL>",
    r"\b[0-9]+\b" : "<INTEGER>",
    r"\b(0x|0X)?[a-fA-F0-9]+\b" : "<HEX>"
}
# matches = re.findall(r"\[\s*(\d+/\D+/.*?)\]", text)