# Burp Extension-antiCSRF

This is a burp extension to bypass csrf protection when the csrf token is within the Response Headers. 
Run a macro which gets the initial CSRF token and then create a Session Handling Rule that runs the macro and then executes the antiCSRF extention that you have imported in Burp
