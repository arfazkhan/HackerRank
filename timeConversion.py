def timeConversion(s):
    if s[-2:].lower() == 'pm':
        hours = (int(s[:2]) + 12) % 24
    else:
        hours = int(s[:2]) % 12

    return f"{hours:02d}{s[2:8]}"