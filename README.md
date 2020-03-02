# rtmp-config-tool

**Project Overview**
This project was created to solve the need to modify the RTMP servers stream keys. The RTMP server required ssh and manual configuration each time a stream key would change. And in January 2020 Facebook required streams move to 'RTMPS'. The rtmp module for Nginx I am using doesn't support rtmps, so I proxied the stream with SSL using stunnel4. The proxy server does timeout if the stream isn't being used so I also added a option to restart stunnel and Nginx if needed.

**Tools**

- Built with Python
- Using paramiko for ssh and sftp

**How to Use**

- On line 42 the strings: 'SERVER IP', 'USERNAME', and 'PASSWORD' need to be replaced with their respective information.
- I build this tool into an .exe using pyinstaller and couldn't use environmental variables with the builder. So there is commented out instructions for using environmental variables in a local environment. To keep my information safe on GitHub I just discluded the actual values.
