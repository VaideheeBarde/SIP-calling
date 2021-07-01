# SIP-calling
Calling using SIP and X-lite Softphone

The objective of this project is to learn the implementation of VOIP using SIP connections through hands on experiment on adhoc networks. The learning process is carried out by utilizing a server and a few VOIP users as clients. 
Initially, we created a proxy server by installing the Asterisk Win 32 software on our Windows laptop.
Client connection takes place by connecting all the clients to the adhoc network and developing a python code to implement the client side application with basic SIP functionalities in  4 phases. We just replicated various requests and  responses associated with various scenarios in SIP.
4 phases of code implementation:
Call establishment
When users in the same domain make the call, they are subscribed to the same ISP i.e. they are in the same domain.
When two callers are in the different domain, redirect servers are required. Else, we do not need redirect servers.
When powered up, A and B register their availability and IP addresses with the SIP proxy server in the ISP’s network.
A initiates the call. 
A tells the proxy server that he/she wants to contact user B.
SIP proxy server then finds user B’s IP address from the SIP registration server.
SIP Proxy server uses medium or media that user A wants to use. Thus, it relays user A’s invitation to communicate with user B.
User B informs the SIP proxy server that user A’s invitation is acceptable and that user A is ready to communicate.
SIP proxy server communicates this to user A and a SIP session is established.
The users then create point-to-point RTP connection enabling interaction
Call busy
In this part of the experiment, we make one user busy while the other user tries to call it through the server, and we want to analyze the SIP messages exchanged. We can use this application in case of timeouts or invalid conditions. 
Call hold
In this part of the experiment, user C tries to call user B when user A and B are already on a call.
Thus, when C calls B, B keeps A on hold. After completing the call with user C, it resumes call with A.
Call conferencing
Mixing can take place in one of the participating end systems instead of the server.
In call conferencing, if A and B are in a call, they can also invite C. 
B and C do not need to be aware of the service performed by A but can also mix other participants from C.
The adhoc gives rise to additional delays on some of the media paths.
Also, conference dissolves when other participant who is acting as a mixer leaves the conference.
