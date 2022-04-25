# Gen AD review of draft-ietf-raw-ldacs-10

CC @larseggert

Thanks to Dale Worley for the General Area Review Team (Gen-ART) review
(https://mailarchive.ietf.org/arch/msg/gen-art/DhJCJ3dvXjga7paQ8GrXYswpX6E).

## Comments

### Unclear consensus

The datatracker state does not indicate whether the consensus boilerplate
should be included in this document.

### Missing references

No reference entries found for: `[KOB1987]`.

### Inclusive language

Found terminology that should be reviewed for inclusivity; see
https://www.rfc-editor.org/part2/#inclusive_language for background and more
guidance:

 * Term `master`; alternatives might be `active`, `central`, `initiator`,
   `leader`, `main`, `orchestrator`, `parent`, `primary`, `server`

### IP addresses

Found IP blocks or addresses not inside RFC5737/RFC3849 example ranges:
`7.3.2.2`, `7.3.2.1`, `7.3.2.3`, and `7.3.2.4`.

## Nits

All comments below are about very minor potential issues that you may choose to
address in some way - or ignore - as you see fit. Some were flagged by
automated tools (via https://github.com/larseggert/ietf-reviewtool), so there
will likely be some false positives. There is no need to let me know what you
did with these suggestions.

### Typos

#### Section 7.3.3, paragraph 1
```
-    Lastly, the SNP handles the transition from IPv6 packts to LDACS
+    Lastly, the SNP handles the transition from IPv6 packets to LDACS
+                                                         +
```

### Outdated references

Document references `draft-haindl-lisp-gb-atn-06`, but `-07` is the latest
available revision.

Document references `draft-ietf-rtgwg-atn-bgp-14`, but `-17` is the latest
available revision.

### IP addresses

Unparsable possible IP blocks or addresses: `1/3`, `1/2`, and `240/400`.

### Grammar/style

#### "Table of Contents", paragraph 1
```
band's increasing saturation in high- density areas and the limitations posed
                                ^^^^^^^^^^^^^
```
This word seems to be formatted incorrectly. Consider fixing the spacing or
removing the hyphen completely.

#### Section 1, paragraph 2
```
ications System (LDACS). Since central Europe has been identified as the area
                               ^^^^^^^^^^^^^^
```
If the term is a proper noun, use initial capitals.

#### Section 1, paragraph 3
```
ically LDACS enables IPv6 based air- ground communication related to aviation
                                ^^^^^^^^^^^
```
This word seems to be formatted incorrectly. Consider fixing the spacing or
removing the hyphen completely.

#### Section 1, paragraph 5
```
cols, the ATN/OSI, failed in the market place. In the context of safety-relat
                                 ^^^^^^^^^^^^
```
This is normally spelled as one word.

#### Section 5.2.1, paragraph 2
```
sponsible to guide the aircraft. Currently this is done by the air crew manu
                                 ^^^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "Currently".

#### Section 5.2.3, paragraph 2
```
eceiver via a separate data link. Currently the VDB data link is used. VDB is
                                  ^^^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "Currently".

#### Section 5.2.3, paragraph 2
```
VDB data link is used. VDB is a narrow-band single-purpose datalink without 
                                ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 6, paragraph 6
```
.1. LDACS Sub-Network An LDACS sub-network contains an Access Router (AR) an
                               ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 6, paragraph 7
```
ternal control plane of an LDACS sub-network interconnects the GSs. An LDACS
                                 ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 6, paragraph 8
```
 interconnects the GSs. An LDACS sub-network is illustrated in Figure 1. wir
                                 ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 6, paragraph 8
```
---------------+ Figure 1: LDACS sub-network with three GSs and one AS 7.2. T
                                 ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 6, paragraph 9
```
imultaneously support multiple bi-directional communications to the ASs unde
                               ^^^^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.1, paragraph 0
```
 last entity resides within the sub-network layer: the Sub-Network Protocol 
                                ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.2, paragraph 2
```
channel. The LDACS GS supports bi-directional links to multiple aircraft unde
                               ^^^^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.3, paragraph 4
```
roadcast and packet mode voice) bi-directional exchange of user data. If user
                                ^^^^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.3.2.2, paragraph 1
```
ontrol plane data over the LDACS sub-network. The security service provides f
                                 ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.3.2.2, paragraph 1
```
ata communication over the LDACS sub-network. Note that the SNP security ser
                                 ^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.3.2.2, paragraph 3
```
ers between non-connected LDACS sub-networks or different aeronautical data 
                                ^^^^^^^^^^^^
```
This word is normally spelled as one.

#### Section 7.3.2.2, paragraph 3
```
data links are handled by the FCI multi- link concept. 8. Reliability and Ava
                                  ^^^^^^^^^^^
```
This word seems to be formatted incorrectly. Consider fixing the spacing or
removing the hyphen completely.

#### Section 8.2, paragraph 4
```
CS is yet to be defined. A Differentiated Services- (DiffServ) based solutio
                         ^^^^^^^^^^^^^^^^^^^^^^^^^
```
The plural noun "Services" cannot be used with the article "A". Did you mean "A
Differentiated service" or "Differentiated Services"?

#### Section 8.2, paragraph 4
```
DiffServ) based solution with a small number of priorities is to be expected
                              ^^^^^^^^^^^^^^^^^
```
Specify a number, remove phrase, use "a few", or use "some".

#### Section 13, paragraph 15
```
tps://sike.org/>. [ROY2020] Roy, S.S.. and A. Basso, "High-Speed Instruction
                                    ^^
```
Two consecutive dots.

#### Section 13, paragraph 23
```
f Flight Measurement Results", IEEE 32th Digital Avionics Systems Conference
                                    ^^^^
```
The suffix does not match the ordinal number.

#### Section 13, paragraph 27
```
nich, N., Micallef, J., Klauspeter, H.., MacBride, J., Sacre, P., v.d. Eiden
                                     ^^
```
Two consecutive dots.

## Notes

This review is formatted in the "IETF Comments" Markdown format, see
https://github.com/mnot/ietf-comments. Generated by the "IETF Review Tool", see
https://github.com/larseggert/ietf-reviewtool.

