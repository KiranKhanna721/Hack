# Hack: Facebook Graph API Access Token Tools

Hackathon scripts for working with the Facebook Graph API: getting, checking and extending access tokens, and reading page data.

## Contents

### Python
| File | Purpose |
|------|---------|
| `define.py` | Shared credentials and settings (app ID, app secret, access token, Graph API version) |
| `access_token.py` | Calls the `debug_token` endpoint to inspect an access token |
| `long_accessToken.py` | Exchanges a short-lived token for a long-lived one |

### PHP (`PHP-file/`)
| File | Purpose |
|------|---------|
| `define.php` | Credentials and settings |
| `obtain_access.php` | Gets an access token with the Facebook PHP Graph SDK |
| `get_page.php` | Reads Facebook page data |
| `index.php` | Simple directory listing page |

The PHP dependencies (`facebook/graph-sdk`) are managed with Composer.

## Getting started

```bash
# Python
pip install requests
python access_token.py

# PHP
cd PHP-file
composer install
php -S localhost:8000
```

> Put your own Facebook app credentials in `define.py` and `define.php`. Don't commit real tokens.
