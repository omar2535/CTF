Use a proxy

When logging in, we will see that the re-directs for login are using page changes with a `next-page` id:

```html
<!DOCTYPE html>
<head>
    <title>flag</title>
</head>
<body>
    <script>
        setTimeout(function () {
           // after 2 seconds
           window.location = "/next-page/id=bF90aGVfd2F5X2RmNDRjOTRjfQ==";
        }, 0.5)
      </script>
    <p></p>
</body>
```

Simply decode from base64 and we can see that it's part of a flag. There are a total of 2 requests. So we just decode the `id` of both.

