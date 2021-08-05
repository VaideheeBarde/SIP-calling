# SIP-calling
Calling using SIP and X-lite Softphone

1.) Goal - The objective of this project is to learn the implementation of VOIP using SIP connections through hands on experiment on adhoc networks.

2.) Technologies used -
- X-lite Softphone
- Asterisk Win 32 on Windows OS (Installation was very smooth on Windows)
- Generation of Adhoc network using Python for client connection and call instantiation
3.) Process flow -
Basic SIP functionality is implemented in 4 phases. The requests and responses associated with various scenarios in SIP.

4 phases of code implementation:
- Call establishment -
Two callers in same domain are subscribed to the same ISP. Two callers in different domains, redirect servers are required. 

- Call flow -
User A and B are powered up, A and B register their availabilities and IP addresses with SIP proxy server in the ISP's network.
User A -> instantiates call and routes the request to the SIP proxy server -> SIP proxy server finds user B's IP address from the SIP registration server -> User B informs SIP proxy server that User A's invitation is acceptable and that User A is ready to communicate -> SIP proxy server communicates User B's message to User A -> point-to-point RTP connection established

- Call busy
In this part of the experiment, we make one user busy while the other user tries to call it through the server, and we want to analyze the SIP messages exchanged. We can use this application in case of timeouts or invalid conditions.

- Call hold
User C tries to call user B when user A and B are already on a call. Thus, when C calls B, B keeps A on hold. After completing the call with user C, it resumes call with A.

- Call conferencing / Mixing
Mixing can take place in one of the participating end systems instead of the server. In call conferencing, if A and B are in a call, they can also invite C. The adhoc gives rise to additional delays on some of the media paths. Also, conference dissolves when other participant who is acting as a mixer leaves the conference.
