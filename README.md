# Burp Extension-antiCSRF

This is a burp extension to bypass csrf protection when a new csrf token is generated in every request within the Response Headers.

There are cases where a CSRF token is uniquely used in every request and a new token is generated in every response. If the CSRF token is transmitted via the HTTP headers, it is not possible to get this token with the build-in functionality of BurpSuite. The build-in functionality supports the extration of CSRF token from either parameters or cookies. Thus, with this extension we are able to extract the CSRF token from the HTTP headers and update the requests to have a valid CSRF token.

First things first, locate the request that generates the csrf token . Run a macro which gets the initial CSRF token and then create a Session Handling Rule that runs the macro and then executes the antiCSRF extension that you have imported in Burp. This extension will read the macro's response headers and extract the header "CSRF". It will then update the request's header of the initial request with the newly acquired CSRF token.
