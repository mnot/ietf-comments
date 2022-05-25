# Gen AD review of draft-ietf-rats-yang-tpm-charra-16

CC @larseggert

Thanks to Roni Even for the General Area Review Team (Gen-ART) review
(https://mailarchive.ietf.org/arch/msg/gen-art/LVJgDXJ4Bwr2DuJ2ytGxONSTSQ8).

## Comments

### Too many authors

The document has eight authors, which exceeds the recommended author limit. Has
the sponsoring AD agreed that this is appropriate?

### IANA

The IANA review of this document seems to not have concluded yet.

### Missing references

No reference entries found for: `[name]`, `[event-number]`,
`[tpm20-hash-algo]`, `[node-id]`, and `[pcr-index]`.

### DOWNREFs

Possible DOWNREF from this Standards Track doc to `[BIOS-Log-Event-Type]`. If
so, the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[NIST-SP800-56A]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM1.2-Commands]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-9797-1]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[NIST-SP800-38C]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM2.0]`. If so, the IESG
needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM2.0-Structures]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-10118-3]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-10116]`. If so, the
IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-14888-3]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM1.2]`. If so, the IESG
needs to approve it.

Possible DOWNREF from this Standards Track doc to `[NIST-PUB-FIPS-202]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM1.2-Structures]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[IEEE-Std-1363a-2004]`. If
so, the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[netequip-boot-log]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[NIST-SP800-38D]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[yang-parameters]`. If so,
the IESG needs to approve it.

DOWNREF `[I-D.ietf-rats-architecture]` from this Proposed Standard to
Informational `draft-ietf-rats-architecture`. (For IESG discussion. It seems
this DOWNREF was not mentioned in the Last Call and also seems to not appear in
the DOWNREF registry.)

DOWNREF `[I-D.ietf-rats-tpm-based-network-device-attest]` from this Proposed
Standard to Informational `draft-ietf-rats-tpm-based-network-device-attest`.
(For IESG discussion. It seems this DOWNREF was not mentioned in the Last Call
and also seems to not appear in the DOWNREF registry.)

Possible DOWNREF from this Standards Track doc to `[bios-log]`. If so, the IESG
needs to approve it.

Possible DOWNREF from this Standards Track doc to `[xml-registry]`. If so, the
IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM2.0-Arch]`. If so, the
IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TPM2.0-Key]`. If so, the
IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ima-log]`. If so, the IESG
needs to approve it.

Possible DOWNREF from this Standards Track doc to `[NIST-SP800-108]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[TCG-Algos]`. If so, the
IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-15946-1]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[IEEE-Std-1363-2000]`. If
so, the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-18033-3]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[ISO-IEC-9797-2]`. If so,
the IESG needs to approve it.

Possible DOWNREF from this Standards Track doc to `[NIST-SP800-38F]`. If so,
the IESG needs to approve it.

### Inclusive language

Found terminology that should be reviewed for inclusivity; see
https://www.rfc-editor.org/part2/#inclusive_language for background and more
guidance:

 * Term `guy`; alternatives might be `individual`, `people`, `person`

## Nits

All comments below are about very minor potential issues that you may choose to
address in some way - or ignore - as you see fit. Some were flagged by
automated tools (via https://github.com/larseggert/ietf-reviewtool), so there
will likely be some false positives. There is no need to let me know what you
did with these suggestions.

### Boilerplate

Document still refers to the "Simplified BSD License", which was corrected in
the TLP on September 21, 2021. It should instead refer to the "Revised BSD
License".

### Outdated references

Document references `draft-ietf-rats-tpm-based-network-device-attest-13`, but
`-14` is the latest available revision.

Document references `draft-ietf-netconf-keystore-23`, but `-24` is the latest
available revision.

### Grammar/style

#### "RATS", paragraph 0
```
cument defines YANG RPCs and a small number of configuration nodes required
                             ^^^^^^^^^^^^^^^^^
