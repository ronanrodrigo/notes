# Wellhub requests

## Conexão Fitness

```json
{
  "data": {
    "checkInWalkInTransaction": {
      "partner": {
        "id": "d44132c5-b467-41ec-970a-7be75c239aa0",
        "name": "Conexão Fitness",
        "address": "Av. Alm. Jaceguay, 179 - Santo Antônio, Joinville - SC, 89218-065, Brazil",
        "__typename": "CheckInWalkInPartner"
      },
      "product": {
        "id": "02b4fd65-7b7e-4a51-9cd5-1e523bf573ad",
        "name": "Musculação",
        "__typename": "CheckInWalkInProducts"
      },
      "transaction": {
        "id": "5f97dd17-a5ef-4649-9671-333734d6f3f2",
        "validatedAt": "12h02 • 26 jun",
        "occurDate": "2026-06-26T12:02:09.547Z",
        "expiresAt": "2026-06-26T12:22:09.547Z",
        "status": "CONFIRMED",
        "timeUntilExpires": -25579,
        "__typename": "CheckInWalkInTransaction"
      },
      "header": {
        "title": {
          "key": "checkin_validation.confirmed.header",
          "params": null,
          "__typename": "Translation"
        },
        "__typename": "CheckInWalkInHeader"
      },
      "cancellation": null,
      "integrationCodeV2": {
        "code": "3504941345548",
        "type": "NUMERIC",
        "isCustomCode": null,
        "hasBarcodeExceedLimitation": null,
        "__typename": "CheckInWalkInIntegrationCode"
      },
      "share": {
        "label": {
          "key": "checkin_validation.confirmed.share.button_label",
          "params": null,
          "__typename": "Translation"
        },
        "__typename": "CheckInWalkInShare"
      },
      "caption": null,
      "joinLiveClassButton": null,
      "checkInNotifications": [],
      "extraInfo": [
        {
          "icon": "BuildingFilled",
          "label": {
            "value": "Av. Alm. Jaceguay, 179 - Santo Antônio, Joinville - SC, 89218-065, Brazil",
            "__typename": "Label"
          },
          "__typename": "CheckInWalkInExtraInfo"
        },
        {
          "icon": "TimeFilled",
          "label": {
            "value": "12h02 • 26 jun",
            "__typename": "Label"
          },
          "__typename": "CheckInWalkInExtraInfo"
        }
      ],
      "__typename": "CheckInWalkIn"
    }
  }
}
```

## Checkin

```bash
curl 'https://mobile-api.gympass.com/enduser/v1/frontdoor' \
-X POST \
-H 'Host: mobile-api.gympass.com' \
-H 'Accept: */*' \
-H 'baggage: sentry-environment=production,sentry-public_key=d49d00ed86744726a7e622bd0ceeaa66,sentry-trace_id=31fe32cf09884f15851b8a35dc5e7670,sentry-org_id=4504963224764416' \
-H 'device-session-id: 1782512634705' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqd3Quc2lna2V5In0.eyJleHAiOjE3ODI1MTY0OTYsImlhdCI6MTc4MjUxMjg5NiwiYXV0aF90aW1lIjoxNzgyNTA5MjA3LCJqdGkiOiI0NzVmODMzOC0yMmQ2LTRhZDItOWQyMi03N2RhOGJlMTQ5NmEiLCJpc3MiOiJodHRwczovL2lkZW50aXR5Lmd5bXBhc3MuY29tL2F1dGgvcmVhbG1zL21hc3RlciIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJmOjE4NTYzNmI3LTU1MDYtNDY0OS04ZmUzLWMxYzg1Y2I4MzIxOTphODJjMTgxZC0xMDI5LTQ0MDctYWVkZS1hZDc1NWU3NWM5MDYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJtb2JpbGUtc3NvIiwic2Vzc2lvbl9zdGF0ZSI6Ino5NDAyMmEyMy1kMjY2LTQxMWMtODUyNy0yZGNjNDZjNTQzZDEiLCJhY3IiOiIwIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInNjb3BlIjoib3BlbmlkIGd5bXBhc3MtY29yZSB0YWd1cyBtb2JpbGVfcm9sZXMgZ3ltcGFzcy1tb2JpbGUgZW1haWwiLCJzaWQiOiJ6OTQwMjJhMjMtZDI2Ni00MTFjLTg1MjctMmRjYzQ2YzU0M2QxIiwiZmlkIjoidGFndXMiLCJlbGlnaWJpbGl0eV90eXBlIjoiQVNTT0NJQVRFIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInVzZXJfc2x1ZyI6InJvbmFuLXJvZHJpZ28tbnVuZXMtYTgyYzE4MWQtMTAyOS00NDA3LWFlZGUtYWQ3NTVlNzVjOTA2Iiwicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdLCJjbGllbnRfdHlwZSI6IlNUQU5EQVJEIiwibG9jYWxlIjoicHQtQlIiLCJoYXNfcHVzaF90b2tlbiI6ZmFsc2UsImNsaWVudF9za3VzIjpbIkZBTUlMWV9NRU1CRVIiLCJHWU1QQVNTX0NPUkUiLCJJTlRFUk5BVElPTkFMX0NIRUNLSU4iLCJXRUxMSFVCX1NDT1JFIl0sInVuaXF1ZV90b2tlbiI6IjM1MDQ5NDEzNDU1NDgiLCJvcmRlcl9zdGF0dXMiOiJBQ1RJVkUiLCJjb3VudHJ5X2NvZGUiOiJCUiIsInVpZCI6ImE4MmMxODFkLTEwMjktNDQwNy1hZWRlLWFkNzU1ZTc1YzkwNiIsImJsb2NrZWQiOmZhbHNlLCJsYXN0X2NoZWNraW5fYXQiOiIyMDI2LTA2LTI2VDE1OjAyOjEwWiIsIm5hbWUiOiJSb25hbiBSb2RyaWdvIE51bmVzIiwiaGFzX2NsYWltIjpmYWxzZSwiZW1haWwiOiJyb25hbi5udW5lc0BtZS5jb20ifQ.xJw2bKw2iKhcQ8Per70xDYPrJGzNp8_H2XLbIUAgLxM' \
-H 'x-device-pixel-ratio: 3' \
-H 'app-version: 10.53.5' \
-H 'Accept-Language: pt-BR' \
-H 'sentry-trace: 31fe32cf09884f15851b8a35dc5e7670-a139b6947a2de39b' \
-H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148' \
-H 'Connection: keep-alive' \
-H 'timezone: America/Sao_Paulo' \
-H 'Content-Type: application/json' \
--data-raw '{...}' \
--proxy http://localhost:9495
```

## Identity

```bash
curl 'https://identity.gympass.com/auth/realms/master/protocol/openid-connect/userinfo' -X POST \
-H 'Host: identity.gympass.com' \
-H 'baggage: sentry-environment=production,sentry-public_key=d49d00ed86744726a7e622bd0ceeaa66,sentry-trace_id=b884cc751ab847aa95779972ceb44b37,sentry-org_id=4504963224764416' \
-H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJqd3Quc2lna2V5In0...' \
-H 'app-version: 10.53.5' \
-H 'Accept-Language: pt-BR,pt;q=0.9' \
-H 'sentry-trace: b884cc751ab847aa95779972ceb44b37-a04d35613286620c' \
-H 'Accept: */*' \
-H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148' \
-H 'Connection: keep-alive' \
-H 'x-device-id: C32B36F91ECA4F0FAC575F5756E85AE5'
```
