curl -X POST \
    https://restful-booker.herokuapp.com/auth \
    -H 'Content-Type: application/json' \
    -d '{
        "username": "admin",
        "password": "password123"
    }'

curl -X POST \
    https://restful-booker.herokuapp.com/booking \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d '{
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : true,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }'


curl -X PUT \
    https://restful-booker.herokuapp.com/booking/1 \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json' \
    -H 'Cookie: token=abc123' \
    -d '{
        "firstname" : "James",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : true,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
            },
        "additionalneeds" : "Breakfast"
    }'