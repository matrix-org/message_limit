```
spam_checker:
  - module: limiter.Limiter
    config:
      limit: 750
      protected_rooms:
        - "!foobarbaz:matrix.org"
        - "!barbazquz:matrix.org"
```
