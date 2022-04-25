# Gen AD review of draft-ietf-bmwg-ngfw-performance-13

CC @larseggert

Thanks to Matt Joras for the General Area Review Team (Gen-ART) review
(https://mailarchive.ietf.org/arch/msg/gen-art/NUycZt5uKAZejOvCr6tdi_7SvPA).

## Discuss

### Paragraph 2

This document needs TSV and ART people to help with straightening out a
lot of issues related to TCP, TLS, and H1/2/3. Large parts of the document don't
correctly reflect the complex realities of what "HTTP" is these days (i.e., that
we have H1 and H2 over either TCP or TLS, and H3 over only QUIC.) The document
is also giving unnecessarily detailed behavioral descriptions of TCP and its
parameters, while at the same time not being detailed enough about TLS, H2 and
esp. QUIC/H3. It feel like this stared out as an H1/TCP document that was then
incompletely extended to H2/H3.

### Section 4.3.1.1, paragraph 1
```
     The TCP stack SHOULD use a congestion control algorithm at client and
     server endpoints.  The IPv4 and IPv6 Maximum Segment Size (MSS)
     SHOULD be set to 1460 bytes and 1440 bytes respectively and a TX and
     RX initial receive windows of 64 KByte.  Client initial congestion
     window SHOULD NOT exceed 10 times the MSS.  Delayed ACKs are
     permitted and the maximum client delayed ACK SHOULD NOT exceed 10
     times the MSS before a forced ACK.  Up to three retries SHOULD be
     allowed before a timeout event is declared.  All traffic MUST set the
     TCP PSH flag to high.  The source port range SHOULD be in the range
     of 1024 - 65535.  Internal timeout SHOULD be dynamically scalable per
     RFC 793.  The client SHOULD initiate and close TCP connections.  The
     TCP connection MUST be initiated via a TCP three-way handshake (SYN,
     SYN/ACK, ACK), and it MUST be closed via either a TCP three-way close
     (FIN, FIN/ACK, ACK), or a TCP four-way close (FIN, ACK, FIN, ACK).
```
There are a lot of requirements in here that are either no-ops ("SHOULD use a
congestion control algorithm"), nonsensical ("maximum client delayed ACK SHOULD
NOT exceed 10 times the MSS") or under the sole control of the stack. This needs
to be reviewed and corrected by someone who understands TCP.

## Comments

### Section 1, paragraph 1
```
     18 years have passed since IETF recommended test methodology and
     terminology for firewalls initially ([RFC3511]).  The requirements
     for network security element performance and effectiveness have
     increased tremendously since then.  In the eighteen years since
```
These sentences don't age well - rephrase without talking about particular
years?

### Section 4.3.2.3, paragraph 1
```
     The server pool for HTTP SHOULD listen on TCP port 80 and emulate the
     same HTTP version (HTTP 1.1 or HTTP/2 or HTTP/3) and settings chosen
     by the client (emulated web browser).  The Server MUST advertise
```
An H3 server will not listen on TCP port 80. In general, the document needs to
be checked for the implicit assumption that HTTP sues TCP; there is text
throughout that is nonsensical for H3 (like this example).
   The Server MUST advertise

### Section 6.3, paragraph 5
```
        The average number of successfully established TCP connections per
        second between hosts across the DUT/SUT, or between hosts and the
        DUT/SUT.  The TCP connection MUST be initiated via a TCP three-way
        handshake (SYN, SYN/ACK, ACK).  Then the TCP session data is sent.
        The TCP session MUST be closed via either a TCP three-way close
        (FIN, FIN/ACK, ACK), or a TCP four-way close (FIN, ACK, FIN, ACK),
        and MUST NOT by RST.
```
This prohibits TCP fast open, why? Also, wouldn't it be enough to say that the
connection needs to not abnormally reset, rather than describing the TCP packet
sequences that are acceptable? Given that those are not the only possible
sequences, c.f., loss and reordering.

### Section 6.3, paragraph 5
```
        The average number of successfully completed transactions per
        second.  For a particular transaction to be considered successful,
        all data MUST have been transferred in its entirety.  In case of
        HTTP(S) transactions, it MUST have a valid status code (200 OK),
        and the appropriate FIN, FIN/ACK sequence MUST have been
        completed.
```
H3 doesn't do FIN/ACK, etc. See above.

### Section 7.1.3.4, paragraph 3
```
     a.  Number of failed application transactions (receiving any HTTP
         response code other than 200 OK) MUST be less than 0.001% (1 out
         of 100,000 transactions) of total attempted transactions.
  
     b.  Number of Terminated TCP connections due to unexpected TCP RST
         sent by DUT/SUT MUST be less than 0.001% (1 out of 100,000
         connections) of total initiated TCP connections.
```
Why is a 0.001% failure rate deemed acceptable? (Also elsewhere.)

### Section 7.2.1, paragraph 1
```
     Using HTTP traffic, determine the sustainable TCP connection
     establishment rate supported by the DUT/SUT under different
     throughput load conditions.
```
H3 doesn't do TCP.

### Section 7.2.3.2, paragraph 8
```
     The client SHOULD negotiate HTTP and close the connection with FIN
     immediately after completion of one transaction.  In each test
     iteration, client MUST send GET request requesting a fixed HTTP
     response object size.
```
H3 doesn't do TCP FIN.

### Section 7.2.3.3, paragraph 5
```
     c.  During the sustain phase, traffic SHOULD be forwarded at a
         constant rate (considered as a constant rate if any deviation of
         traffic forwarding rate is less than 5%).
```
What does this mean? How would traffic NOT be forwarded at a constant rate?

### Section 7.2.3.3, paragraph 4
```
     d.  Concurrent TCP connections MUST be constant during steady state
         and any deviation of concurrent TCP connections SHOULD be less
         than 10%. This confirms the DUT opens and closes TCP connections
         at approximately the same rate.
```
What does it mean for a TCP connection to be constant?

### Section 7.4.1, paragraph 3
```
     Scenario 1: The client MUST negotiate HTTP and close the connection
     with FIN immediately after completion of a single transaction (GET
     and RESPONSE).
```
H3 sessions don't send TCP FINs. (Also elsewhere.)

### Section 7.7, paragraph 0
```
  7.7.  HTTPS Throughput
```
Is this HTTPS as in H1, H2 or H3? All of the above?

### Boilerplate

Document has Informational status, but uses the RFC2119 keywords "NOT
RECOMMENDED", "SHOULD", "SHALL NOT", "RECOMMENDED", "MUST NOT", "MAY", "MUST
NOT", "REQUIRED", "OPTIONAL", "SHOULD NOT", "MUST", and "SHALL". Check if this
is really necessary?

### Inclusive language

Found terminology that should be reviewed for inclusivity; see
https://www.rfc-editor.org/part2/#inclusive_language for background and more
guidance:

 * Term `dummy`; alternatives might be `placeholder`, `sample`, `stand-in`,
   `substitute`

### IP addresses

Found IP blocks or addresses not inside RFC5737/RFC3849 example ranges:
`2001:2::/48` and `198.18.0.0/15`.

## Nits

All comments below are about very minor potential issues that you may choose to
address in some way - or ignore - as you see fit. Some were flagged by
automated tools (via https://github.com/larseggert/ietf-reviewtool), so there
will likely be some false positives. There is no need to let me know what you
did with these suggestions.

### Typos

#### Section 4.3.2.3, paragraph 1
```
-    by the client (emulated web browser).  The Server MUST advertise
-                                         ---------------------------
```

### Grammar/style

#### Paragraph 3
```
 about TLS, H2 and esp. QUIC/H3. It feel like this stared out as an H1/TCP d
                                    ^^^^
```
After "It", use the third-person verb form "feels".

#### Section 4.1, paragraph 7
```
 actively inspected by the DUT/SUT. Also "Fail-Open" behavior MUST be disable
                                    ^^^^
```
A comma may be missing after the conjunctive/linking adverb "Also".

#### Section 4.2, paragraph 8
```
ur different classes of DUT/SUT: Extra Small (XS), Small (S), Medium (M), and
                                 ^^^^^^^^^^^
```
Consider using an extreme adjective for "small".

#### Section 4.2, paragraph 8
```
security vendors implement ACL decision making.) The configured ACL MUST NOT
                               ^^^^^^^^^^^^^^^
```
The noun "decision-making" (= the process of deciding something) is spelled
with a hyphen.

#### Section 4.2.1, paragraph 0
```
 the MSS. Delayed ACKs are permitted and the maximum client delayed ACK SHOUL
                                    ^^^^
```
Use a comma before "and" if it connects two independent clauses (unless they
are closely connected and short).

#### Section 4.3.1.3, paragraph 2
```
 the MSS. Delayed ACKs are permitted and the maximum server delayed ACK MUST
                                    ^^^^
```
Use a comma before "and" if it connects two independent clauses (unless they
are closely connected and short).

#### Section 4.3.1.3, paragraph 3
```
IPv6 with a ratio identical to the clients distribution ratio. Note: The IAN
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 4.3.3.1, paragraph 1
```
S throughput performance test with smallest object size. 3. Ensure that any 
                                   ^^^^^^^^
```
A determiner may be missing.

#### Section 4.3.4, paragraph 3
```
testbed software and hardware details a. DUT/SUT hardware/virtual configurati
                                      ^^
```
A word may be missing after "a".

#### Section 6.1, paragraph 1
```
se (FIN, ACK, FIN, ACK), and MUST NOT by RST. This prohibits TCP fast open, w
                                      ^^
```
Did you maybe mean "buy" or "be"?

#### Section 6.1, paragraph 18
```
sion with a more specific Kbit/s in parenthesis. * Time to First Byte (TTFB) 
                                 ^^^^^^^^^^^^^^
```
Did you mean "in parentheses"? "parenthesis" is the singular.

#### "H3", paragraph 2
```
he following criteria are the test results validation criteria. The test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### "H3", paragraph 4
```
f the traffic load profile. COMMENT: a. Number of failed application transac
                                     ^^
```
A word may be missing after "a".

#### "H3", paragraph 8
```
ial throughput) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### "H3", paragraph 8
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7, paragraph 0
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.2, paragraph 0
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.3.1, paragraph 1
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.3.2, paragraph 1
```
 value or does not fulfill the test results validation criteria. 7.1.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.3.2, paragraph 1
```
spected throughput within the test results validation criteria. Final test i
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.4, paragraph 1
```
he following criteria are the test results validation criteria. The Test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.4.2, paragraph 1
```
ons per second) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.4.2, paragraph 1
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.1.4.2, paragraph 1
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.1, paragraph 1
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.3.2, paragraph 4
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.3.2, paragraph 6
```
 value or does not fulfill the test results validation criteria. 7.2.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.3.2, paragraph 6
```
nections per second within the test results validation criteria. 7.3. HTTP Th
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.4.1, paragraph 2
```
he following criteria are the test results validation criteria. The test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.4.2, paragraph 2
```
ial throughput) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.4.2, paragraph 2
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.2.4.2, paragraph 3
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.2, paragraph 0
```
e sustain phase MUST meet the test results validation criteria "a" defined in
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.3, paragraph 0
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.3.2, paragraph 1
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.3.2, paragraph 3
```
 value or does not fulfill the test results validation criteria. 7.3.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.3.2, paragraph 4
```
spected throughput within the test results validation criteria and measure th
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.3.4, paragraph 0
```
he following criteria are the test results validation criteria. The Test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.4.1, paragraph 4
```
formance values and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.4.1, paragraph 5
```
the latency values within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.3.4.3, paragraph 1
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.1, paragraph 2
```
es are completed. Within the test results validation criteria, the DUT/SUT M
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.3.3, paragraph 2
```
he following criteria are the test results validation criteria. The Test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.4, paragraph 1
```
ent connection) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.4, paragraph 1
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.4, paragraph 1
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.4.1, paragraph 2
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.4.2, paragraph 2
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.4.4.2, paragraph 4
```
 value or does not fulfill the test results validation criteria. 7.5.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.1, paragraph 1
```
onnections capacity within the test results validation criteria. 7.6. TCP/HTT
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.3, paragraph 1
```
s and key strengths as well as forward looking stronger keys. Specific test 
                               ^^^^^^^^^^^^^^^
```
This word is normally spelled with a hyphen.

#### Section 7.5.3.2, paragraph 12
```
he following criteria are the test results validation criteria. The test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.4, paragraph 1
```
ons per second) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.4, paragraph 1
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.4, paragraph 1
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.4.1, paragraph 3
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.5.4.2, paragraph 2
```
SHOULD NOT be reported, if the above mentioned KPI (especially inspected thro
                               ^^^^^^^^^^^^^^^
```
The adjective "above-mentioned" is spelled with a hyphen.

#### Section 7.5.4.2, paragraph 4
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.1, paragraph 0
```
 value or does not fulfill the test results validation criteria. 7.6.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.1, paragraph 1
```
nections per second within the test results validation criteria. COMMENT: 7.7
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.1, paragraph 3
```
s and key strengths as well as forward looking stronger keys. Specific test 
                               ^^^^^^^^^^^^^^^
```
This word is normally spelled with a hyphen.

#### Section 7.6.3.2, paragraph 8
```
he following criteria are the test results validation criteria. The test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.3.3, paragraph 5
```
ial throughput) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.3.4, paragraph 0
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.3.4, paragraph 1
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.4, paragraph 1
```
e sustain phase MUST meet the test results validation criteria "a" defined in
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.4, paragraph 2
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.4.1, paragraph 2
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.4.1, paragraph 3
```
 value or does not fulfill the test results validation criteria. 7.7.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.6.4.2, paragraph 0
