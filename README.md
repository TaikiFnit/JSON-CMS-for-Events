# JSON CMS for Events

イベント開催のための CMS

## Models

### users

* id: integer
* email: string
* name: string
* avatar_url: string
* google_id: string
* google_token: string # for google login
* created: date
* modified: date

### events

* id: integer
* title: sting
* description: string
* locale: string
* date: datetime
* created: date
* modified: date

### event_users ( Event に参加しているユーザー )

* id: integer
* user_id: ref
* event_id: ref
* presenter: bool
* slide_url: string
* created: date
* modified: date

## APIs

### GET `/api/events`

```json
{
  "events": [
    {
      "id": 1,
      "title": "2018年7月LT 開催のお知らせ",
      "description":
        "7月のLT会は, 2018年7月11日に開催します! 技術系だけでなくライフハックや、料理など趣味に関することでもぜひ発表してください 出入り自由なので少しだけという方も大歓迎です お待ちしております",
      "date": "20180711",
      "users": [
        {
          "id": 1,
          "name": "TaikiFnit",
          "email": "fnit@fnit.com",
          "avatar_url": "https://...",
          "presenter": "true"
          "slide_url": "https://",
        }
      ]
    }
  ]
}
```

### POST `/api/users/`
register user info.

#### request body

```json
{
  "email": "fnit@fnit.com",
  "name": "TaikiFnit",
  "avatar_url": "https://",
  "google_id": 123456,
  "google_token": "token"
}
```

#### response body
```json
{
  "status": true,
  "user": {
    "id": 1,
    "email": "fnit@fnit.com",
    "name": "TaikiFnit",
    "avatar_url": "https://",
    "google_id": 123456,
    "google_token": "token"
  }
}
```

