# facebook-likes-for-datanitro reviewer patterns

Snapshot: `191e2372d5d803e9dadbfdd15c98c4d6690eceb4`. [Repository](https://github.com/seerinteractive/facebook-likes-for-datanitro).

These reviewer patterns apply to the pinned snapshot. Accepted items passed independent refutation and deterministic evidence checks at the pinned snapshot. Quotes verify source presence; they do not prove every interpretation or current production behavior.

Coverage: 1 extracted business rules; 0 accepted, 0 uncertain, 1 rejected, 0 pending audit. 1 extracted dependencies; 1 accepted, 0 uncertain, 0 rejected, 0 pending audit.

Scanned branch: `master`. GitHub default branch: `master`.

## Accepted business rules

No business rule has cleared the acceptance gates for this snapshot.

## Accepted dependencies

### Facebook Graph API (external system)

facebook_likes(url) requests https://graph.facebook.com/?ids=<url>, decodes the response as JSON, and reads shares from the input URL's response object.

**Keep in sync:** Request construction and response parsing must agree on the URL identity and response shape: ids supplies the URL used as the top-level lookup key, and shares is read within that object.

**Why reviewers need it:** Changes to the endpoint or response format require checking the URL-key lookup and shares extraction together.

**Evidence:**

- [facebook-likes-for-datanitro/functions.py:8](https://github.com/seerinteractive/facebook-likes-for-datanitro/blob/191e2372d5d803e9dadbfdd15c98c4d6690eceb4/functions.py#L8)

  ```text
  def facebook_likes(url):
  ```
- [facebook-likes-for-datanitro/functions.py:9](https://github.com/seerinteractive/facebook-likes-for-datanitro/blob/191e2372d5d803e9dadbfdd15c98c4d6690eceb4/functions.py#L9)

  ```text
      facebook_url = "https://graph.facebook.com/?ids=" + url
  ```
- [facebook-likes-for-datanitro/functions.py:10](https://github.com/seerinteractive/facebook-likes-for-datanitro/blob/191e2372d5d803e9dadbfdd15c98c4d6690eceb4/functions.py#L10)

  ```text
      raw_data = urllib2.urlopen(facebook_url).read()
  ```
- [facebook-likes-for-datanitro/functions.py:11](https://github.com/seerinteractive/facebook-likes-for-datanitro/blob/191e2372d5d803e9dadbfdd15c98c4d6690eceb4/functions.py#L11)

  ```text
      formatted_data = json.loads(raw_data)
  ```
- [facebook-likes-for-datanitro/functions.py:12](https://github.com/seerinteractive/facebook-likes-for-datanitro/blob/191e2372d5d803e9dadbfdd15c98c4d6690eceb4/functions.py#L12)

  ```text
      likes = formatted_data[url].get('shares', 0)
  ```

## Provenance and limits

Raw extraction: `out/facebook-likes-for-datanitro.json`. Independent audit: `audit/facebook-likes-for-datanitro.json` in the knowledge report bundle. The original whitespace-normalized `.verified.json` files are not acceptance inputs. This report does not assert a complete semantic audit of every tracked file, deployment verification, or owner approval. Excluded candidate text and audit rationale are kept in the separate review report.
