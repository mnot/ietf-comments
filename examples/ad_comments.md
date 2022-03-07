
# AD comments for draft-ietf-httpbis-proxy-status-08

## Comments

### Preserving existing members

Section 2 , paragraph 12, comment:
>    When adding a value to the Proxy-Status field, intermediaries SHOULD
>    preserve the existing members of the field to allow debugging of the
>    entire chain of intermediaries handling the request,

I'm surprised this is not a MUST? Are there any valid reasons for not observing
order?


## Nits

All comments below are about very minor potential issues that you may choose to
address in some way - or ignore - as you see fit. Some were flagged by
automated tools (via https://github.com/larseggert/ietf-reviewtool), so there
will likely be some false positives. There is no need to let me know what you
did with these suggestions.

"Table of Contents", paragraph 2, nit:
> critical infrastructure of many Web sites.

Nowadays, it's more common to write this as one word.

Section 2.1.1. , paragraph 6, nit:
> HTTP Status Code. When generating a HTTP response containing error, its

Use "an" instead of "a" if the following word starts with a vowel sound, e.g.
"an article", "an hour". (Also elsewhere.)

Section 2.1.2., paragraph 1, nit:
> protocol identifier is able to be expressed as an sf-token

Avoid the passive voice after "to be able to".