```
spected throughput within the test results validation criteria. Final test i
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.7.3.2, paragraph 2
```
he following criteria are the test results validation criteria. The Test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.7.3.3, paragraph 4
```
formance values and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.7.3.3, paragraph 4
```
the latency values within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.7.4.1, paragraph 0
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.7.4.1, paragraph 3
```
es are completed. Within the test results validation criteria, the DUT/SUT M
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.3.2, paragraph 5
```
he following criteria are the test results validation criteria. The Test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.3.3, paragraph 2
```
ent connection) and meets the test results validation criteria when it was ve
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.3.3, paragraph 2
```
 performance value within the test results validation criteria. Step 3 deter
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.3.3, paragraph 3
```
 performance value within the test results validation criteria. This test pr
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.3.3, paragraph 6
```
e sustain phase MUST meet the test results validation criteria "a" and "b" de
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.3.4, paragraph 0
```
e KPI metrics do not meet the test results validation criteria, the test proc
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.4, paragraph 2
```
es are completed. Within the test results validation criteria, the DUT/SUT i
                                  ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.4.1, paragraph 1
```
 value or does not fulfill the test results validation criteria. 7.9.4.3. Ste
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.8.4.1, paragraph 2
```
ent TCP connections within the test results validation criteria. 8. IANA Cons
                                    ^^^^^^^