```
Specify a number, remove phrase, use "a few", or use "some".

#### Section 2, paragraph 1
```
tion 2.1.2.3 with prefix 'taa'. Additionally references are made to [RFC8032
                                ^^^^^^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "Additionally".

#### Section 2.1.1.3.1, paragraph 2
```
PC challenge requesting PCRs 0-7 from a SHA-256 bank could look like the foll
                                      ^
```
Use "an" instead of "a" if the following word starts with a vowel sound, e.g.
"an article", "an hour".

#### Section 2.1.1.5, paragraph 8
```
/ typedef pcr { type uint8 { range "0..31"; } description "Valid index number
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 18
```
n Quotes returned from the TPM. Additionally if more bytes are sent, the non
                                ^^^^^^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "Additionally".

#### Section 2.1.1.5, paragraph 29
```
 pull only the objects related to these TPM(s). If it does not exist, all qu
                                  ^^^^^^^^^
```
The plural demonstrative "these" does not agree with the singular noun "TPM".

#### Section 2.1.1.5, paragraph 33
```
ngle PCR has changed? To help this happen, if the Attester does know specifi
                                   ^^^^^^
```
The verb "happen" is plural. Did you mean: "happens"? Did you use a verb
instead of a noun?

#### Section 2.1.1.5, paragraph 33
```
By comparing this information to the what has previously been validated, it
                                 ^^^^^^^^
```
Did you mean "what"?

#### Section 2.1.1.5, paragraph 34
```
an unsigned PCR value is actually that that within a quote. If there is a dif
                                  ^^^^^^^^^
```
Possible typo: you repeated a word.

#### Section 2.1.1.5, paragraph 35
```
ing ima-event { description "Defines an hash log extend event for IMA measur
                                     ^^
```
Use "a" instead of "an" if the following word doesn't start with a vowel sound,
e.g. "a sentence", "a university".

#### Section 2.1.1.5, paragraph 42
```
type binary; description "Content of an log event which matches 1:1 with a u
                                     ^^
```
Use "a" instead of "an" if the following word doesn't start with a vowel sound,
e.g. "a sentence", "a university".

#### Section 2.1.1.5, paragraph 42
```
ned within the log. Log entries subsequent to this will be passed to the requ
                                ^^^^^^^^^^^^^
```
Consider using "after".

#### Section 2.1.1.5, paragraph 42
```
e beginning of the log. Entries subsequent to this will be passed to the requ
                                ^^^^^^^^^^^^^
```
Consider using "after".

#### Section 2.1.1.5, paragraph 42
```
extraction. The next log entry subsequent to this timestamp is to be sent.";
                               ^^^^^^^^^^^^^
```
Consider using "after".

#### Section 2.1.1.5, paragraph 42
```
e definition enabling verifiers or relying parties to discover the informatio
                                   ^^^^^^^
```
The verb "rely" requires the preposition "on" (or "upon").

#### Section 2.1.1.5, paragraph 42
```
hw:entity-mib"; type int32 { range "1..2147483647"; } config false; descript
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 42
```
hw:entity-mib"; type int32 { range "1..2147483647"; } config false; descript
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 42
```
ory true; description "Indicates the compute node measured by this TPM."; } l
                                 ^^^^^^^^^^^
```
After "the", the verb "compute" doesn't fit. Is "compute" spelled correctly? If
"compute" is the first word in a compound adjective, use a hyphen between the
two words. Using the verb "compute" as a noun may be non-standard.

#### Section 2.1.1.5, paragraph 43
```
."; } } leaf-list tpm12-pcrs { when "../firmware-version = 'taa:tpm12'"; typ
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 43
```
sor."; } list tpm20-pcr-bank { when "../firmware-version = 'taa:tpm20'"; key
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 43
```
ue 0; description "The TPM currently is currently running normally and is re
                           ^^^^^^^^^^^^^^^^^^^^^^
```
Adverb repetition.

#### Section 2.1.1.5, paragraph 45
```
ist tpm12-asymmetric-signing { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmwar
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 45
```
 tpm12-asymmetric-signing { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmware-v
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 46
```
ms."; } leaf-list tpm12-hash { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmwar
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 46
```
"; } leaf-list tpm12-hash { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmware-v
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 46
```
ist tpm20-asymmetric-signing { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmwar
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 46
```
 tpm20-asymmetric-signing { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmware-v
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 46
```
ms."; } leaf-list tpm20-hash { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmwar
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 46
```
"; } leaf-list tpm20-hash { when "../../tpm:tpms" + "/tpm:tpm[tpm:firmware-v
                                     ^^
```
Two consecutive dots.

#### Section 2.1.1.5, paragraph 47
```
escription "This module defines a identities for asymmetric algorithms. Copy
                                ^^^^^^^^^^^^
```
The plural noun "identities" cannot be used with the article "a". Did you mean
"a identity" or "identities"?

#### Section 2.1.1.5, paragraph 49
```
base symmetric; description "Block cipher with various key sizes (Triple Dat
                                   ^^^^^^
```
The singular proper name "Block" must be used with a third-person or a past
tense verb.

#### Section 2.1.1.5, paragraph 49
```
ficient cryptographic protection. However it is still useful for hash algori
                                  ^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "However".

#### Section 2.1.2.3, paragraph 4
```
ietf-tpm-remote-attestation.yang. However the full definition of Table 3 of
                                  ^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "However".

#### Section 2.1.2.3, paragraph 7
```
 module ietf-tpm-remote-attestation.yang specified in this document defines
                                    ^^^^
```
If a new sentence starts here, add a space and start with an uppercase letter.

#### Section 2.1.2.3, paragraph 12
```
as 'rw', it is system generated. Therefore it should not be possible for an
                                 ^^^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "Therefore".

#### Section 2.1.2.3, paragraph 17
```
ulnerabilities on those systems. Therefore RPCs should be protected by NACM
                                 ^^^^^^^^^
```
A comma may be missing after the conjunctive/linking adverb "Therefore".

#### Section 2.1.2.3, paragraph 18
```
. For the YANG module ietf-tcg-algs.yang, please use care when selecting spec
                                    ^^^^
```
If a new sentence starts here, add a space and start with an uppercase letter.



