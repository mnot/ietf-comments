# Intdir Review draft-ietf-httpbis-proxy-status-06

I am an assigned INT directorate reviewer for
draft-ietf-httpbis-proxy-status-06.  These comments were written
primarily for the benefit of the Internet Area Directors.  Document
editors and shepherd(s) should treat these comments just like they
would treat comments from any other IETF contributors and resolve them
along with any other Last Call comments that have been received.  For
more details on the INT Directorate, see
https://datatracker.ietf.org/group/intdir/about/.

Overall, I find the document well written and understandable.  I only
have questions on clarifications and think the draft is ready with
nits for publication.

## Comments

### Abstract

Section Abstract could provide a little more explanation, such as one
or two examples of how to use the error reporting (as explained in the
Introduction).

### Adding proxy-status

At the beginning of Section 2, should it be stated that Proxy-Status
HTTP Fields are only added to responses towards the user agent?  So
explicitly state that an intermediary only adds Proxy-Status HTTP
Field towards the user agent and not towards the origin server?  (It
is implied by the use of the word "response" of course and other text
in this section.)

### Confusing paragraph

In Section 2.1.1, the following paragraph is a bit confusing to me:

   Unless a Proxy Error Type specifies otherwise, the presences of error
   often, but not always, indicates that response was generated by the
   proxy, not the origin server or any other upstream server.  For
   example, a proxy might attempt to correct an error, or part of a
   response might be forwarded before the error is encountered.

## Nits

### Reading of example

I read the sentence "For example, a proxy might ..." as the situation
where the next intermediary will generate the error message.  Is that
correct?


### next-hop

Section 2.1.2, it is not clear to me what "next-hop" implies.  The
intermediary or origin server selected for this response?  So with
the error reported to the user agent, is the intermediary or origin
server where the error occurred reported?