```
An apostrophe may be missing.

#### Section 7.9.3.4, paragraph 0
```
* Accuracy of DUT/SUT statistics in term of vulnerabilities reporting A.2. T
                                 ^^^^^^^^^^
```
Did you mean the commonly used phrase "in terms of"?

#### Section 7.9.4, paragraph 1
```
tected attack traffic MUST be dropped and the session SHOULD be reset A.3.2.
                                     ^^^^
```
Use a comma before "and" if it connects two independent clauses (unless they
are closely connected and short).

#### Section 7.9.4.2, paragraph 0
```
he following criteria are the test results validation criteria. The test resu
                                   ^^^^^^^
```
An apostrophe may be missing.

#### Section 12.1, paragraph 2
```
e four different categories are Extra Small (XS), Small (S), Medium (M), and
                                ^^^^^^^^^^^
```
Consider using an extreme adjective for "small".

#### Section 12.1, paragraph 3
```
r the following categories are: Extra Small (XS) - Supported throughput less
                                ^^^^^^^^^^^
```
Consider using an extreme adjective for "small".

## Notes

This review is formatted in the "IETF Comments" Markdown format, see
https://github.com/mnot/ietf-comments. Generated by the "IETF Review Tool", see
https://github.com/larseggert/ietf-reviewtool.

