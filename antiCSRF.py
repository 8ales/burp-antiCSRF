import re

from burp import IBurpExtender
from burp import ISessionHandlingAction
from burp import IParameter

class BurpExtender(IBurpExtender, ISessionHandlingAction):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName('Anti-CSRF')
        callbacks.registerSessionHandlingAction(self)

    def getActionName(self):
        return 'Anti-CSRF'

    def performAction(self, currentRequest, macroItems):
        macroResponse = macroItems[0].getResponse()
        marcoInfo = self._helpers.analyzeRequest(macroResponse)
        macroheaders = marcoInfo.getHeaders()
        macroHeadersWithCSRF = list(macroheaders)
        requestInfo = self._helpers.analyzeRequest(currentRequest)
        headers = requestInfo.getHeaders()
        oldHeaders = list(headers)
        bodyBytes = currentRequest.getRequest()[requestInfo.getBodyOffset():]
        bodyStr = self._helpers.bytesToString(bodyBytes)
        for header in oldHeaders:
            if header.startswith('CSRF'):
                testHeaders = requestInfo.getHeaders()
                newHeaders = list(testHeaders)
                for arg in newHeaders:
                    if arg.startswith('CSRF'):
                        for arg1 in macroHeadersWithCSRF:
                            if arg1.startswith('CSRF'):
                                newHeaders[newHeaders.index(arg)]=arg.split(' ')[0]+' '+arg1.split('"')[3]
        httpMessage = self._helpers.buildHttpMessage(newHeaders, bodyStr)
        currentRequest.setRequest(httpMessage)