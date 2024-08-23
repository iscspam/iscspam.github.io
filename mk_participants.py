#!/usr/bin/env python

with open("nomi.txt", "rt") as fh:
    lines = [l.strip() for l in fh if l.strip()]

participants, affiliations = [], []
while lines:
    participants.append(lines.pop(0))
    affiliations.append(lines.pop(0))

rows = list(zip(participants, affiliations))
# sort by first name
rows = sorted(rows, key=lambda t: t[0].split()[0])
#print(rows)


header = """
<!doctype html>
<html>

<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=0.4">
<title>ISCSP&amp;AM 2024 (Participants)</title>
<link href="css/style.css" rel="stylesheet" type="text/css">
<script class="include" type="text/javascript" src="scripts/w3data.js"></script>

<style>
#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>

<body>
  <div w3-include-html="header.html"></div>
  <div class="text">
    <h1>Participants</h1>
    <table align="center" id="customers">
  <tr>
    <th>Participant</th>
    <th>Affiliation</th>
  </tr>
"""

body = []
for participant, affiliation in rows:
    s = f"""
<tr>
<td> {participant} </td>
<td> {affiliation} </td>
</tr>
"""
    body.append(s)

body = "\n".join(body)

footer = """
    </table>
  </div>
</body>

<script>
  w3IncludeHTML();
</script>

</html>
"""

html = header + body + footer

with open("participants.html", "wt") as fh:
    fh.write(html)
