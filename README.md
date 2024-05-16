# json-payload-escaper
A Burp Suite extension to escape JSON payloads.

**## Usage**

**Open Burp Suite:**
- Go to the "Extender" tab.
- Click on the "Extensions" sub-tab.
- Click "Add".
- Select "Python" as the extension type.
- Browse to and select the Python file from this repository.

**Setup Intruder:**
- Go to the "Intruder" tab.
- Configure your target and set payload positions.
- Navigate to the "Payloads" tab.
- Choose your payload set and add the payloads you want to test.

**Add Payload Processing Rule:**
- In the "Payloads" tab, find the "Payload Processing" section.
- Click "Add" to create a new payload processing rule.
- In the "Add payload processing rule" dialog box set the "Enter the details of the payload processing rule" field to "Invoke Burp extension".
- In the "Select processor" dropdown, choose "JSON Payload Escaper".
- Click "OK" to add the rule.

**Run the Attack:**
- After configuring your payloads and adding the JSON escaping processor, proceed to run the Intruder attack.
- The extension will process each payload by escaping it for JSON compatibility before sending the requests.

## License

This project is licensed under the MIT License.
