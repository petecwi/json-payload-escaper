from burp import IBurpExtender, IIntruderPayloadProcessor
import json

class BurpExtender(IBurpExtender, IIntruderPayloadProcessor):
    def registerExtenderCallbacks(self, callbacks):
        # Keep a reference to our callbacks object
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Set our extension name
        callbacks.setExtensionName("JSON Payload Escaper")
        
        # Register ourselves as an Intruder payload processor
        callbacks.registerIntruderPayloadProcessor(self)
    
    def getProcessorName(self):
        # Return the name of our processor
        return "JSON Payload Escaper"
    
    def processPayload(self, currentPayload, originalPayload, baseValue):
        # Convert the current payload to a string
        payload = self._helpers.bytesToString(currentPayload)
        
        # Escape the payload for JSON
        escapedPayload = self.escapeJson(payload)
        
        # Return the escaped payload as a byte array
        return self._helpers.stringToBytes(escapedPayload)
    
    def escapeJson(self, payload):
        # Use Python's JSON library to escape the payload
        return json.dumps(payload)[1:-1]

