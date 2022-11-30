from voluptuous import Schema, PREVENT_EXTRA, Optional

"""
Параметр, показывающий, что все поля обязательные
        required=True,

Параметр, показывающий, что дополнительных полей не должно передаваться
        extra=PREVENT_EXTRA

Параметр, показывающий, что дополнительных полей не должно передаваться
        extra=ALLOW_EXTRA
"""
get_single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            Optional("avatar"): str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    required=True,
    extra=PREVENT_EXTRA
)

post_create_user_schema = Schema(
        {
            "name": str,
            Optional("job"): str,
            "id": str,
            "createdAt": str
        },
        required=True,
        extra=PREVENT_EXTRA
    )

put_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

post_register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)
